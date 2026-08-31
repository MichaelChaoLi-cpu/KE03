#!/usr/bin/env python3
"""Simulate graded road disruption and health/emergency service accessibility."""

from __future__ import annotations

import argparse
import csv
import heapq
import math
from pathlib import Path

import numpy as np
import pandas as pd


NETWORK_DIR = Path("data/processed/geospatial/network")
EXPOSURE_DIR = Path("data/processed/geospatial/exposure")
OUTPUT_SETTLEMENTS = Path(
    "data/processed/geospatial/accessibility/"
    "settlement_disruption_accessibility_preprocessed.parquet"
)
OUTPUT_SCENARIOS = Path(
    "data/processed/geospatial/accessibility/"
    "accessibility_scenario_summary_preprocessed.parquet"
)
OUTPUT_SCENARIOS_CSV = Path(
    "data/exp/data-preprocessing/accessibility_scenario_summary.csv"
)
AUDIT = Path(
    "data/exp/data-preprocessing/disruption_accessibility_audit.csv"
)

PRIMARY_TOPOLOGY_THRESHOLD_M = 5
MAX_SETTLEMENT_SNAP_M = 3_000
DELAY_THRESHOLD_MINUTES = 5.0

HAZARD_SCENARIOS = (
    ("Primary conservative", 3),
    ("Alternative mapped or multisensor", 2),
    ("Sensitivity screening", 1),
)
CLOSURE_RULES = (
    ("Destroyed only", {"Destroyed"}),
    (
        "All disruption candidates",
        {"Possibly damaged", "Damaged", "Destroyed"},
    ),
)
FACILITY_RULES = (
    ("Road disruption only", False),
    ("Road and directly exposed facility disruption", True),
)


def build_adjacency(
    node_count: int, edges: pd.DataFrame
) -> list[list[tuple[int, float, int]]]:
    adjacency: list[list[tuple[int, float, int]]] = [
        [] for _ in range(node_count)
    ]
    for row in edges.itertuples(index=False):
        edge_id = int(row.edge_id)
        left = int(row.left)
        right = int(row.right)
        minutes = float(row.minutes)
        adjacency[left].append((right, minutes, edge_id))
        adjacency[right].append((left, minutes, edge_id))
    return adjacency


def dijkstra(
    adjacency: list[list[tuple[int, float, int]]],
    sources: set[int],
    closed_edges: np.ndarray,
) -> np.ndarray:
    distances = np.full(len(adjacency), np.inf, dtype="float64")
    queue: list[tuple[float, int]] = []
    for source in sources:
        distances[source] = 0.0
        heapq.heappush(queue, (0.0, source))
    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbour, cost, edge_id in adjacency[node]:
            if closed_edges[edge_id]:
                continue
            candidate = distance + cost
            if candidate < distances[neighbour]:
                distances[neighbour] = candidate
                heapq.heappush(queue, (candidate, neighbour))
    return distances


def service_nodes(
    facility_crosswalk: pd.DataFrame,
    facility_exposure: pd.DataFrame,
    threshold: int,
    remove_exposed: bool,
) -> tuple[set[int], int]:
    exposure = facility_exposure.set_index("OSM Facility ID")[
        "Direct Evidence Class"
    ]
    nodes: set[int] = set()
    removed = 0
    for row in facility_crosswalk.loc[
        facility_crosswalk["Included health/emergency destination"]
    ].itertuples(index=False):
        facility_id = str(row[0])
        direct_class = exposure.get(facility_id, pd.NA)
        is_exposed = (
            not pd.isna(direct_class) and int(direct_class) >= threshold
        )
        if remove_exposed and is_exposed:
            removed += 1
            continue
        nodes.add(int(row[3]))
    return nodes, removed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    edge_path = root / NETWORK_DIR / "road_edges_preprocessed.parquet"
    node_path = root / NETWORK_DIR / "road_nodes_preprocessed.parquet"
    settlement_path = (
        root / NETWORK_DIR / "settlement_road_crosswalk_preprocessed.parquet"
    )
    facility_path = (
        root / NETWORK_DIR / "facility_road_crosswalk_preprocessed.parquet"
    )
    baseline_path = (
        root
        / NETWORK_DIR
        / "settlement_baseline_accessibility_preprocessed.parquet"
    )
    damage_path = (
        root
        / EXPOSURE_DIR
        / "road_damage_scenario_exposure_preprocessed.parquet"
    )
    facility_exposure_path = (
        root
        / EXPOSURE_DIR
        / "facility_hazard_exposure_preprocessed.parquet"
    )
    for path in (
        edge_path,
        node_path,
        settlement_path,
        facility_path,
        baseline_path,
        damage_path,
        facility_exposure_path,
    ):
        if not path.exists():
            raise FileNotFoundError(path)

    nodes = pd.read_parquet(node_path)
    edges_all = pd.read_parquet(edge_path)
    edges = edges_all.loc[
        edges_all["Minimum topology repair threshold (m)"]
        <= PRIMARY_TOPOLOGY_THRESHOLD_M,
        [
            "Edge ID",
            "From node ID",
            "To node ID",
            "Edge travel time (minutes)",
        ],
    ].copy()
    edges.columns = ["edge_id", "left", "right", "minutes"]
    adjacency = build_adjacency(len(nodes), edges)
    maximum_edge_id = int(edges_all["Edge ID"].max())
    no_closed_edges = np.zeros(maximum_edge_id + 1, dtype=bool)

    settlements = pd.read_parquet(settlement_path)
    facilities = pd.read_parquet(facility_path)
    facility_exposure = pd.read_parquet(facility_exposure_path)
    damage = pd.read_parquet(damage_path)
    baseline_saved = pd.read_parquet(baseline_path)
    baseline_saved = baseline_saved.loc[
        baseline_saved["Topology repair threshold (m)"]
        == PRIMARY_TOPOLOGY_THRESHOLD_M
    ].copy()

    all_service_nodes, _ = service_nodes(
        facilities, facility_exposure, threshold=1, remove_exposed=False
    )
    baseline_distances = dijkstra(
        adjacency, all_service_nodes, no_closed_edges
    )
    settlement_nodes = settlements["Nearest road node ID"].to_numpy(dtype="int64")
    on_network = settlements["Within 3000 m of road"].to_numpy(dtype=bool)
    baseline_minutes = baseline_distances[settlement_nodes]
    baseline_eligible = on_network & np.isfinite(baseline_minutes)

    saved = baseline_saved.set_index("OSM settlement ID").reindex(
        settlements["OSM settlement ID"]
    )
    saved_minutes = saved[
        "Baseline health/emergency accessibility (minutes)"
    ].to_numpy(dtype="float64")
    saved_reachable = saved["Baseline service reachable"].to_numpy(dtype=bool)
    finite_both = np.isfinite(saved_minutes) & np.isfinite(baseline_minutes)
    maximum_baseline_difference = (
        float(np.max(np.abs(saved_minutes[finite_both] - baseline_minutes[finite_both])))
        if finite_both.any()
        else 0.0
    )
    reachable_mismatches = int(
        np.count_nonzero(saved_reachable != baseline_eligible)
    )
    if maximum_baseline_difference > 1e-8 or reachable_mismatches:
        raise RuntimeError(
            "Recomputed baseline does not match saved primary-topology accessibility: "
            f"max difference={maximum_baseline_difference}, "
            f"reachable mismatches={reachable_mismatches}"
        )

    settlement_rows: list[dict[str, object]] = []
    scenario_rows: list[dict[str, object]] = []
    for hazard_name, threshold in HAZARD_SCENARIOS:
        class_eligible = damage["Maximum Intersecting Evidence Class"].ge(
            threshold
        ).fillna(False)
        for closure_name, grades in CLOSURE_RULES:
            closure_eligible = class_eligible & damage[
                "CEMS Damage Grade"
            ].isin(grades)
            closed_edge_ids = damage.loc[closure_eligible, "Edge ID"].astype(int)
            closed_edges = np.zeros(maximum_edge_id + 1, dtype=bool)
            closed_edges[closed_edge_ids.to_numpy()] = True
            closed_length_km = float(
                edges_all.loc[
                    edges_all["Edge ID"].isin(closed_edge_ids),
                    "Edge length (m)",
                ].sum()
                / 1000
            )
            for facility_rule, remove_exposed in FACILITY_RULES:
                sources, removed_facilities = service_nodes(
                    facilities,
                    facility_exposure,
                    threshold,
                    remove_exposed,
                )
                post_distances = dijkstra(adjacency, sources, closed_edges)
                post_minutes = post_distances[settlement_nodes]
                post_reachable = on_network & np.isfinite(post_minutes)
                newly_isolated = baseline_eligible & ~post_reachable
                finite_comparison = baseline_eligible & post_reachable
                accessibility_loss = np.full(len(settlements), np.nan)
                accessibility_loss[finite_comparison] = (
                    post_minutes[finite_comparison]
                    - baseline_minutes[finite_comparison]
                )
                delayed_over_five = finite_comparison & (
                    accessibility_loss > DELAY_THRESHOLD_MINUTES
                )
                scenario_id = (
                    f"H{threshold}_"
                    f"{'destroyed' if closure_name == 'Destroyed only' else 'all_candidate'}_"
                    f"{'facility_loss' if remove_exposed else 'roads_only'}"
                )
                for index, settlement in settlements.iterrows():
                    eligible = bool(baseline_eligible[index])
                    reachable = bool(post_reachable[index]) if eligible else False
                    settlement_rows.append(
                        {
                            "Scenario ID": scenario_id,
                            "Hazard Scenario": hazard_name,
                            "Minimum Evidence Class": threshold,
                            "Road Closure Rule": closure_name,
                            "Facility Availability Rule": facility_rule,
                            "Topology Repair Threshold (m)": PRIMARY_TOPOLOGY_THRESHOLD_M,
                            "Maximum Settlement Snap Distance (m)": MAX_SETTLEMENT_SNAP_M,
                            "OSM Settlement ID": settlement["OSM settlement ID"],
                            "Settlement Name": settlement["Settlement name"],
                            "Place Type": settlement["Place type"],
                            "Settlement-to-Road Snap Distance (m)": settlement[
                                "Settlement-to-road snap distance (m)"
                            ],
                            "Baseline Eligible": eligible,
                            "Baseline Health/Emergency Accessibility (minutes)": (
                                float(baseline_minutes[index]) if eligible else np.nan
                            ),
                            "Post-Disruption Service Reachable": (
                                reachable if eligible else pd.NA
                            ),
                            "Post-Disruption Travel Time (minutes)": (
                                float(post_minutes[index])
                                if eligible and reachable
                                else np.nan
                            ),
                            "Accessibility Loss (minutes)": (
                                float(accessibility_loss[index])
                                if finite_comparison[index]
                                else np.nan
                            ),
                            "Newly Isolated": (
                                bool(newly_isolated[index]) if eligible else pd.NA
                            ),
                            "Accessibility Loss Is Infinite": (
                                bool(newly_isolated[index]) if eligible else pd.NA
                            ),
                            "Accessibility Status": (
                                "baseline ineligible"
                                if not eligible
                                else (
                                    "newly isolated"
                                    if newly_isolated[index]
                                    else (
                                        "delay over 5 minutes"
                                        if delayed_over_five[index]
                                        else "reachable with limited change"
                                    )
                                )
                            ),
                        }
                    )
                finite_losses = accessibility_loss[finite_comparison]
                positive_losses = finite_losses[finite_losses > 1e-8]
                scenario_rows.append(
                    {
                        "Scenario ID": scenario_id,
                        "Hazard Scenario": hazard_name,
                        "Minimum Evidence Class": threshold,
                        "Road Closure Rule": closure_name,
                        "Facility Availability Rule": facility_rule,
                        "Topology Repair Threshold (m)": PRIMARY_TOPOLOGY_THRESHOLD_M,
                        "Maximum Settlement Snap Distance (m)": MAX_SETTLEMENT_SNAP_M,
                        "Closed Graph Edges": int(len(closed_edge_ids)),
                        "Closed Edge Length (km)": closed_length_km,
                        "Removed Health/Emergency Destinations": removed_facilities,
                        "Baseline Eligible Settlements": int(baseline_eligible.sum()),
                        "Post-Disruption Reachable Settlements": int(
                            (baseline_eligible & post_reachable).sum()
                        ),
                        "Newly Isolated Settlements": int(newly_isolated.sum()),
                        "Settlements Delayed over 5 Minutes": int(
                            delayed_over_five.sum()
                        ),
                        "Settlements with Positive Accessibility Loss": int(
                            positive_losses.size
                        ),
                        "Median Finite Accessibility Loss (minutes)": (
                            float(np.median(finite_losses))
                            if finite_losses.size
                            else np.nan
                        ),
                        "Median Positive Accessibility Loss (minutes)": (
                            float(np.median(positive_losses))
                            if positive_losses.size
                            else np.nan
                        ),
                        "P90 Positive Accessibility Loss (minutes)": (
                            float(np.quantile(positive_losses, 0.9))
                            if positive_losses.size
                            else np.nan
                        ),
                        "Maximum Finite Accessibility Loss (minutes)": (
                            float(np.max(finite_losses))
                            if finite_losses.size
                            else np.nan
                        ),
                        "Interpretation": (
                            "modeled scenario; closures and facility availability are not field confirmed"
                        ),
                    }
                )

    settlement_output = pd.DataFrame(settlement_rows)
    for column in (
        "Post-Disruption Service Reachable",
        "Newly Isolated",
        "Accessibility Loss Is Infinite",
    ):
        settlement_output[column] = settlement_output[column].astype("boolean")
    scenario_output = pd.DataFrame(scenario_rows)

    settlement_path_out = root / OUTPUT_SETTLEMENTS
    scenario_path_out = root / OUTPUT_SCENARIOS
    settlement_path_out.parent.mkdir(parents=True, exist_ok=True)
    settlement_output.to_parquet(settlement_path_out, index=False)
    scenario_output.to_parquet(scenario_path_out, index=False)
    scenario_csv = root / OUTPUT_SCENARIOS_CSV
    scenario_csv.parent.mkdir(parents=True, exist_ok=True)
    scenario_output.to_csv(scenario_csv, index=False)

    audit_rows = [
        {
            "measure": "Primary-topology graph nodes",
            "value": len(nodes),
            "status": "validated",
        },
        {
            "measure": "Primary-topology graph edges",
            "value": len(edges),
            "status": "minimum repair threshold at most 5 m",
        },
        {
            "measure": "Health/emergency destination records",
            "value": int(
                facilities["Included health/emergency destination"].sum()
            ),
            "status": "within 3 km of road graph",
        },
        {
            "measure": "Unique baseline service nodes",
            "value": len(all_service_nodes),
            "status": "validated",
        },
        {
            "measure": "Baseline eligible settlements",
            "value": int(baseline_eligible.sum()),
            "status": "within 3 km and baseline reachable",
        },
        {
            "measure": "Baseline reachable mismatches",
            "value": reachable_mismatches,
            "status": "must equal zero",
        },
        {
            "measure": "Maximum baseline travel-time difference",
            "value": maximum_baseline_difference,
            "status": "minutes; must be at numerical precision",
        },
        {
            "measure": "Disruption scenarios",
            "value": len(scenario_output),
            "status": "3 hazard x 2 closure x 2 facility rules",
        },
    ]
    audit_path = root / AUDIT
    with audit_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    print(scenario_output.to_string(index=False))
    print(pd.DataFrame(audit_rows).to_string(index=False))
    print(
        {
            "settlements": str(settlement_path_out),
            "scenarios": str(scenario_path_out),
            "scenario_csv": str(scenario_csv),
            "audit": str(audit_path),
        }
    )


if __name__ == "__main__":
    main()
