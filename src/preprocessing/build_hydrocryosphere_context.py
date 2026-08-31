#!/usr/bin/env python3
"""Build river and glacier context layers for the Nepal event corridor."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely import force_2d


HYDRO_ARCHIVE_RELATIVE = Path(
    "data/raw/geospatial/hydrography/hydrorivers_v10_asia/"
    "HydroRIVERS_v10_as_shp.zip"
)
RGI_ARCHIVE_RELATIVE = Path(
    "data/raw/geospatial/cryosphere/rgi7_south_asia_east/"
    "rgi2000-v7.0-g-15_south_asia_east.zip"
)
ADMIN_RELATIVE = Path("data/processed/geospatial/base/event_area_admin.gpkg")
REFERENCE_RELATIVE = Path(
    "data/processed/geospatial/reference/unosat_event_reference.gpkg"
)
OUTPUT_RELATIVE = Path(
    "data/processed/geospatial/context/hydrocryosphere_context.gpkg"
)
GLACIER_TABLE_RELATIVE = Path(
    "data/processed/geospatial/context/glacier_event_context.parquet"
)
AUDIT_RELATIVE = Path(
    "data/exp/data-preprocessing/hydrocryosphere_context_audit.csv"
)
TARGET_CRS = "EPSG:32645"
CONTEXT_BUFFER_M = 50_000


def source_paths(root: Path) -> tuple[str, str]:
    hydro_archive = root / HYDRO_ARCHIVE_RELATIVE
    rgi_archive = root / RGI_ARCHIVE_RELATIVE
    hydro = (
        f"/vsizip/{hydro_archive}/HydroRIVERS_v10_as_shp/"
        "HydroRIVERS_v10_as.shp"
    )
    rgi = (
        f"/vsizip/{rgi_archive}/"
        "RGI2000-v7.0-G-15_south_asia_east.shp"
    )
    return hydro, rgi


def clean(frame: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    nonnull = frame.loc[frame.geometry.notna()].copy()
    nonnull.geometry = force_2d(nonnull.geometry.array)
    return nonnull.loc[nonnull.geometry.is_valid & ~nonnull.geometry.is_empty].copy()


def write_layers(path: Path, layers: dict[str, gpd.GeoDataFrame]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    first = True
    for layer, frame in layers.items():
        frame.to_file(
            path,
            layer=layer,
            driver="GPKG",
            mode="w" if first else "a",
            engine="pyogrio",
        )
        first = False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    hydro_source, rgi_source = source_paths(root)
    for required in (
        root / HYDRO_ARCHIVE_RELATIVE,
        root / RGI_ARCHIVE_RELATIVE,
        root / ADMIN_RELATIVE,
        root / REFERENCE_RELATIVE,
    ):
        if not required.exists():
            raise FileNotFoundError(required)

    districts = gpd.read_file(root / ADMIN_RELATIVE, layer="districts")
    context_metric = districts.to_crs(TARGET_CRS).geometry.union_all().buffer(
        CONTEXT_BUFFER_M
    )
    context_wgs84 = gpd.GeoSeries([context_metric], crs=TARGET_CRS).to_crs(
        "EPSG:4326"
    ).iloc[0]
    bbox = tuple(context_wgs84.bounds)

    rivers_raw = gpd.read_file(hydro_source, bbox=bbox, engine="pyogrio")
    glaciers_raw = gpd.read_file(rgi_source, bbox=bbox, engine="pyogrio")
    rivers_clean = clean(rivers_raw)
    glaciers_clean = clean(glaciers_raw)

    context_series = gpd.GeoSeries([context_metric], crs=TARGET_CRS)
    rivers_metric = rivers_clean.to_crs(TARGET_CRS)
    rivers_metric = gpd.clip(rivers_metric, context_series, keep_geom_type=True)
    glaciers_metric = glaciers_clean.to_crs(TARGET_CRS)
    glaciers_metric = glaciers_metric.loc[
        glaciers_metric.geometry.intersects(context_metric)
    ].copy()

    river_columns = {
        "HYRIV_ID": "River Reach ID",
        "NEXT_DOWN": "Next Downstream Reach ID",
        "MAIN_RIV": "Main River ID",
        "LENGTH_KM": "Source Reach Length (km)",
        "CATCH_SKM": "Catchment Area (sq km)",
        "UPLAND_SKM": "Upstream Area (sq km)",
        "DIS_AV_CMS": "Mean Discharge (m3/s)",
        "ORD_STRA": "Strahler Order",
        "HYBAS_L12": "HydroBASINS Level 12 ID",
    }
    rivers = rivers_metric[list(river_columns) + ["geometry"]].rename(
        columns=river_columns
    )
    rivers["Clipped Reach Length (km)"] = rivers.geometry.length / 1000
    rivers["Context Buffer (km)"] = CONTEXT_BUFFER_M / 1000

    glacier_columns = {
        "rgi_id": "RGI Glacier ID",
        "glims_id": "GLIMS Glacier ID",
        "src_date": "Source Date",
        "glac_name": "Glacier Name",
        "area_km2": "Inventory Area (sq km)",
        "zmin_m": "Minimum Elevation (m)",
        "zmax_m": "Maximum Elevation (m)",
        "zmed_m": "Median Elevation (m)",
        "slope_deg": "Mean Slope (degrees)",
        "lmax_m": "Maximum Length (m)",
    }
    glaciers = glaciers_metric[list(glacier_columns) + ["geometry"]].rename(
        columns=glacier_columns
    )
    reference = gpd.read_file(
        root / REFERENCE_RELATIVE, layer="affected_extent"
    ).to_crs(TARGET_CRS)
    reference_geometry = reference.geometry.union_all()
    glaciers["Distance to Preliminary Event Footprint (km)"] = (
        glaciers.geometry.distance(reference_geometry) / 1000
    )
    glaciers["Intersects Preliminary Event Footprint"] = glaciers.geometry.intersects(
        reference_geometry
    )
    glaciers["Context Buffer (km)"] = CONTEXT_BUFFER_M / 1000

    output = root / OUTPUT_RELATIVE
    write_layers(
        output,
        {
            "hydrorivers_context": rivers,
            "rgi7_glaciers_context": glaciers,
        },
    )

    glacier_table = pd.DataFrame(glaciers.drop(columns="geometry")).sort_values(
        ["Distance to Preliminary Event Footprint (km)", "RGI Glacier ID"]
    )
    glacier_table_path = root / GLACIER_TABLE_RELATIVE
    glacier_table_path.parent.mkdir(parents=True, exist_ok=True)
    glacier_table.to_parquet(glacier_table_path, index=False)

    audit_rows = [
        {
            "layer": "hydrorivers_context",
            "source_bbox_candidates": len(rivers_raw),
            "valid_source_features": len(rivers_clean),
            "output_features": len(rivers),
            "output_measure": round(float(rivers.geometry.length.sum() / 1000), 3),
            "output_measure_unit": "km of clipped river reaches",
            "interpretation": "regional hydrographic context; not event observations",
        },
        {
            "layer": "rgi7_glaciers_context",
            "source_bbox_candidates": len(glaciers_raw),
            "valid_source_features": len(glaciers_clean),
            "output_features": len(glaciers),
            "output_measure": round(
                float(glaciers["Inventory Area (sq km)"].sum()), 3
            ),
            "output_measure_unit": "inventory sq km",
            "interpretation": "approximately year-2000 context; not 2026 trigger evidence",
        },
    ]
    audit = root / AUDIT_RELATIVE
    audit.parent.mkdir(parents=True, exist_ok=True)
    with audit.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    print(pd.DataFrame(audit_rows).to_string(index=False))
    print(
        glacier_table[
            [
                "RGI Glacier ID",
                "Glacier Name",
                "Inventory Area (sq km)",
                "Distance to Preliminary Event Footprint (km)",
            ]
        ]
        .head(10)
        .to_string(index=False)
    )
    print(
        {
            "output": str(output),
            "glacier_table": str(glacier_table_path),
            "audit": str(audit),
        }
    )


if __name__ == "__main__":
    main()
