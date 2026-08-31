#!/usr/bin/env python3
"""Audit candidate endpoint-to-node repairs for the pre-event motor-road graph."""

from __future__ import annotations

import argparse
import csv
import math
import os
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


CRS = "EPSG:32645"
MAX_NETWORK_SNAP_M = 3_000
MAX_REPAIR_DISTANCE_M = 50
THRESHOLDS_M = (0, 5, 10, 20, 50)
MOTOR_ROADS = {
    "trunk",
    "trunk_link",
    "primary",
    "primary_link",
    "secondary",
    "secondary_link",
    "tertiary",
    "tertiary_link",
    "residential",
    "living_street",
    "unclassified",
    "service",
    "road",
    "track",
}


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, value: int) -> int:
        parent = self.parent
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(self, left: int, right: int) -> bool:
        left_root, right_root = self.find(left), self.find(right)
        if left_root == right_root:
            return False
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1
        self.components -= 1
        return True

    def copy(self) -> "DisjointSet":
        duplicate = DisjointSet.__new__(DisjointSet)
        duplicate.parent = self.parent.copy()
        duplicate.rank = self.rank.copy()
        duplicate.components = self.components
        return duplicate


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
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

    osm_path = root / "data/processed/geospatial/base/osm_pre_event_aoi.gpkg"
    reference_path = root / "data/processed/geospatial/reference/unosat_event_reference.gpkg"
    roads = gpd.read_file(osm_path, layer="roads").to_crs(CRS)
    waterways = gpd.read_file(osm_path, layer="waterways").to_crs(CRS)
    settlements = gpd.read_file(osm_path, layer="settlements").to_crs(CRS)
    facilities = gpd.read_file(osm_path, layer="facilities").to_crs(CRS)
    affected = gpd.read_file(reference_path, layer="affected_extent").to_crs(CRS)
    analysis = gpd.read_file(reference_path, layer="analysis_extent").to_crs(CRS)
    motor_roads = roads.loc[roads["highway"].isin(MOTOR_ROADS)]

    lookup: dict[tuple[float, float], int] = {}
    coordinates: list[tuple[float, float]] = []
    degree: list[int] = []
    edges: list[tuple[int, int]] = []

    def node_id(coordinate: tuple[float, float]) -> int:
        key = (round(float(coordinate[0]), 3), round(float(coordinate[1]), 3))
        if key in lookup:
            return lookup[key]
        identifier = len(coordinates)
        lookup[key] = identifier
        coordinates.append(key)
        degree.append(0)
        return identifier

    for road in motor_roads.itertuples():
        line = list(road.geometry.coords)
        for start, end in zip(line[:-1], line[1:]):
            u, v = node_id(start), node_id(end)
            if u == v:
                continue
            edges.append((u, v))
            degree[u] += 1
            degree[v] += 1

    baseline = DisjointSet(len(coordinates))
    for u, v in edges:
        baseline.union(u, v)
    baseline_roots = [baseline.find(index) for index in range(len(coordinates))]

    coordinate_array = np.asarray(coordinates)
    node_geometries = points(coordinate_array[:, 0], coordinate_array[:, 1])
    node_tree = STRtree(node_geometries)
    water_geometries = waterways.geometry.to_numpy()
    water_tree = STRtree(water_geometries)
    endpoint_ids = np.flatnonzero(np.asarray(degree) == 1)

    candidate_by_pair: dict[tuple[int, int], dict[str, object]] = {}
    for endpoint in endpoint_ids:
        point = node_geometries[endpoint]
        nearby = node_tree.query(
            point, predicate="dwithin", distance=MAX_REPAIR_DISTANCE_M
        )
        best: tuple[float, int] | None = None
        endpoint_root = baseline_roots[endpoint]
        for candidate in nearby:
            candidate = int(candidate)
            if candidate == endpoint or baseline_roots[candidate] == endpoint_root:
                continue
            distance = float(point.distance(node_geometries[candidate]))
            if best is None or distance < best[0]:
                best = (distance, candidate)
        if best is None:
            continue
        distance, candidate = best
        pair = tuple(sorted((int(endpoint), candidate)))
        connector = LineString((coordinates[endpoint], coordinates[candidate]))
        water_hits = water_tree.query(connector, predicate="intersects")
        crosses_waterway = len(water_hits) > 0
        record = {
            "from_node": pair[0],
            "to_node": pair[1],
            "distance_m": round(distance, 4),
            "crosses_mapped_waterway": crosses_waterway,
            "from_easting": round(coordinates[pair[0]][0], 3),
            "from_northing": round(coordinates[pair[0]][1], 3),
            "to_easting": round(coordinates[pair[1]][0], 3),
            "to_northing": round(coordinates[pair[1]][1], 3),
            "geometry": connector,
        }
        previous = candidate_by_pair.get(pair)
        if previous is None or float(record["distance_m"]) < float(previous["distance_m"]):
            candidate_by_pair[pair] = record

    candidates = sorted(candidate_by_pair.values(), key=lambda row: float(row["distance_m"]))

    targets = facilities.loc[
        facilities["facility_category"].isin(["health", "emergency"])
    ]
    service_nodes: set[int] = set()
    for geometry in targets.geometry:
        nearest = int(node_tree.nearest(geometry))
        if geometry.distance(node_geometries[nearest]) <= MAX_NETWORK_SNAP_M:
            service_nodes.add(nearest)

    settlement_nodes: list[tuple[int, float]] = []
    for geometry in settlements.geometry:
        nearest = int(node_tree.nearest(geometry))
        settlement_nodes.append((nearest, float(geometry.distance(node_geometries[nearest]))))

    sensitivity_rows: list[dict[str, object]] = []
    accepted_by_threshold: dict[int, set[tuple[int, int]]] = {}
    baseline_reachable = None
    for threshold in THRESHOLDS_M:
        graph = baseline.copy()
        accepted: set[tuple[int, int]] = set()
        eligible = 0
        rejected_water = 0
        redundant = 0
        for record in candidates:
            if float(record["distance_m"]) > threshold:
                break
            if bool(record["crosses_mapped_waterway"]):
                rejected_water += 1
                continue
            eligible += 1
            pair = (int(record["from_node"]), int(record["to_node"]))
            if graph.union(*pair):
                accepted.add(pair)
            else:
                redundant += 1
        service_roots = {graph.find(node) for node in service_nodes}
        reachable = 0
        off_network = 0
        for node, snap_distance in settlement_nodes:
            if snap_distance > MAX_NETWORK_SNAP_M:
                off_network += 1
            elif graph.find(node) in service_roots:
                reachable += 1
        if threshold == 0:
            baseline_reachable = reachable
        accepted_by_threshold[threshold] = accepted
        sensitivity_rows.append(
            {
                "repair_threshold_m": threshold,
                "road_components": graph.components,
                "eligible_gap_candidates": eligible,
                "accepted_component_merges": len(accepted),
                "redundant_candidates": redundant,
                "rejected_waterway_crossings": rejected_water,
                "baseline_reachable_settlements": reachable,
                "newly_reachable_vs_strict_topology": reachable - int(baseline_reachable),
                "reachable_share_all_settlements": round(reachable / len(settlements), 6),
                "settlements_over_3km_off_network": off_network,
                "rule": "connect dangling endpoint to nearest node in another component; reject mapped-waterway crossings",
            }
        )

    for rank, record in enumerate(candidates, 1):
        record["candidate_rank"] = rank
        record["accepted_at_5m"] = (
            int(record["from_node"]), int(record["to_node"])
        ) in accepted_by_threshold[5]
        record["accepted_at_10m"] = (
            int(record["from_node"]), int(record["to_node"])
        ) in accepted_by_threshold[10]
        record["accepted_at_20m"] = (
            int(record["from_node"]), int(record["to_node"])
        ) in accepted_by_threshold[20]
        record["accepted_at_50m"] = (
            int(record["from_node"]), int(record["to_node"])
        ) in accepted_by_threshold[50]

    table_dir = root / "data/exp/data-briefing/tables"
    serializable_rows = [
        {key: value for key, value in record.items() if key != "geometry"}
        for record in candidates
    ]
    if serializable_rows:
        ordered = ["candidate_rank"] + [
            key for key in serializable_rows[0] if key != "candidate_rank"
        ]
        serializable_rows = [{key: row[key] for key in ordered} for row in serializable_rows]
        write_rows(table_dir / "road_topology_gap_candidates.csv", serializable_rows)
    write_rows(table_dir / "road_topology_repair_sensitivity.csv", sensitivity_rows)

    candidate_frame = gpd.GeoDataFrame(candidates, geometry="geometry", crs=CRS)
    bounds = analysis.total_bounds
    padding = 4_000
    fig, ax = plt.subplots(figsize=(9.5, 10))
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.10, top=0.90)
    motor_roads.plot(ax=ax, color="#bdbdbd", linewidth=0.22, alpha=0.55)
    affected.plot(ax=ax, color="#d73027", edgecolor="#7f0000", alpha=0.28, linewidth=0.7)
    analysis.boundary.plot(ax=ax, color="#542788", linestyle="--", linewidth=1.0)
    bands = [
        (0, 5, "#1b9e77", "Accepted gap repair: <=5 m"),
        (5, 10, "#377eb8", "Accepted gap repair: 5-10 m"),
        (10, 20, "#ff7f00", "Accepted gap repair: 10-20 m"),
        (20, 50, "#e41a1c", "Accepted gap repair: 20-50 m"),
    ]
    accepted_50 = accepted_by_threshold[50]
    for lower, upper, colour, _ in bands:
        subset = candidate_frame.loc[
            candidate_frame.apply(
                lambda row: (int(row.from_node), int(row.to_node)) in accepted_50
                and lower < float(row.distance_m) <= upper
                if lower > 0
                else (int(row.from_node), int(row.to_node)) in accepted_50
                and float(row.distance_m) <= upper,
                axis=1,
            )
        ]
        if not subset.empty:
            subset.plot(ax=ax, color=colour, linewidth=1.0, alpha=0.9, zorder=5)
    ax.set_xlim(bounds[0] - padding, bounds[2] + padding)
    ax.set_ylim(bounds[1] - padding, bounds[3] + padding)
    ax.set_aspect("equal")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
    ax.set_xlabel("Easting (km), WGS 84 / UTM zone 45N")
    ax.set_ylabel("Northing (km)")
    ax.set_title(
        "Road-topology repair candidate audit\nDangling endpoints connected across small mapped gaps",
        loc="left",
        fontsize=14,
        fontweight="bold",
    )
    legend = [
        Patch(facecolor="#d73027", edgecolor="#7f0000", alpha=0.28, label="UNOSAT affected extent"),
        Line2D([0], [0], color="#542788", linestyle="--", label="UNOSAT analysis extent"),
    ] + [Line2D([0], [0], color=colour, label=label) for _, _, colour, label in bands]
    ax.legend(handles=legend, loc="lower left", fontsize=7.5, framealpha=0.94)
    fig.text(
        0.01,
        0.02,
        "Exploratory audit only. Candidate connectors join dangling endpoints to nearby nodes in different components; connectors crossing mapped waterways are rejected.\n"
        "No repair threshold is treated as final until visual review and human confirmation.",
        fontsize=7,
        color="#444444",
    )
    figure_dir = root / "data/exp/data-briefing/figures/geospatial"
    figure_dir.mkdir(parents=True, exist_ok=True)
    figure_path = figure_dir / "road_topology_repair_candidate_audit.png"
    fig.savefig(figure_path, dpi=220, facecolor="white")
    plt.close(fig)
    print(
        {
            "nodes": len(coordinates),
            "strict_components": baseline.components,
            "dangling_endpoints": len(endpoint_ids),
            "gap_candidates": len(candidates),
            "sensitivity": sensitivity_rows,
            "figure": str(figure_path),
        }
    )


if __name__ == "__main__":
    main()
