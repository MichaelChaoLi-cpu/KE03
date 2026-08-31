#!/usr/bin/env python3
"""Create a compact event-source reference from the archived Hi-RISK report."""

from __future__ import annotations

import argparse
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point


REPORT_RELATIVE = Path(
    "data/raw/geospatial/reference/hirisk_2026_rasuwa/"
    "RHA_NP3_RasuwaFlood-1.pdf"
)
OUTPUT_GPKG_RELATIVE = Path(
    "data/processed/geospatial/reference/event_mechanism_reference.gpkg"
)
OUTPUT_TABLE_RELATIVE = Path(
    "data/processed/geospatial/reference/event_mechanism_reference.parquet"
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    report = root / REPORT_RELATIVE
    if not report.exists():
        raise FileNotFoundError(report)

    record = {
        "Event ID": "nepal_rasuwa_2026_08_26",
        "Event Date": "2026-08-26",
        "Report Date": "2026-08-28",
        "Source Latitude": 28.288708,
        "Source Longitude": 85.528159,
        "Reported Event Type": "rock-ice avalanche and downstream flood",
        "Proposed Sequence": (
            "glacier and bedrock detachment; possible brief valley blockage; "
            "downstream flood"
        ),
        "Referenced RGI Glacier ID": "RGI2000-v7.0-G-15-05732",
        "Evidence Class": "rapid remote-sensing assessment",
        "Field Validated": False,
        "Supports Climate Attribution": False,
        "Source Document": str(REPORT_RELATIVE),
    }
    table = pd.DataFrame([record])
    table_path = root / OUTPUT_TABLE_RELATIVE
    table_path.parent.mkdir(parents=True, exist_ok=True)
    table.to_parquet(table_path, index=False)

    spatial = gpd.GeoDataFrame(
        table,
        geometry=[Point(record["Source Longitude"], record["Source Latitude"])],
        crs="EPSG:4326",
    )
    gpkg_path = root / OUTPUT_GPKG_RELATIVE
    if gpkg_path.exists():
        gpkg_path.unlink()
    spatial.to_file(
        gpkg_path,
        layer="reported_source_point",
        driver="GPKG",
        engine="pyogrio",
    )
    print(table.to_string(index=False))
    print({"table": str(table_path), "geopackage": str(gpkg_path)})


if __name__ == "__main__":
    main()
