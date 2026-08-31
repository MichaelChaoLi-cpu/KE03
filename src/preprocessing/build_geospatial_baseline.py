#!/usr/bin/env python3
"""Clip and classify the pre-event Nepal OSM snapshot for the event corridor."""

from __future__ import annotations

import argparse
import csv
import os
import subprocess
import tempfile
from pathlib import Path

import geopandas as gpd
import pandas as pd


BBOX = (84.5, 27.55, 85.95, 28.60)
SOURCE_RELATIVE = Path(
    "data/raw/geospatial/osm/pre_event_2026-08-25/nepal-260825.osm.pbf"
)
OUTPUT_RELATIVE = Path("data/processed/geospatial/base/osm_pre_event_aoi.gpkg")
ADMIN_RELATIVE = Path("data/processed/geospatial/base/event_area_admin.gpkg")
INVENTORY_RELATIVE = Path(
    "data/exp/data-briefing/tables/osm_pre_event_layer_inventory.csv"
)
GEOMETRY_AUDIT_RELATIVE = Path(
    "data/exp/data-briefing/tables/osm_pre_event_geometry_audit.csv"
)
TARGET_CRS = "EPSG:32645"


def present(series: pd.Series) -> pd.Series:
    return series.notna() & series.astype(str).str.strip().ne("")


def text_blob(frame: gpd.GeoDataFrame) -> pd.Series:
    candidates = [
        column
        for column in (
            "name",
            "amenity",
            "healthcare",
            "shop",
            "office",
            "tourism",
            "man_made",
            "other_tags",
        )
        if column in frame.columns
    ]
    if not candidates:
        return pd.Series("", index=frame.index, dtype="string")
    return frame[candidates].fillna("").astype(str).agg(" ".join, axis=1).str.lower()


def classify_facilities(frame: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    blob = text_blob(frame)
    categories = pd.Series(pd.NA, index=frame.index, dtype="string")
    patterns = {
        "health": r"hospital|clinic|health_post|healthcare|doctors|pharmacy",
        "education": r"school|college|university|kindergarten",
        "emergency": r"police|fire_station|shelter",
        "government_community": r"government|townhall|community_centre|social_facility",
        "transport_energy": r"bus_station|ferry_terminal|fuel|charging_station",
        "market_finance": r"marketplace|bank|atm",
        "water_sanitation": r"drinking_water|water_point|toilets",
    }
    for category, pattern in patterns.items():
        mask = categories.isna() & blob.str.contains(pattern, regex=True)
        categories.loc[mask] = category
    result = frame.loc[categories.notna()].copy()
    result["facility_category"] = categories.loc[result.index]
    return result


def extract_source_layers(source: Path, destination: Path) -> None:
    west, south, east, north = BBOX
    env = os.environ.copy()
    env["PROJ_LIB"] = "/opt/homebrew/share/proj"
    subprocess.run(
        [
            "ogr2ogr",
            "-f",
            "GPKG",
            str(destination),
            str(source),
            "points",
            "lines",
            "multipolygons",
            "-spat",
            str(west),
            str(south),
            str(east),
            str(north),
            "-skipfailures",
        ],
        check=True,
        env=env,
    )


def write_layers(output: Path, layers: dict[str, gpd.GeoDataFrame]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    first = True
    for layer_name, frame in layers.items():
        frame.to_file(
            output,
            layer=layer_name,
            driver="GPKG",
            mode="w" if first else "a",
            engine="pyogrio",
        )
        first = False


def read_clean_layer(path: Path, layer: str) -> tuple[gpd.GeoDataFrame, dict[str, object]]:
    frame = gpd.read_file(path, layer=layer, on_invalid="ignore")
    null_geometry = int(frame.geometry.isna().sum())
    nonnull = frame.loc[frame.geometry.notna()].copy()
    invalid_geometry = int((~nonnull.geometry.is_valid).sum())
    clean = nonnull.loc[nonnull.geometry.is_valid].copy()
    audit = {
        "source_layer": layer,
        "rows_read": len(frame),
        "null_geometry_rows_dropped": null_geometry,
        "invalid_geometry_rows_dropped": invalid_geometry,
        "rows_retained": len(clean),
    }
    return clean, audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    source = root / SOURCE_RELATIVE
    output = root / OUTPUT_RELATIVE
    admin = root / ADMIN_RELATIVE
    inventory = root / INVENTORY_RELATIVE
    geometry_audit = root / GEOMETRY_AUDIT_RELATIVE
    if not source.exists():
        raise FileNotFoundError(source)
    if not admin.exists():
        raise FileNotFoundError(admin)

    with tempfile.TemporaryDirectory(prefix="ke03-osm-") as temporary:
        clipped = Path(temporary) / "osm_aoi_all.gpkg"
        extract_source_layers(source, clipped)
        points, points_audit = read_clean_layer(clipped, "points")
        lines, lines_audit = read_clean_layer(clipped, "lines")
        polygons, polygons_audit = read_clean_layer(clipped, "multipolygons")

    districts_metric = gpd.read_file(admin, layer="districts").to_crs(TARGET_CRS)
    core_metric = districts_metric.geometry.union_all()
    network_metric = core_metric.buffer(10_000)
    core_geometry = gpd.GeoSeries([core_metric], crs=TARGET_CRS).to_crs(points.crs).iloc[0]
    network_geometry = (
        gpd.GeoSeries([network_metric], crs=TARGET_CRS).to_crs(points.crs).iloc[0]
    )
    points = points.loc[points.geometry.intersects(core_geometry)].copy()
    lines = lines.loc[lines.geometry.intersects(network_geometry)].copy()
    polygons = polygons.loc[polygons.geometry.intersects(core_geometry)].copy()

    roads = lines.loc[present(lines["highway"])].copy()
    roads_metric = roads.to_crs(TARGET_CRS)
    roads["length_m"] = roads_metric.geometry.length.values
    road_tags = roads.get("other_tags", pd.Series("", index=roads.index)).fillna("")
    roads["is_bridge"] = road_tags.str.contains('"bridge"=>', regex=False)
    bridges = roads.loc[roads["is_bridge"]].copy()

    waterways = lines.loc[present(lines["waterway"])].copy()
    waterways_metric = waterways.to_crs(TARGET_CRS)
    waterways["length_m"] = waterways_metric.geometry.length.values

    settlements = points.loc[present(points["place"])].copy()
    facilities = classify_facilities(points)
    buildings = polygons.loc[present(polygons["building"])].copy()

    layers = {
        "roads": roads,
        "bridges": bridges,
        "waterways": waterways,
        "settlements": settlements,
        "facilities": facilities,
        "buildings": buildings,
    }
    write_layers(output, layers)

    inventory.parent.mkdir(parents=True, exist_ok=True)
    with inventory.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "layer",
                "feature_count",
                "crs",
                "source_snapshot",
                "bbox",
                "analysis_extent",
            ],
        )
        writer.writeheader()
        for layer_name, frame in layers.items():
            writer.writerow(
                {
                    "layer": layer_name,
                    "feature_count": len(frame),
                    "crs": str(frame.crs),
                    "source_snapshot": "2026-08-25",
                    "bbox": ",".join(map(str, BBOX)),
                    "analysis_extent": (
                        "districts_plus_10km"
                        if layer_name in {"roads", "bridges", "waterways"}
                        else "three_core_districts"
                    ),
                }
            )
    geometry_audit.parent.mkdir(parents=True, exist_ok=True)
    with geometry_audit.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "source_layer",
                "rows_read",
                "null_geometry_rows_dropped",
                "invalid_geometry_rows_dropped",
                "rows_retained",
            ],
        )
        writer.writeheader()
        writer.writerows([points_audit, lines_audit, polygons_audit])
    print({name: len(frame) for name, frame in layers.items()})
    print({"geometry_audit": [points_audit, lines_audit, polygons_audit]})


if __name__ == "__main__":
    main()
