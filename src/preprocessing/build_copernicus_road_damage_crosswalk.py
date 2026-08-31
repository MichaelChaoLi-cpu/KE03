#!/usr/bin/env python3
"""Crosswalk Copernicus EMSR927 road and bridge grades to the routable OSM graph."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import LineString


REFERENCE_RELATIVE = Path(
    "data/processed/geospatial/reference/copernicus_emsr927_damage_reference.gpkg"
)
EDGES_RELATIVE = Path(
    "data/processed/geospatial/network/road_edges_preprocessed.parquet"
)
NODES_RELATIVE = Path(
    "data/processed/geospatial/network/road_nodes_preprocessed.parquet"
)
OUTPUT_RELATIVE = Path(
    "data/processed/geospatial/network/road_damage_evidence_crosswalk.parquet"
)
SPATIAL_OUTPUT_RELATIVE = Path(
    "data/processed/geospatial/network/road_damage_evidence_crosswalk.gpkg"
)
AUDIT_RELATIVE = Path(
    "data/exp/data-preprocessing/copernicus_road_damage_crosswalk_audit.csv"
)
TARGET_CRS = "EPSG:32645"
ROAD_MATCH_TOLERANCE_M = 20
BRIDGE_MATCH_TOLERANCE_M = 100
SEARCH_MARGIN_M = 150
SEVERITY = {
    "Not Analysed": -1,
    "No visible damage": 0,
    "Possibly damaged": 1,
    "Damaged": 2,
    "Destroyed": 3,
}
DISRUPTION_GRADES = {"Possibly damaged", "Damaged", "Destroyed"}


def edge_geometry(
    edges: pd.DataFrame, nodes: pd.DataFrame
) -> gpd.GeoDataFrame:
    coordinates = nodes.set_index("Road node ID")[["Easting (m)", "Northing (m)"]]
    starts = coordinates.reindex(edges["From node ID"]).to_numpy()
    ends = coordinates.reindex(edges["To node ID"]).to_numpy()
    valid = np.isfinite(starts).all(axis=1) & np.isfinite(ends).all(axis=1)
    result = edges.loc[valid].copy()
    geometry = [
        LineString((start, end))
        for start, end in zip(starts[valid], ends[valid], strict=True)
    ]
    return gpd.GeoDataFrame(result, geometry=geometry, crs=TARGET_CRS)


def road_matches(
    graph_edges: gpd.GeoDataFrame, evidence: gpd.GeoDataFrame
) -> pd.DataFrame:
    source = evidence.reset_index(drop=True).copy()
    source["evidence_id"] = source["CEMS Feature ID"]
    source["grade"] = source["Damage Grade"]
    source["aoi"] = source["AOI"]
    source.geometry = source.geometry.buffer(ROAD_MATCH_TOLERANCE_M)
    joined = gpd.sjoin(
        graph_edges,
        source[["evidence_id", "grade", "aoi", "geometry"]],
        how="inner",
        predicate="intersects",
    )
    if joined.empty:
        return pd.DataFrame()
    joined["severity"] = joined["grade"].map(SEVERITY).fillna(-2)
    joined["evidence_type"] = "Copernicus road line"
    joined["match_type"] = f"intersects {ROAD_MATCH_TOLERANCE_M} m evidence buffer"
    joined["match_distance_m"] = 0.0
    return pd.DataFrame(joined.drop(columns="geometry"))


def bridge_matches(
    graph_edges: gpd.GeoDataFrame, evidence: gpd.GeoDataFrame
) -> pd.DataFrame:
    source = evidence.reset_index(drop=True).copy()
    source["evidence_id"] = source["CEMS Feature ID"]
    source["grade"] = source["Damage Grade"]
    source["aoi"] = source["AOI"]
    preferred = graph_edges.loc[graph_edges["Is bridge"]].copy()
    if preferred.empty:
        preferred = graph_edges
    joined = gpd.sjoin_nearest(
        preferred,
        source[["evidence_id", "grade", "aoi", "geometry"]],
        how="inner",
        max_distance=BRIDGE_MATCH_TOLERANCE_M,
        distance_col="match_distance_m",
    )
    if joined.empty:
        return pd.DataFrame()
    # One CEMS bridge point can fall equally close to multiple graph segments of
    # the same mapped bridge. Keep every equally near segment for disruption.
    joined["severity"] = joined["grade"].map(SEVERITY).fillna(-2)
    joined["evidence_type"] = "Copernicus bridge point"
    joined["match_type"] = f"nearest OSM bridge within {BRIDGE_MATCH_TOLERANCE_M} m"
    return pd.DataFrame(joined.drop(columns="geometry"))


def collapse_matches(matches: pd.DataFrame) -> pd.DataFrame:
    if matches.empty:
        return matches
    rows: list[dict[str, object]] = []
    for edge_id, group in matches.groupby("Edge ID", sort=True):
        maximum = int(group["severity"].max())
        strongest = group.loc[group["severity"] == maximum]
        representative = strongest.iloc[0]
        rows.append(
            {
                "Edge ID": int(edge_id),
                "OSM Feature ID": representative["OSM feature ID"],
                "Road Name": representative["Road name"],
                "Road Class": representative["Road class"],
                "Is OSM Bridge": bool(representative["Is bridge"]),
                "CEMS Damage Grade": representative["grade"],
                "Damage Severity Order": maximum,
                "Is Disruption Candidate": representative["grade"]
                in DISRUPTION_GRADES,
                "CEMS Evidence Type": "; ".join(
                    sorted(group["evidence_type"].dropna().unique())
                ),
                "CEMS Feature IDs": ";".join(
                    sorted(group["evidence_id"].dropna().astype(str).unique())
                ),
                "Evidence AOIs": "; ".join(
                    sorted(group["aoi"].dropna().astype(str).unique())
                ),
                "Match Method": "; ".join(
                    sorted(group["match_type"].dropna().unique())
                ),
                "Minimum Match Distance (m)": float(group["match_distance_m"].min()),
                "Evidence Source": "Copernicus EMS Rapid Mapping EMSR927",
                "Evidence Status": "rapid satellite-image damage grading; not field validated",
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    reference_path = root / REFERENCE_RELATIVE
    edges_path = root / EDGES_RELATIVE
    nodes_path = root / NODES_RELATIVE
    for required in (reference_path, edges_path, nodes_path):
        if not required.exists():
            raise FileNotFoundError(required)

    roads = gpd.read_file(reference_path, layer="roads").to_crs(TARGET_CRS)
    bridges = gpd.read_file(reference_path, layer="bridges").to_crs(TARGET_CRS)
    evidence_bounds = np.vstack([roads.total_bounds, bridges.total_bounds])
    minx = float(evidence_bounds[:, 0].min() - SEARCH_MARGIN_M)
    miny = float(evidence_bounds[:, 1].min() - SEARCH_MARGIN_M)
    maxx = float(evidence_bounds[:, 2].max() + SEARCH_MARGIN_M)
    maxy = float(evidence_bounds[:, 3].max() + SEARCH_MARGIN_M)

    nodes = pd.read_parquet(nodes_path)
    candidate_nodes = nodes.loc[
        nodes["Easting (m)"].between(minx, maxx)
        & nodes["Northing (m)"].between(miny, maxy)
    ].copy()
    node_ids = set(candidate_nodes["Road node ID"].astype(int))
    edges = pd.read_parquet(edges_path)
    candidate_edges = edges.loc[
        edges["From node ID"].isin(node_ids) | edges["To node ID"].isin(node_ids)
    ].copy()
    graph = edge_geometry(candidate_edges, nodes)

    road_match_frame = road_matches(graph, roads)
    bridge_match_frame = bridge_matches(graph, bridges)
    available = [frame for frame in (road_match_frame, bridge_match_frame) if not frame.empty]
    if not available:
        raise RuntimeError("No Copernicus road or bridge evidence matched the OSM graph")
    matches = pd.concat(available, ignore_index=True)
    crosswalk = collapse_matches(matches)

    output = root / OUTPUT_RELATIVE
    output.parent.mkdir(parents=True, exist_ok=True)
    crosswalk.to_parquet(output, index=False)

    spatial = graph.loc[
        graph["Edge ID"].isin(crosswalk["Edge ID"]), ["Edge ID", "geometry"]
    ].merge(crosswalk, on="Edge ID", how="inner", validate="one_to_one")
    for column in spatial.columns:
        if column == "geometry":
            continue
        if isinstance(spatial[column].dtype, pd.CategoricalDtype) or str(
            spatial[column].dtype
        ) == "str":
            spatial[column] = spatial[column].astype(object)
    spatial_output = root / SPATIAL_OUTPUT_RELATIVE
    if spatial_output.exists():
        spatial_output.unlink()
    spatial.to_file(
        spatial_output,
        layer="road_damage_crosswalk",
        driver="GPKG",
        engine="pyogrio",
    )

    matched_evidence_ids = set(matches["evidence_id"].astype(str))
    matched_road_ids = (
        set(road_match_frame["evidence_id"].astype(str))
        if not road_match_frame.empty
        else set()
    )
    matched_bridge_ids = (
        set(bridge_match_frame["evidence_id"].astype(str))
        if not bridge_match_frame.empty
        else set()
    )
    audit_rows = [
        {
            "measure": "candidate_osm_nodes",
            "value": len(candidate_nodes),
            "note": "nodes inside the EMSR927 evidence bounding box plus search margin",
        },
        {
            "measure": "candidate_osm_edges",
            "value": len(graph),
            "note": "edges reconstructed for local spatial matching",
        },
        {
            "measure": "cems_road_features",
            "value": len(roads),
            "note": "all current road grades, including no visible damage and not analysed",
        },
        {
            "measure": "cems_bridge_features",
            "value": len(bridges),
            "note": "current Copernicus bridge points",
        },
        {
            "measure": "matched_cems_road_features",
            "value": len(matched_road_ids),
            "note": "road evidence features linked within the 20 m tolerance",
        },
        {
            "measure": "unmatched_cems_road_features",
            "value": len(roads) - len(matched_road_ids),
            "note": "retain for manual review; not forced onto the graph",
        },
        {
            "measure": "matched_cems_bridge_features",
            "value": len(matched_bridge_ids),
            "note": "bridge evidence points linked to OSM bridge edges within 100 m",
        },
        {
            "measure": "unmatched_cems_bridge_features",
            "value": len(bridges) - len(matched_bridge_ids),
            "note": "retain for manual review; not forced onto the graph",
        },
        {
            "measure": "matched_cems_evidence_features",
            "value": len(matched_evidence_ids),
            "note": "unique road or bridge evidence features linked to at least one graph edge",
        },
        {
            "measure": "matched_osm_edges",
            "value": len(crosswalk),
            "note": "graph edges carrying a Copernicus evidence grade",
        },
        {
            "measure": "disruption_candidate_osm_edges",
            "value": int(crosswalk["Is Disruption Candidate"].sum()),
            "note": "possibly damaged, damaged, or destroyed grades",
        },
    ]
    audit = root / AUDIT_RELATIVE
    audit.parent.mkdir(parents=True, exist_ok=True)
    with audit.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    print(pd.DataFrame(audit_rows).to_string(index=False))
    print(crosswalk["CEMS Damage Grade"].value_counts().to_string())
    print(
        {
            "crosswalk": str(output),
            "spatial_crosswalk": str(spatial_output),
            "audit": str(audit),
        }
    )


if __name__ == "__main__":
    main()
