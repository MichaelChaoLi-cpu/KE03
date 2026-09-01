#!/usr/bin/env python3
"""Build an operational crosswalk for priority settlements and road sections."""

from __future__ import annotations

import argparse
from pathlib import Path

import geopandas as gpd
import pandas as pd


SETTLEMENTS = Path(
    "data/processed/decision/settlement_intervention_priority_preprocessed.parquet"
)
ROADS = Path(
    "data/processed/decision/road_repair_candidate_benefits_preprocessed.parquet"
)
ROAD_GEOMETRY = Path(
    "data/processed/decision/road_repair_candidate_benefits.gpkg"
)
ADMIN = Path("data/processed/geospatial/base/event_area_admin.gpkg")
PROCESSED_OUTPUT = Path(
    "data/processed/decision/priority_object_operational_crosswalk_preprocessed.parquet"
)
SUPPLEMENTARY_OUTPUT = Path(
    "data/results/supplementary/priority_object_operational_crosswalk.csv"
)
AUDIT_OUTPUT = Path(
    "data/exp/data-preprocessing/priority_object_operational_crosswalk_audit.csv"
)


def spatial_admin_context(
    points: gpd.GeoDataFrame,
    admin_path: Path,
) -> pd.DataFrame:
    """Attach local-unit and district names to point geometries."""
    result = points[["Road Repair Candidate ID", "geometry"]].copy()
    for layer, output_name in (("local_units", "Local Unit"), ("districts", "District")):
        areas = gpd.read_file(admin_path, layer=layer).to_crs(points.crs)
        name_candidates = [
            column
            for column in areas.columns
            if column != "geometry" and "name" in column.lower()
        ]
        if not name_candidates:
            raise ValueError(f"No readable name field in {admin_path}:{layer}")
        joined = gpd.sjoin(
            result[["Road Repair Candidate ID", "geometry"]],
            areas[[name_candidates[0], "geometry"]],
            how="left",
            predicate="within",
        )
        lookup = (
            joined.drop_duplicates("Road Repair Candidate ID")
            .set_index("Road Repair Candidate ID")[name_candidates[0]]
        )
        result[output_name] = result["Road Repair Candidate ID"].map(lookup)
    return pd.DataFrame(result.drop(columns="geometry"))


def build_crosswalk(root: Path) -> pd.DataFrame:
    settlements = pd.read_parquet(root / SETTLEMENTS)
    settlements = settlements.loc[
        settlements["Primary Scenario"].astype(bool)
        & settlements["Priority Rank"].le(10)
    ].copy()
    settlements["Name Verification Status"] = settlements[
        "Settlement Name (English Preferred)"
    ].where(
        ~settlements["Settlement Name (English Preferred)"].str.startswith(
            "OSM Settlement", na=True
        ),
        "",
    ).map(lambda value: "OSM name available" if value else "Unnamed in OSM")
    settlements["Display Label"] = settlements.apply(
        lambda row: row["Settlement Name (English Preferred)"]
        if row["Name Verification Status"] == "OSM name available"
        else f"Unnamed settlement (OSM {row['OSM Settlement ID']})",
        axis=1,
    )
    settlement_rows = pd.DataFrame(
        {
            "Object Type": "Priority settlement",
            "Stable OSM ID": settlements["OSM Settlement ID"].astype(str),
            "Display Label": settlements["Display Label"],
            "Name Verification Status": settlements["Name Verification Status"],
            "Longitude": settlements["Settlement Longitude"],
            "Latitude": settlements["Settlement Latitude"],
            "Local Unit": settlements["Local Unit"],
            "District": settlements["District"],
            "Priority Rank": settlements["Priority Rank"].astype(int),
            "Operational Use": "Settlement verification and response prioritization",
        }
    )

    roads = pd.read_parquet(root / ROADS)
    roads = roads.loc[roads["Is Critical Road Section"].astype(bool)].copy()
    road_geometry = gpd.read_file(root / ROAD_GEOMETRY)
    road_geometry = road_geometry.loc[
        road_geometry["Road Repair Candidate ID"].isin(roads["Road Repair Candidate ID"])
    ].copy()
    centroids = road_geometry.to_crs(32645)
    centroids.geometry = centroids.geometry.centroid
    admin = spatial_admin_context(centroids, root / ADMIN)
    coordinates = centroids.to_crs(4326)
    coordinates["Longitude"] = coordinates.geometry.x
    coordinates["Latitude"] = coordinates.geometry.y
    roads = roads.merge(
        coordinates[["Road Repair Candidate ID", "Longitude", "Latitude"]],
        on="Road Repair Candidate ID",
        how="left",
        validate="one_to_one",
    ).merge(
        admin,
        on="Road Repair Candidate ID",
        how="left",
        validate="one_to_one",
    )
    roads["Name Verification Status"] = roads["Road Name"].map(
        lambda value: "OSM name available" if pd.notna(value) and str(value).strip()
        else "Unnamed in OSM"
    )
    road_rows = pd.DataFrame(
        {
            "Object Type": "Critical road section",
            "Stable OSM ID": roads["OSM Feature ID"].astype(str),
            "Display Label": roads["Critical Road Section"],
            "Name Verification Status": roads["Name Verification Status"],
            "Longitude": roads["Longitude"],
            "Latitude": roads["Latitude"],
            "Local Unit": roads["Local Unit"],
            "District": roads["District"],
            "Priority Rank": roads["Primary Repair Benefit Rank"].astype(int),
            "Operational Use": "Road-section field verification and repair screening",
        }
    )

    crosswalk = pd.concat([settlement_rows, road_rows], ignore_index=True)
    crosswalk = crosswalk.sort_values(
        ["Object Type", "Priority Rank"], kind="stable"
    ).reset_index(drop=True)
    if crosswalk["Stable OSM ID"].duplicated().any():
        raise ValueError("Stable OSM IDs must be unique within the operational crosswalk")
    if crosswalk[["Longitude", "Latitude"]].isna().any().any():
        raise ValueError("Every priority object must have operational coordinates")
    return crosswalk


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    for path in (SETTLEMENTS, ROADS, ROAD_GEOMETRY, ADMIN):
        if not (root / path).exists():
            raise FileNotFoundError(root / path)

    crosswalk = build_crosswalk(root)
    for output in (PROCESSED_OUTPUT, SUPPLEMENTARY_OUTPUT, AUDIT_OUTPUT):
        (root / output).parent.mkdir(parents=True, exist_ok=True)
    crosswalk.to_parquet(root / PROCESSED_OUTPUT, index=False)
    crosswalk.to_csv(root / SUPPLEMENTARY_OUTPUT, index=False)

    audit = pd.DataFrame(
        [
            {"Audit Check": "Priority objects", "Value": len(crosswalk)},
            {
                "Audit Check": "Named objects",
                "Value": int(crosswalk["Name Verification Status"].eq("OSM name available").sum()),
            },
            {
                "Audit Check": "Objects unnamed in OSM",
                "Value": int(crosswalk["Name Verification Status"].eq("Unnamed in OSM").sum()),
            },
            {
                "Audit Check": "Objects missing coordinates",
                "Value": int(crosswalk[["Longitude", "Latitude"]].isna().any(axis=1).sum()),
            },
        ]
    )
    audit.to_csv(root / AUDIT_OUTPUT, index=False)
    print(
        f"Wrote {len(crosswalk)} operational crosswalk rows to "
        f"{root / SUPPLEMENTARY_OUTPUT}"
    )


if __name__ == "__main__":
    main()
