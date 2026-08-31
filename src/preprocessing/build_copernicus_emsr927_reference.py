#!/usr/bin/env python3
"""Consolidate current Copernicus EMSR927 damage-grading vectors."""

from __future__ import annotations

import argparse
import csv
import tempfile
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import geopandas as gpd
import pandas as pd
import pyogrio
from shapely import force_2d


ARCHIVE_RELATIVE = Path(
    "data/raw/geospatial/reference/copernicus_emsr927/EMSR927_products.zip"
)
OUTPUT_RELATIVE = Path(
    "data/processed/geospatial/reference/copernicus_emsr927_damage_reference.gpkg"
)
SUMMARY_RELATIVE = Path(
    "data/processed/geospatial/reference/copernicus_emsr927_damage_summary.parquet"
)
REVISION_AUDIT_RELATIVE = Path(
    "data/exp/data-preprocessing/copernicus_emsr927_revision_audit.csv"
)
TARGET_CRS = "EPSG:32645"

PRODUCTS = (
    {
        "archive": "EMSR927_AOI01_GRA_PRODUCT_v1.zip",
        "aoi": "Syapru Besi",
        "aoi_number": 1,
        "product": "Grading",
        "version": 1,
        "monitoring_update": 0,
        "current": True,
    },
    {
        "archive": "EMSR927_AOI02_GRA_PRODUCT_v2.zip",
        "aoi": "Timure",
        "aoi_number": 2,
        "product": "Grading",
        "version": 2,
        "monitoring_update": 0,
        "current": True,
    },
    {
        "archive": "EMSR927_AOI03_GRA_PRODUCT_v1.zip",
        "aoi": "Bidur",
        "aoi_number": 3,
        "product": "Grading",
        "version": 1,
        "monitoring_update": 0,
        "current": False,
    },
    {
        "archive": "EMSR927_AOI03_GRA_MONIT01_v1.zip",
        "aoi": "Bidur",
        "aoi_number": 3,
        "product": "Grading Monitoring",
        "version": 1,
        "monitoring_update": 1,
        "current": True,
    },
)

LAYER_PATTERNS = {
    "area_of_interest": "areaOfInterestA",
    "buildings": "builtUpP",
    "facilities_area": "facilitiesA",
    "facilities_line": "facilitiesL",
    "observed_event": "observedEventA",
    "transportation_area": "transportationA",
    "roads": "transportationL",
    "bridges": "transportationP",
}

COMMON_RENAMES = {
    "obj_type": "Object Type",
    "name": "Feature Name",
    "info": "Feature Information",
    "simplified": "Feature Class",
    "damage_gra": "Damage Grade",
    "det_method": "Detection Method",
    "notation": "Notation",
    "or_src_id": "Original Source ID",
    "dmg_src_id": "Damage Source ID",
    "cd_value": "Copernicus Value",
    "event_type": "Event Type",
    "obj_desc": "Object Description",
    "area": "Source Reported Area (ha)",
    "emsr_id": "Activation ID",
    "glide_no": "GLIDE Number",
    "area_id": "Area ID",
    "locality": "Locality",
    "map_type": "Map Type",
}


def clean(frame: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    result = frame.loc[frame.geometry.notna()].copy()
    result.geometry = force_2d(result.geometry.array)
    return result.loc[result.geometry.is_valid & ~result.geometry.is_empty].copy()


def read_product(
    outer: ZipFile, product: dict[str, object], temporary: Path
) -> dict[str, gpd.GeoDataFrame]:
    # AOI01 is duplicated byte-for-byte in the official outer bundle. ZipFile
    # resolves the final matching member; the acquisition audit records the duplicate.
    payload = outer.read(str(product["archive"]))
    with ZipFile(BytesIO(payload)) as inner:
        gpkg_names = [name for name in inner.namelist() if name.casefold().endswith(".gpkg")]
        if len(gpkg_names) != 1:
            raise RuntimeError(
                f"Expected one GeoPackage in {product['archive']}, got {gpkg_names}"
            )
        gpkg_path = temporary / Path(gpkg_names[0]).name
        gpkg_path.write_bytes(inner.read(gpkg_names[0]))

    available = {name: geometry for name, geometry in pyogrio.list_layers(gpkg_path)}
    result: dict[str, gpd.GeoDataFrame] = {}
    for group, pattern in LAYER_PATTERNS.items():
        matches = [name for name in available if pattern.casefold() in name.casefold()]
        if not matches:
            continue
        if len(matches) != 1:
            raise RuntimeError(f"Ambiguous {pattern} layers in {gpkg_path}: {matches}")
        frame = clean(gpd.read_file(gpkg_path, layer=matches[0], engine="pyogrio"))
        frame = frame.rename(columns=COMMON_RENAMES)
        keep = [column for column in COMMON_RENAMES.values() if column in frame.columns]
        frame = frame[keep + ["geometry"]].copy()
        frame["AOI"] = product["aoi"]
        frame["AOI Number"] = product["aoi_number"]
        frame["Product"] = product["product"]
        frame["Product Version"] = product["version"]
        frame["Monitoring Update"] = product["monitoring_update"]
        frame["Is Current Product"] = product["current"]
        frame["Source Product Archive"] = product["archive"]
        result[group] = frame
    return result


def concatenate(frames: list[gpd.GeoDataFrame]) -> gpd.GeoDataFrame:
    if not frames:
        raise RuntimeError("Cannot concatenate an empty geospatial layer")
    crs = frames[0].crs
    return gpd.GeoDataFrame(pd.concat(frames, ignore_index=True), crs=crs).to_crs(
        TARGET_CRS
    )


def write_layers(path: Path, layers: dict[str, gpd.GeoDataFrame]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    first = True
    for name, frame in layers.items():
        frame.to_file(
            path,
            layer=name,
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
    archive_path = root / ARCHIVE_RELATIVE
    if not archive_path.exists():
        raise FileNotFoundError(archive_path)

    grouped_all: dict[str, list[gpd.GeoDataFrame]] = {
        group: [] for group in LAYER_PATTERNS
    }
    audit_rows: list[dict[str, object]] = []
    with ZipFile(archive_path) as outer, tempfile.TemporaryDirectory(
        prefix="ke03-emsr927-"
    ) as temporary_name:
        temporary = Path(temporary_name)
        for product in PRODUCTS:
            layers = read_product(outer, product, temporary)
            for group, frame in layers.items():
                grouped_all[group].append(frame)
                if "Damage Grade" in frame.columns:
                    counts = frame["Damage Grade"].fillna("Missing").value_counts()
                    for grade, count in counts.items():
                        audit_rows.append(
                            {
                                "aoi": product["aoi"],
                                "aoi_number": product["aoi_number"],
                                "product": product["product"],
                                "monitoring_update": product["monitoring_update"],
                                "is_current_product": product["current"],
                                "feature_group": group,
                                "damage_grade": grade,
                                "feature_count": int(count),
                            }
                        )
                else:
                    audit_rows.append(
                        {
                            "aoi": product["aoi"],
                            "aoi_number": product["aoi_number"],
                            "product": product["product"],
                            "monitoring_update": product["monitoring_update"],
                            "is_current_product": product["current"],
                            "feature_group": group,
                            "damage_grade": "Not applicable",
                            "feature_count": len(frame),
                        }
                    )

    current_layers: dict[str, gpd.GeoDataFrame] = {}
    for group, frames in grouped_all.items():
        current_frames = [frame.loc[frame["Is Current Product"]].copy() for frame in frames]
        current_frames = [frame for frame in current_frames if not frame.empty]
        if not current_frames:
            continue
        current = concatenate(current_frames)
        current["CEMS Feature ID"] = [
            f"EMSR927-{group}-{index + 1:06d}" for index in range(len(current))
        ]
        if group in {"roads", "facilities_line"}:
            current["Mapped Length (m)"] = current.geometry.length
        if group in {
            "observed_event",
            "facilities_area",
            "transportation_area",
            "area_of_interest",
        }:
            current["Mapped Area (sq m)"] = current.geometry.area
        current_layers[group] = current

    output = root / OUTPUT_RELATIVE
    write_layers(output, current_layers)

    summary_rows: list[dict[str, object]] = []
    for group, frame in current_layers.items():
        if "Damage Grade" in frame.columns:
            combinations = frame.groupby(["AOI", "Damage Grade"], dropna=False)
            for (aoi, grade), subset in combinations:
                summary_rows.append(
                    {
                        "Feature Group": group,
                        "AOI": aoi,
                        "Damage Grade": grade,
                        "Feature Count": len(subset),
                        "Mapped Length (km)": (
                            float(subset.geometry.length.sum() / 1000)
                            if group in {"roads", "facilities_line"}
                            else pd.NA
                        ),
                        "Mapped Area (ha)": (
                            float(subset.geometry.area.sum() / 10_000)
                            if group
                            in {"facilities_area", "transportation_area"}
                            else pd.NA
                        ),
                    }
                )
        elif group == "observed_event":
            for aoi, subset in frame.groupby("AOI"):
                summary_rows.append(
                    {
                        "Feature Group": group,
                        "AOI": aoi,
                        "Damage Grade": "Observed event area",
                        "Feature Count": len(subset),
                        "Mapped Length (km)": pd.NA,
                        "Mapped Area (ha)": float(subset.geometry.area.sum() / 10_000),
                    }
                )
    summary = pd.DataFrame(summary_rows)
    summary_path = root / SUMMARY_RELATIVE
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_parquet(summary_path, index=False)

    audit_path = root / REVISION_AUDIT_RELATIVE
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    with audit_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    print(
        pd.DataFrame(
            [
                {
                    "layer": group,
                    "features": len(frame),
                    "damage_grades": (
                        ";".join(sorted(frame["Damage Grade"].dropna().unique()))
                        if "Damage Grade" in frame.columns
                        else "not applicable"
                    ),
                }
                for group, frame in current_layers.items()
            ]
        ).to_string(index=False)
    )
    print(
        {
            "output": str(output),
            "summary": str(summary_path),
            "revision_audit": str(audit_path),
        }
    )


if __name__ == "__main__":
    main()
