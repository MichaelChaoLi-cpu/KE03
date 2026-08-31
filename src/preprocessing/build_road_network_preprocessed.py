#!/usr/bin/env python3
"""Build analysis-ready road-network topology scenarios and access crosswalks."""

from __future__ import annotations

import argparse
import heapq
import json
import math
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from shapely import STRtree, points
from shapely.geometry import LineString
from shapely.prepared import prep


CRS = "EPSG:32645"
PRIMARY_REPAIR_THRESHOLD_M = 5
ROBUSTNESS_THRESHOLDS_M = (0, 10, 20)
TOPOLOGY_THRESHOLDS_M = (0, 5, 10, 20)
MAX_CANDIDATE_DISTANCE_M = max(TOPOLOGY_THRESHOLDS_M)
MAX_SNAP_DISTANCE_M = 3_000
REPAIR_SPEED_KMH = 10
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


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
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


def clean_text(value: object) -> str | None:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    text = str(value).strip()
    return text or None


def dijkstra(
    node_count: int,
    edges: list[tuple[int, int, float, int]],
    sources: set[int],
    threshold: int,
) -> np.ndarray:
    adjacency: list[list[tuple[int, float]]] = [[] for _ in range(node_count)]
    for left, right, minutes, minimum_threshold in edges:
        if minimum_threshold > threshold:
            continue
        adjacency[left].append((right, minutes))
        adjacency[right].append((left, minutes))
    distances = np.full(node_count, np.inf, dtype="float64")
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    source = root / "data/processed/geospatial/base/osm_pre_event_aoi.gpkg"
    reference = root / "data/processed/geospatial/reference/unosat_event_reference.gpkg"
    output = root / "data/processed/geospatial/network"
    audit_output = root / "data/exp/data-preprocessing"
    if not source.exists():
        raise FileNotFoundError(source)
    if not reference.exists():
        raise FileNotFoundError(reference)

    roads = gpd.read_file(source, layer="roads").to_crs(CRS)
    waterways = gpd.read_file(source, layer="waterways").to_crs(CRS)
    settlements = gpd.read_file(source, layer="settlements").to_crs(CRS)
    facilities = gpd.read_file(source, layer="facilities").to_crs(CRS)
    affected = gpd.read_file(reference, layer="affected_extent").to_crs(CRS)
    affected_prepared = prep(affected.geometry.union_all())
    roads = roads.loc[roads["highway"].isin(ROAD_SPEED_KMH)].copy()

    node_lookup: dict[tuple[float, float], int] = {}
    node_coordinates: list[tuple[float, float]] = []
    node_degree: list[int] = []
    edge_rows: list[dict[str, object]] = []
    graph_edges: list[tuple[int, int, float, int]] = []

    def node_id(coordinate: tuple[float, float]) -> int:
        key = (round(float(coordinate[0]), 3), round(float(coordinate[1]), 3))
        if key in node_lookup:
            return node_lookup[key]
        identifier = len(node_coordinates)
        node_lookup[key] = identifier
        node_coordinates.append(key)
        node_degree.append(0)
        return identifier

    for road in roads.itertuples():
        highway = str(road.highway)
        speed = ROAD_SPEED_KMH[highway]
        coordinates = list(road.geometry.coords)
        for start, end in zip(coordinates[:-1], coordinates[1:]):
            left, right = node_id(start), node_id(end)
            if left == right:
                continue
            segment = LineString((start, end))
            length = float(segment.length)
            if length <= 0:
                continue
            minutes = length / (speed * 1_000 / 60)
            node_degree[left] += 1
            node_degree[right] += 1
            graph_edges.append((left, right, minutes, 0))
            edge_rows.append(
                {
                    "Edge ID": len(edge_rows),
                    "From node ID": left,
                    "To node ID": right,
                    "Edge type": "mapped road",
                    "Road class": highway,
                    "Road speed (km/h)": speed,
                    "Edge length (m)": length,
                    "Edge travel time (minutes)": minutes,
                    "Minimum topology repair threshold (m)": 0,
                    "Intersects preliminary event footprint": bool(
                        affected_prepared.intersects(segment)
                    ),
                    "OSM feature ID": clean_text(road.osm_id),
                    "Road name": clean_text(road.name),
                    "Is bridge": bool(road.is_bridge),
                }
            )

    strict_graph = DisjointSet(len(node_coordinates))
    for left, right, _, _ in graph_edges:
        strict_graph.union(left, right)
    strict_roots = [strict_graph.find(index) for index in range(len(node_coordinates))]
    node_array = np.asarray(node_coordinates, dtype="float64")
    node_geometries = points(node_array[:, 0], node_array[:, 1])
    node_tree = STRtree(node_geometries)
    water_tree = STRtree(waterways.geometry.to_numpy())

    candidate_by_pair: dict[tuple[int, int], dict[str, object]] = {}
    endpoints = np.flatnonzero(np.asarray(node_degree) == 1)
    for endpoint in endpoints:
        point = node_geometries[endpoint]
        nearby = node_tree.query(
            point, predicate="dwithin", distance=MAX_CANDIDATE_DISTANCE_M
        )
        best: tuple[float, int] | None = None
        for candidate_value in nearby:
            candidate = int(candidate_value)
            if candidate == endpoint or strict_roots[candidate] == strict_roots[endpoint]:
                continue
            distance = float(point.distance(node_geometries[candidate]))
            if best is None or distance < best[0]:
                best = (distance, candidate)
        if best is None:
            continue
        distance, candidate = best
        pair = tuple(sorted((int(endpoint), candidate)))
        connector = LineString((node_coordinates[endpoint], node_coordinates[candidate]))
        crosses_waterway = len(water_tree.query(connector, predicate="intersects")) > 0
        previous = candidate_by_pair.get(pair)
        if previous is None or distance < float(previous["distance"]):
            candidate_by_pair[pair] = {
                "left": pair[0],
                "right": pair[1],
                "distance": distance,
                "crosses_waterway": crosses_waterway,
                "geometry": connector,
            }

    candidates = sorted(candidate_by_pair.values(), key=lambda row: float(row["distance"]))
    accepted_minimum: dict[tuple[int, int], int] = {}
    accepted_by_threshold: dict[int, int] = {}
    components_by_threshold: dict[int, int] = {}
    rejected_by_threshold: dict[int, int] = {}
    redundant_by_threshold: dict[int, int] = {}
    for threshold in TOPOLOGY_THRESHOLDS_M:
        graph = strict_graph.copy()
        accepted = 0
        rejected = 0
        redundant = 0
        for candidate in candidates:
            if float(candidate["distance"]) > threshold:
                break
            if bool(candidate["crosses_waterway"]):
                rejected += 1
                continue
            pair = (int(candidate["left"]), int(candidate["right"]))
            if graph.union(*pair):
                accepted += 1
                accepted_minimum.setdefault(pair, threshold)
            else:
                redundant += 1
        accepted_by_threshold[threshold] = accepted
        components_by_threshold[threshold] = graph.components
        rejected_by_threshold[threshold] = rejected
        redundant_by_threshold[threshold] = redundant

    for candidate in candidates:
        pair = (int(candidate["left"]), int(candidate["right"]))
        if pair not in accepted_minimum:
            continue
        threshold = accepted_minimum[pair]
        length = float(candidate["distance"])
        minutes = length / (REPAIR_SPEED_KMH * 1_000 / 60)
        graph_edges.append((pair[0], pair[1], minutes, threshold))
        edge_rows.append(
            {
                "Edge ID": len(edge_rows),
                "From node ID": pair[0],
                "To node ID": pair[1],
                "Edge type": "topology repair",
                "Road class": "topology repair",
                "Road speed (km/h)": REPAIR_SPEED_KMH,
                "Edge length (m)": length,
                "Edge travel time (minutes)": minutes,
                "Minimum topology repair threshold (m)": threshold,
                "Intersects preliminary event footprint": bool(
                    affected_prepared.intersects(candidate["geometry"])
                ),
                "OSM feature ID": None,
                "Road name": None,
                "Is bridge": False,
            }
        )

    node_frame = pd.DataFrame(
        {
            "Road node ID": np.arange(len(node_coordinates), dtype="int64"),
            "Easting (m)": node_array[:, 0],
            "Northing (m)": node_array[:, 1],
            "Mapped degree": np.asarray(node_degree, dtype="int32"),
        }
    )
    edge_frame = pd.DataFrame(edge_rows)
    edge_frame["Road class"] = edge_frame["Road class"].astype("category")
    edge_frame["Edge type"] = edge_frame["Edge type"].astype("category")

    settlement_crosswalk: list[dict[str, object]] = []
    for settlement in settlements.itertuples():
        nearest = int(node_tree.nearest(settlement.geometry))
        distance = float(settlement.geometry.distance(node_geometries[nearest]))
        settlement_crosswalk.append(
            {
                "OSM settlement ID": clean_text(settlement.osm_id),
                "Settlement name": clean_text(settlement.name),
                "Place type": clean_text(settlement.place),
                "Nearest road node ID": nearest,
                "Settlement-to-road snap distance (m)": distance,
                "Within 500 m of road": distance <= 500,
                "Within 1000 m of road": distance <= 1_000,
                "Within 2000 m of road": distance <= 2_000,
                "Within 3000 m of road": distance <= MAX_SNAP_DISTANCE_M,
            }
        )

    facility_crosswalk: list[dict[str, object]] = []
    service_nodes: set[int] = set()
    for facility in facilities.itertuples():
        nearest = int(node_tree.nearest(facility.geometry))
        distance = float(facility.geometry.distance(node_geometries[nearest]))
        category = clean_text(facility.facility_category)
        included = category in {"health", "emergency"} and distance <= MAX_SNAP_DISTANCE_M
        if included:
            service_nodes.add(nearest)
        facility_crosswalk.append(
            {
                "OSM facility ID": clean_text(facility.osm_id),
                "Facility name": clean_text(facility.name),
                "Facility category": category,
                "Nearest road node ID": nearest,
                "Facility-to-road snap distance (m)": distance,
                "Included health/emergency destination": included,
            }
        )

    accessibility_rows: list[dict[str, object]] = []
    scenario_rows: list[dict[str, object]] = []
    for threshold in TOPOLOGY_THRESHOLDS_M:
        distances = dijkstra(len(node_coordinates), graph_edges, service_nodes, threshold)
        reachable = 0
        for settlement in settlement_crosswalk:
            on_network = bool(settlement["Within 3000 m of road"])
            node = int(settlement["Nearest road node ID"])
            travel_minutes = float(distances[node]) if on_network else math.inf
            is_reachable = math.isfinite(travel_minutes)
            reachable += int(is_reachable)
            accessibility_rows.append(
                {
                    "OSM settlement ID": settlement["OSM settlement ID"],
                    "Topology repair threshold (m)": threshold,
                    "Primary topology scenario": threshold == PRIMARY_REPAIR_THRESHOLD_M,
                    "Maximum settlement snap distance (m)": MAX_SNAP_DISTANCE_M,
                    "Baseline service reachable": is_reachable,
                    "Baseline health/emergency accessibility (minutes)": (
                        travel_minutes if is_reachable else np.nan
                    ),
                }
            )
        scenario_rows.append(
            {
                "Topology repair threshold (m)": threshold,
                "Scenario role": (
                    "primary" if threshold == PRIMARY_REPAIR_THRESHOLD_M else "robustness"
                ),
                "Road components": components_by_threshold[threshold],
                "Accepted topology repairs": accepted_by_threshold[threshold],
                "Rejected mapped-waterway crossings": rejected_by_threshold[threshold],
                "Redundant repair candidates": redundant_by_threshold[threshold],
                "Baseline reachable settlements": reachable,
                "Total settlements": len(settlement_crosswalk),
                "Reachable settlement share": reachable / len(settlement_crosswalk),
            }
        )

    output.mkdir(parents=True, exist_ok=True)
    node_frame.to_parquet(output / "road_nodes_preprocessed.parquet", index=False)
    edge_frame.to_parquet(output / "road_edges_preprocessed.parquet", index=False)
    pd.DataFrame(settlement_crosswalk).to_parquet(
        output / "settlement_road_crosswalk_preprocessed.parquet", index=False
    )
    pd.DataFrame(facility_crosswalk).to_parquet(
        output / "facility_road_crosswalk_preprocessed.parquet", index=False
    )
    pd.DataFrame(accessibility_rows).to_parquet(
        output / "settlement_baseline_accessibility_preprocessed.parquet", index=False
    )
    scenario_frame = pd.DataFrame(scenario_rows)
    scenario_frame.to_parquet(
        output / "road_topology_scenarios_preprocessed.parquet", index=False
    )

    audit_output.mkdir(parents=True, exist_ok=True)
    scenario_frame.to_csv(audit_output / "road_topology_scenario_summary.csv", index=False)
    decisions = {
        "status": "confirmed",
        "source": "data/processed/geospatial/base/osm_pre_event_aoi.gpkg",
        "primary_topology_repair_threshold_m": PRIMARY_REPAIR_THRESHOLD_M,
        "robustness_topology_repair_thresholds_m": list(ROBUSTNESS_THRESHOLDS_M),
        "maximum_settlement_and_facility_snap_distance_m": MAX_SNAP_DISTANCE_M,
        "repair_rule": "connect dangling endpoints to nearest nodes in different components",
        "waterway_rule": "reject connectors intersecting mapped waterways",
        "mapped_road_speeds_kmh": ROAD_SPEED_KMH,
        "topology_repair_speed_kmh": REPAIR_SPEED_KMH,
        "missing_value_treatment": "preserve missing values; do not impute",
        "event_footprint_intersection": "screening attribute only; not confirmed damage",
    }
    (audit_output / "geospatial_network_decisions.json").write_text(
        json.dumps(decisions, ensure_ascii=True, indent=2) + "\n", encoding="utf-8"
    )
    print(
        {
            "nodes": len(node_frame),
            "mapped_edges": int(edge_frame["Edge type"].eq("mapped road").sum()),
            "repair_edges_through_20m": int(edge_frame["Edge type"].eq("topology repair").sum()),
            "settlements": len(settlement_crosswalk),
            "facilities": len(facility_crosswalk),
            "service_nodes": len(service_nodes),
            "primary_reachable_settlements": int(
                scenario_frame.loc[
                    scenario_frame["Scenario role"].eq("primary"),
                    "Baseline reachable settlements",
                ].iloc[0]
            ),
            "output": str(output),
        }
    )


if __name__ == "__main__":
    main()
