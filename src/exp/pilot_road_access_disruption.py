#!/usr/bin/env python3
"""Pilot road-disruption accessibility screening for the Rasuwa event corridor."""

from __future__ import annotations

import argparse
import csv
import heapq
import math
import os
from collections import defaultdict
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/ke03-matplotlib")

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter
from shapely import STRtree, points
from shapely.geometry import LineString
from shapely.prepared import prep


CRS = "EPSG:32645"
MAX_SNAP_M = 3_000
ROAD_SPEED_KMH = {
    "trunk": 60,
    "trunk_link": 40,
    "primary": 50,
    "primary_link": 35,
    "secondary": 40,
    "secondary_link": 30,
    "tertiary": 30,
    "tertiary_link": 25,
    "residential": 20,
    "living_street": 15,
    "unclassified": 20,
    "service": 15,
    "road": 15,
    "track": 10,
}
ROAD_PRIORITY = {
    "trunk": 1,
    "trunk_link": 1,
    "primary": 2,
    "primary_link": 2,
    "secondary": 3,
    "secondary_link": 3,
    "tertiary": 4,
    "tertiary_link": 4,
    "residential": 5,
    "unclassified": 6,
    "service": 7,
    "living_street": 7,
    "road": 7,
    "track": 8,
}


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def dijkstra(adjacency: list[list[tuple[int, float]]], sources: set[int]) -> np.ndarray:
    distances = np.full(len(adjacency), np.inf, dtype="float64")
    queue: list[tuple[float, int]] = []
    for source in sources:
        distances[source] = 0.0
        heapq.heappush(queue, (0.0, source))
    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbour, cost in adjacency[node]:
            candidate = distance + cost
            if candidate < distances[neighbour]:
                distances[neighbour] = candidate
                heapq.heappush(queue, (candidate, neighbour))
    return distances


def clean_value(value: object) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return ""
    return str(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    table_dir = root / "data/exp/data-briefing/tables"
    figure_dir = root / "data/exp/data-briefing/figures/geospatial"

    osm_path = root / "data/processed/geospatial/base/osm_pre_event_aoi.gpkg"
    reference_path = root / "data/processed/geospatial/reference/unosat_event_reference.gpkg"
    roads = gpd.read_file(osm_path, layer="roads").to_crs(CRS)
    settlements = gpd.read_file(osm_path, layer="settlements").to_crs(CRS)
    facilities = gpd.read_file(osm_path, layer="facilities").to_crs(CRS)
    affected = gpd.read_file(reference_path, layer="affected_extent").to_crs(CRS)
    analysis = gpd.read_file(reference_path, layer="analysis_extent").to_crs(CRS)
    hazard = affected.geometry.union_all()
    prepared_hazard = prep(hazard)

    motor_roads = roads.loc[roads["highway"].isin(ROAD_SPEED_KMH)].copy()
    node_lookup: dict[tuple[float, float], int] = {}
    node_coords: list[tuple[float, float]] = []
    edges: list[tuple[int, int, float, bool]] = []
    disrupted_features: dict[str, dict[str, object]] = {}

    def node_id(coordinate: tuple[float, float]) -> int:
        key = (round(float(coordinate[0]), 3), round(float(coordinate[1]), 3))
        existing = node_lookup.get(key)
        if existing is not None:
            return existing
        identifier = len(node_coords)
        node_lookup[key] = identifier
        node_coords.append(key)
        return identifier

    for road in motor_roads.itertuples():
        coordinates = list(road.geometry.coords)
        highway = str(road.highway)
        speed = ROAD_SPEED_KMH[highway]
        osm_id = clean_value(road.osm_id)
        for start, end in zip(coordinates[:-1], coordinates[1:]):
            segment = LineString((start, end))
            length_m = segment.length
            if length_m <= 0:
                continue
            disrupted = prepared_hazard.intersects(segment)
            u, v = node_id(start), node_id(end)
            minutes = length_m / (speed * 1_000 / 60)
            edges.append((u, v, minutes, disrupted))
            if disrupted:
                record = disrupted_features.setdefault(
                    osm_id,
                    {
                        "osm_id": osm_id,
                        "name": clean_value(road.name),
                        "highway": highway,
                        "is_bridge": bool(road.is_bridge),
                        "intersecting_length_m": 0.0,
                        "segment_count": 0,
                    },
                )
                record["intersecting_length_m"] = float(record["intersecting_length_m"]) + length_m
                record["segment_count"] = int(record["segment_count"]) + 1

    baseline_adjacency: list[list[tuple[int, float]]] = [[] for _ in node_coords]
    disrupted_adjacency: list[list[tuple[int, float]]] = [[] for _ in node_coords]
    disrupted_edge_count = 0
    for u, v, minutes, disrupted in edges:
        baseline_adjacency[u].append((v, minutes))
        baseline_adjacency[v].append((u, minutes))
        if disrupted:
            disrupted_edge_count += 1
        else:
            disrupted_adjacency[u].append((v, minutes))
            disrupted_adjacency[v].append((u, minutes))

    node_array = np.asarray(node_coords)
    node_geometries = points(node_array[:, 0], node_array[:, 1])
    node_tree = STRtree(node_geometries)

    targets = facilities.loc[
        facilities["facility_category"].isin(["health", "emergency"])
    ].copy()
    all_sources: set[int] = set()
    conservative_sources: set[int] = set()
    target_snap_distances: list[float] = []
    target_in_hazard = 0
    for target in targets.itertuples():
        nearest = int(node_tree.nearest(target.geometry))
        snap_distance = target.geometry.distance(node_geometries[nearest])
        target_snap_distances.append(float(snap_distance))
        if snap_distance <= MAX_SNAP_M:
            all_sources.add(nearest)
            if prepared_hazard.intersects(target.geometry):
                target_in_hazard += 1
            else:
                conservative_sources.add(nearest)

    baseline_distance = dijkstra(baseline_adjacency, all_sources)
    road_only_distance = dijkstra(disrupted_adjacency, all_sources)
    conservative_distance = dijkstra(disrupted_adjacency, conservative_sources)

    settlement_rows: list[dict[str, object]] = []
    status_geometries = []
    for settlement in settlements.itertuples():
        nearest = int(node_tree.nearest(settlement.geometry))
        snap_distance = float(settlement.geometry.distance(node_geometries[nearest]))
        on_network = snap_distance <= MAX_SNAP_M
        baseline = float(baseline_distance[nearest]) if on_network else math.inf
        road_only = float(road_only_distance[nearest]) if on_network else math.inf
        conservative = float(conservative_distance[nearest]) if on_network else math.inf
        baseline_reachable = math.isfinite(baseline)
        road_isolated = baseline_reachable and not math.isfinite(road_only)
        conservative_isolated = baseline_reachable and not math.isfinite(conservative)
        if not on_network:
            status = "off_network"
        elif not baseline_reachable:
            status = "baseline_unreachable"
        elif conservative_isolated:
            status = "isolated_conservative"
        elif conservative > baseline + 5:
            status = "delay_over_5min"
        else:
            status = "limited_change"
        settlement_rows.append(
            {
                "osm_id": clean_value(settlement.osm_id),
                "name": clean_value(settlement.name),
                "place": clean_value(settlement.place),
                "longitude": round(float(settlement.geometry.to_crs(4326).x), 7)
                if hasattr(settlement.geometry, "to_crs")
                else "",
                "snap_distance_m": round(snap_distance, 2),
                "inside_unosat_extent": prepared_hazard.intersects(settlement.geometry),
                "baseline_minutes": round(baseline, 2) if baseline_reachable else "",
                "road_only_minutes": round(road_only, 2) if math.isfinite(road_only) else "",
                "conservative_minutes": round(conservative, 2) if math.isfinite(conservative) else "",
                "road_only_delay_minutes": round(road_only - baseline, 2)
                if math.isfinite(road_only) and baseline_reachable
                else "",
                "conservative_delay_minutes": round(conservative - baseline, 2)
                if math.isfinite(conservative) and baseline_reachable
                else "",
                "road_only_isolated": road_isolated,
                "conservative_isolated": conservative_isolated,
                "pilot_status": status,
            }
        )
        status_geometries.append(settlement.geometry)

    settlement_output = gpd.GeoDataFrame(
        settlement_rows, geometry=status_geometries, crs=CRS
    )
    csv_rows = settlement_output.drop(columns="geometry").to_dict("records")
    # Replace the placeholder coordinate with a reproducible WGS84 longitude/latitude pair.
    wgs84 = settlement_output.to_crs(4326)
    for row, geometry in zip(csv_rows, wgs84.geometry):
        row["longitude"] = round(float(geometry.x), 7)
        row["latitude"] = round(float(geometry.y), 7)
    write_rows(table_dir / "pilot_settlement_accessibility.csv", csv_rows)

    sensitivity_rows: list[dict[str, object]] = []
    for threshold in (500, 1_000, 2_000, 3_000):
        eligible = [
            row
            for row in settlement_rows
            if float(row["snap_distance_m"]) <= threshold and row["baseline_minutes"] != ""
        ]
        isolated = sum(bool(row["conservative_isolated"]) for row in eligible)
        sensitivity_rows.append(
            {
                "maximum_snap_distance_m": threshold,
                "baseline_reachable_settlements": len(eligible),
                "baseline_reachable_share": round(len(eligible) / len(settlements), 6),
                "conservative_isolated_settlements": isolated,
                "isolated_share_of_baseline_reachable": round(isolated / len(eligible), 6)
                if eligible
                else "",
            }
        )
    write_rows(table_dir / "pilot_snap_threshold_sensitivity.csv", sensitivity_rows)

    critical_rows: list[dict[str, object]] = []
    for record in disrupted_features.values():
        length_km = float(record.pop("intersecting_length_m")) / 1_000
        highway = str(record["highway"])
        critical_rows.append(
            {
                **record,
                "intersecting_length_km": round(length_km, 6),
                "road_hierarchy_rank": ROAD_PRIORITY[highway],
                "candidate_score": round(10 / ROAD_PRIORITY[highway] + min(length_km, 5), 4),
                "interpretation": "screening rank; no confirmed damage or marginal reconnection estimate",
            }
        )
    critical_rows.sort(
        key=lambda row: (
            -float(row["candidate_score"]),
            int(row["road_hierarchy_rank"]),
            -float(row["intersecting_length_km"]),
        )
    )
    for rank, row in enumerate(critical_rows, 1):
        row["candidate_rank"] = rank
    field_order = ["candidate_rank"] + [key for key in critical_rows[0] if key != "candidate_rank"]
    critical_rows = [{key: row[key] for key in field_order} for row in critical_rows]
    write_rows(table_dir / "pilot_disrupted_road_candidates.csv", critical_rows)

    baseline_reachable_count = sum(
        bool(row["baseline_minutes"] != "") for row in settlement_rows
    )
    road_isolated_count = sum(bool(row["road_only_isolated"]) for row in settlement_rows)
    conservative_isolated_count = sum(
        bool(row["conservative_isolated"]) for row in settlement_rows
    )
    delays = [
        float(row["conservative_delay_minutes"])
        for row in settlement_rows
        if row["conservative_delay_minutes"] != ""
    ]
    summary_rows = [
        {"metric": "motor_road_features", "value": len(motor_roads), "unit": "features"},
        {"metric": "graph_nodes", "value": len(node_coords), "unit": "nodes"},
        {"metric": "graph_edges", "value": len(edges), "unit": "segments"},
        {"metric": "disrupted_edges", "value": disrupted_edge_count, "unit": "segments"},
        {"metric": "disrupted_osm_features", "value": len(disrupted_features), "unit": "features"},
        {"metric": "service_facilities", "value": len(targets), "unit": "facilities"},
        {"metric": "service_sources_snapped", "value": len(all_sources), "unit": "unique_nodes"},
        {"metric": "service_facilities_inside_hazard", "value": target_in_hazard, "unit": "facilities"},
        {"metric": "settlements", "value": len(settlements), "unit": "settlements"},
        {"metric": "baseline_reachable_settlements", "value": baseline_reachable_count, "unit": "settlements"},
        {
            "metric": "baseline_reachable_share",
            "value": round(baseline_reachable_count / len(settlements), 6),
            "unit": "fraction",
        },
        {"metric": "road_only_isolated_settlements", "value": road_isolated_count, "unit": "settlements"},
        {"metric": "conservative_isolated_settlements", "value": conservative_isolated_count, "unit": "settlements"},
        {
            "metric": "conservative_isolated_share_of_baseline_reachable",
            "value": round(conservative_isolated_count / baseline_reachable_count, 6),
            "unit": "fraction",
        },
        {
            "metric": "median_conservative_delay_reachable",
            "value": round(float(np.median(delays)), 3) if delays else "",
            "unit": "minutes",
        },
        {
            "metric": "p95_conservative_delay_reachable",
            "value": round(float(np.percentile(delays, 95)), 3) if delays else "",
            "unit": "minutes",
        },
        {"metric": "maximum_snap_distance", "value": MAX_SNAP_M, "unit": "metres"},
    ]
    write_rows(table_dir / "pilot_road_access_summary.csv", summary_rows)

    bounds = analysis.total_bounds
    padding = 4_000
    fig, ax = plt.subplots(figsize=(9.5, 10))
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.12, top=0.89)
    analysis.boundary.plot(ax=ax, color="#542788", linestyle="--", linewidth=1.1)
    affected.plot(ax=ax, color="#d73027", alpha=0.35, edgecolor="#7f0000", linewidth=0.8)
    motor_roads.plot(ax=ax, color="#9e9e9e", linewidth=0.28, alpha=0.5)
    motor_roads.loc[motor_roads["highway"].isin(["trunk", "primary", "secondary"])].plot(
        ax=ax, color="#fdae61", linewidth=0.8, alpha=0.9
    )
    palette = {
        "isolated_conservative": ("#7f0000", "^", 28),
        "delay_over_5min": ("#e66101", "o", 19),
        "limited_change": ("#1a9850", "o", 10),
        "baseline_unreachable": ("#756bb1", "x", 18),
        "off_network": ("#636363", "x", 18),
    }
    for status, (colour, marker, size) in palette.items():
        subset = settlement_output.loc[settlement_output["pilot_status"].eq(status)]
        if not subset.empty:
            subset.plot(ax=ax, color=colour, marker=marker, markersize=size, zorder=5)
    targets.loc[~targets.geometry.intersects(hazard)].plot(
        ax=ax, color="#2166ac", marker="+", markersize=26, linewidth=1.0, zorder=6
    )
    ax.set_xlim(bounds[0] - padding, bounds[2] + padding)
    ax.set_ylim(bounds[1] - padding, bounds[3] + padding)
    ax.set_aspect("equal")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
    ax.set_xlabel("Easting (km), WGS 84 / UTM zone 45N")
    ax.set_ylabel("Northing (km)")
    ax.set_title(
        "Pilot road-access disruption screening\nSettlement access to health and emergency facilities",
        loc="left",
        fontsize=14,
        fontweight="bold",
    )
    legend = [
        Patch(facecolor="#d73027", alpha=0.35, edgecolor="#7f0000", label="UNOSAT affected extent"),
        Line2D([0], [0], color="#fdae61", label="Major road"),
        Line2D([0], [0], marker="+", color="#2166ac", lw=0, label="Available service facility"),
        Line2D([0], [0], marker="^", color="#7f0000", lw=0, label="Isolated in conservative scenario"),
        Line2D([0], [0], marker="o", color="#e66101", lw=0, label="Delay >5 min"),
        Line2D([0], [0], marker="o", color="#1a9850", lw=0, label="Limited change"),
        Line2D([0], [0], marker="x", color="#756bb1", lw=0, label="Baseline topology gap"),
        Line2D([0], [0], marker="x", color="#636363", lw=0, label="More than 3 km off network"),
    ]
    ax.legend(handles=legend, loc="lower left", fontsize=7.5, framealpha=0.92)
    fig.text(
        0.01,
        0.005,
        "Pilot assumptions: undirected pre-event OSM motor-road graph; class-based speeds; roads intersecting the preliminary UNOSAT extent removed.\n"
        "The conservative scenario also excludes service facilities inside the extent. Results are topology screening, not observed travel times.",
        fontsize=7,
        color="#444444",
    )
    figure_dir.mkdir(parents=True, exist_ok=True)
    figure_path = figure_dir / "pilot_road_access_disruption.png"
    fig.savefig(figure_path, dpi=220, facecolor="white")
    plt.close(fig)
    print(
        {
            "graph_nodes": len(node_coords),
            "graph_edges": len(edges),
            "baseline_reachable": baseline_reachable_count,
            "conservative_isolated": conservative_isolated_count,
            "figure": str(figure_path),
        }
    )


if __name__ == "__main__":
    main()
