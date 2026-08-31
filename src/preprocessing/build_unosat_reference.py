#!/usr/bin/env python3
"""Validate UNOSAT event polygons and build reproducible exposure overlays."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import geopandas as gpd


TARGET_CRS = "EPSG:32645"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    raw_dir = root / "data/raw/geospatial/reference/unosat_2026-08-26/extracted"
    affected_path = raw_dir / "FloodExtent_20260826_Nepal.shp"
    analysis_path = raw_dir / "UNOSAT_Analysis_extent_20260826_20260827.shp"
    output = root / "data/processed/geospatial/reference/unosat_event_reference.gpkg"
    table_dir = root / "data/exp/data-briefing/tables"

    affected = gpd.read_file(affected_path).to_crs(TARGET_CRS)
    analysis = gpd.read_file(analysis_path).to_crs(TARGET_CRS)
    for name, frame in (("affected_extent", affected), ("analysis_extent", analysis)):
        if frame.empty or frame.geometry.isna().any() or not frame.geometry.is_valid.all():
            raise RuntimeError(f"UNOSAT {name} failed geometry validation")

    affected = affected[["geometry"]].copy()
    affected["source"] = "UNOSAT"
    affected["event_date"] = "2026-08-26"
    affected["status"] = "preliminary_not_field_validated"
    affected["area_km2"] = affected.geometry.area / 1_000_000
    analysis = analysis[["geometry"]].copy()
    analysis["source"] = "UNOSAT"
    analysis["imagery_dates"] = "2026-08-26;2026-08-27"
    analysis["area_km2"] = analysis.geometry.area / 1_000_000

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    affected.to_file(output, layer="affected_extent", driver="GPKG")
    analysis.to_file(output, layer="analysis_extent", driver="GPKG", mode="a")

    inventory_rows = [
        {
            "layer": "affected_extent",
            "features": len(affected),
            "crs": TARGET_CRS,
            "valid_geometries": int(affected.geometry.is_valid.sum()),
            "area_km2": round(float(affected.geometry.area.sum() / 1_000_000), 6),
            "source_geometry": str(affected_path.relative_to(root)),
            "output": str(output.relative_to(root)),
        },
        {
            "layer": "analysis_extent",
            "features": len(analysis),
            "crs": TARGET_CRS,
            "valid_geometries": int(analysis.geometry.is_valid.sum()),
            "area_km2": round(float(analysis.geometry.area.sum() / 1_000_000), 6),
            "source_geometry": str(analysis_path.relative_to(root)),
            "output": str(output.relative_to(root)),
        },
    ]
    write_csv(table_dir / "unosat_reference_inventory.csv", inventory_rows)

    hazard = affected.geometry.union_all()
    admin_dir = root / "data/raw/geospatial/base/admin/npl_admin_boundaries_2024"
    admin_rows: list[dict[str, object]] = []
    for layer, source_name, code, name in (
        ("districts", "npl_admin2.shp", "adm2_pcode", "adm2_name"),
        ("local_units", "npl_admin3.shp", "adm3_pcode", "adm3_name"),
    ):
        frame = gpd.read_file(admin_dir / source_name).to_crs(TARGET_CRS)
        frame["affected_area_km2"] = frame.geometry.intersection(hazard).area / 1_000_000
        frame["unit_area_km2"] = frame.geometry.area / 1_000_000
        frame["affected_share_percent"] = 100 * frame["affected_area_km2"] / frame["unit_area_km2"]
        for row in frame.loc[frame["affected_area_km2"] > 0].itertuples():
            admin_rows.append(
                {
                    "admin_level": layer,
                    "pcode": getattr(row, code),
                    "name": getattr(row, name),
                    "affected_area_km2": round(float(row.affected_area_km2), 6),
                    "unit_area_km2": round(float(row.unit_area_km2), 6),
                    "affected_share_percent": round(float(row.affected_share_percent), 4),
                }
            )
    admin_rows.sort(key=lambda row: (str(row["admin_level"]), -float(row["affected_area_km2"])))
    write_csv(table_dir / "unosat_admin_affected_area.csv", admin_rows)

    osm_path = root / "data/processed/geospatial/base/osm_pre_event_aoi.gpkg"
    exposure_rows: list[dict[str, object]] = []
    for layer in ("roads", "bridges", "waterways", "settlements", "facilities", "buildings"):
        frame = gpd.read_file(osm_path, layer=layer).to_crs(TARGET_CRS)
        intersects = frame.geometry.intersects(hazard)
        selected = frame.loc[intersects]
        metric = "feature_count"
        value = len(selected)
        if layer in ("roads", "waterways"):
            metric = "intersecting_length_km"
            value = selected.geometry.intersection(hazard).length.sum() / 1_000
        exposure_rows.append(
            {
                "layer": layer,
                "all_aoi_features": len(frame),
                "intersecting_features": len(selected),
                "metric": metric,
                "metric_value": round(float(value), 6),
                "interpretation": "screening overlap; not confirmed damage",
            }
        )
    write_csv(table_dir / "unosat_osm_exposure_screening.csv", exposure_rows)
    print(
        {
            "output": str(output),
            "affected_area_km2": round(float(affected.geometry.area.sum() / 1_000_000), 3),
            "analysis_area_km2": round(float(analysis.geometry.area.sum() / 1_000_000), 3),
            "admin_units_intersected": len(admin_rows),
        }
    )


if __name__ == "__main__":
    main()
