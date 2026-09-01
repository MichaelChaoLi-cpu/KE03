#!/usr/bin/env python3
"""Build the pre-specified topology, snap, hazard, and disruption grid."""

from __future__ import annotations

import argparse
import gc
import heapq
import json
from pathlib import Path

import numpy as np
import pandas as pd


NETWORK_DIR = Path("data/processed/geospatial/network")
EXPOSURE_DIR = Path("data/processed/geospatial/exposure")
OUTPUT_DIR = Path("data/processed/geospatial/accessibility")
EXP_DIR = Path("data/exp/data-preprocessing")

TOPOLOGY_THRESHOLDS_M = (0, 5, 10, 20)
SNAP_THRESHOLDS_M = (500, 1_000, 2_000, 3_000)
HAZARD_SCENARIOS = (
    ("Primary conservative", 3),
    ("Alternative mapped or multisensor", 2),
    ("Sensitivity screening", 1),
)
CLOSURE_RULES = (
    ("Destroyed only", {"Destroyed"}, "destroyed"),
    (
        "All disruption candidates",
        {"Possibly damaged", "Damaged", "Destroyed"},
        "all_candidate",
    ),
)
FACILITY_RULES = (
    ("Road disruption only", False, "roads_only"),
    (
        "Road and directly exposed facility disruption",
        True,
        "facility_loss",
    ),
)
PRIMARY = (3, "Destroyed only", "Road disruption only", 5, 3_000)
DELAY_THRESHOLD_MINUTES = 5.0


def build_adjacency(
    node_count: int, edges: pd.DataFrame
) -> list[list[tuple[int, float, int]]]:
    adjacency: list[list[tuple[int, float, int]]] = [
        [] for _ in range(node_count)
    ]
    for edge_id, left, right, minutes in edges.itertuples(index=False, name=None):
        edge_id = int(edge_id)
        left = int(left)
        right = int(right)
        minutes = float(minutes)
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
    facilities: pd.DataFrame,
    facility_exposure: pd.DataFrame,
    threshold: int,
    remove_exposed: bool,
) -> tuple[set[int], int]:
    exposure = facility_exposure.set_index("OSM Facility ID")[
        "Direct Evidence Class"
    ]
    nodes: set[int] = set()
    removed = 0
    selected = facilities.loc[
        facilities["Included health/emergency destination"]
    ]
    for row in selected.itertuples(index=False, name=None):
        facility_id = str(row[0])
        direct_class = exposure.get(facility_id, pd.NA)
        is_exposed = (
            not pd.isna(direct_class) and int(direct_class) >= threshold
        )
        if remove_exposed and is_exposed:
            removed += 1
        else:
            nodes.add(int(row[3]))
    return nodes, removed


def scenario_identifier(
    hazard: int,
    closure_slug: str,
    facility_slug: str,
    topology: int,
    snap: int,
) -> str:
    return (
        f"H{hazard}_{closure_slug}_{facility_slug}_"
        f"r{topology}_t{snap}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    paths = {
        "nodes": root / NETWORK_DIR / "road_nodes_preprocessed.parquet",
        "edges": root / NETWORK_DIR / "road_edges_preprocessed.parquet",
        "settlements": root
        / NETWORK_DIR
        / "settlement_road_crosswalk_preprocessed.parquet",
        "facilities": root
        / NETWORK_DIR
        / "facility_road_crosswalk_preprocessed.parquet",
        "baseline": root
        / NETWORK_DIR
        / "settlement_baseline_accessibility_preprocessed.parquet",
        "damage": root
        / EXPOSURE_DIR
        / "road_damage_scenario_exposure_preprocessed.parquet",
        "facility_exposure": root
        / EXPOSURE_DIR
        / "facility_hazard_exposure_preprocessed.parquet",
    }
    for path in paths.values():
        if not path.exists():
            raise FileNotFoundError(path)

    nodes = pd.read_parquet(paths["nodes"])
    edges_all = pd.read_parquet(paths["edges"])
    settlements = pd.read_parquet(paths["settlements"])
    facilities = pd.read_parquet(paths["facilities"])
    baseline_saved = pd.read_parquet(paths["baseline"])
    damage = pd.read_parquet(paths["damage"])
    facility_exposure = pd.read_parquet(paths["facility_exposure"])

    node_ids = nodes["Road node ID"].to_numpy(dtype="int64")
    if not np.array_equal(node_ids, np.arange(len(nodes), dtype="int64")):
        raise RuntimeError("Road node identifiers are not contiguous zero-based IDs.")
    if settlements["OSM settlement ID"].duplicated().any():
        raise RuntimeError("Settlement crosswalk contains duplicate identifiers.")

    settlement_nodes = settlements["Nearest road node ID"].to_numpy(
        dtype="int64"
    )
    snap_distance = settlements[
        "Settlement-to-road snap distance (m)"
    ].to_numpy(dtype="float64")
    maximum_edge_id = int(edges_all["Edge ID"].max())
    detail_frames: list[pd.DataFrame] = []
    summary_rows: list[dict[str, object]] = []
    validation_rows: list[dict[str, object]] = []

    all_service_nodes, _ = service_nodes(
        facilities, facility_exposure, threshold=1, remove_exposed=False
    )

    for topology in TOPOLOGY_THRESHOLDS_M:
        edges = edges_all.loc[
            edges_all["Minimum topology repair threshold (m)"].le(topology),
            [
                "Edge ID",
                "From node ID",
                "To node ID",
                "Edge travel time (minutes)",
            ],
        ].copy()
        adjacency = build_adjacency(len(nodes), edges)
        no_closed_edges = np.zeros(maximum_edge_id + 1, dtype=bool)
        baseline_distances = dijkstra(
            adjacency, all_service_nodes, no_closed_edges
        )
        baseline_at_settlements = baseline_distances[settlement_nodes]

        saved = baseline_saved.loc[
            baseline_saved["Topology repair threshold (m)"].eq(topology)
        ].set_index("OSM settlement ID").reindex(
            settlements["OSM settlement ID"]
        )
        saved_minutes = saved[
            "Baseline health/emergency accessibility (minutes)"
        ].to_numpy(dtype="float64")
        finite_both = np.isfinite(saved_minutes) & np.isfinite(
            baseline_at_settlements
        )
        maximum_difference = (
            float(
                np.max(
                    np.abs(
                        saved_minutes[finite_both]
                        - baseline_at_settlements[finite_both]
                    )
                )
            )
            if finite_both.any()
            else 0.0
        )
        expected_reachable = saved[
            "Baseline service reachable"
        ].fillna(False).to_numpy(dtype=bool)
        computed_reachable = (
            (snap_distance <= 3_000)
            & np.isfinite(baseline_at_settlements)
        )
        mismatch_count = int(
            np.count_nonzero(expected_reachable != computed_reachable)
        )
        if maximum_difference > 1e-8 or mismatch_count:
            raise RuntimeError(
                "Baseline validation failed for topology "
                f"{topology}: max difference={maximum_difference}, "
                f"reachable mismatches={mismatch_count}."
            )
        validation_rows.append(
            {
                "Topology Repair Threshold (m)": topology,
                "Included Graph Edges": len(edges),
                "Maximum Baseline Difference (minutes)": maximum_difference,
                "Baseline Reachable Mismatches": mismatch_count,
            }
        )

        for hazard_name, threshold in HAZARD_SCENARIOS:
            class_eligible = damage[
                "Maximum Intersecting Evidence Class"
            ].ge(threshold).fillna(False)
            for closure_name, grades, closure_slug in CLOSURE_RULES:
                closure_eligible = (
                    class_eligible
                    & damage["CEMS Damage Grade"].isin(grades)
                )
                closed_edge_ids = damage.loc[
                    closure_eligible, "Edge ID"
                ].astype("int64")
                closed_edge_ids = closed_edge_ids[
                    closed_edge_ids.isin(edges["Edge ID"])
                ].drop_duplicates()
                closed_edges = np.zeros(maximum_edge_id + 1, dtype=bool)
                closed_edges[closed_edge_ids.to_numpy()] = True
                closed_length_km = float(
                    edges_all.loc[
                        edges_all["Edge ID"].isin(closed_edge_ids),
                        "Edge length (m)",
                    ].sum()
                    / 1_000
                )
                for (
                    facility_rule,
                    remove_exposed,
                    facility_slug,
                ) in FACILITY_RULES:
                    sources, removed_facilities = service_nodes(
                        facilities,
                        facility_exposure,
                        threshold,
                        remove_exposed,
                    )
                    post_distances = dijkstra(
                        adjacency, sources, closed_edges
                    )
                    post_at_settlements = post_distances[settlement_nodes]

                    for snap in SNAP_THRESHOLDS_M:
                        on_network = snap_distance <= snap
                        baseline_eligible = on_network & np.isfinite(
                            baseline_at_settlements
                        )
                        post_reachable = on_network & np.isfinite(
                            post_at_settlements
                        )
                        newly_isolated = baseline_eligible & ~post_reachable
                        finite_comparison = baseline_eligible & post_reachable
                        accessibility_loss = np.full(
                            len(settlements), np.nan, dtype="float64"
                        )
                        accessibility_loss[finite_comparison] = (
                            post_at_settlements[finite_comparison]
                            - baseline_at_settlements[finite_comparison]
                        )
                        accessibility_loss[
                            np.isclose(accessibility_loss, 0.0, atol=1e-10)
                        ] = 0.0
                        delayed = finite_comparison & (
                            accessibility_loss > DELAY_THRESHOLD_MINUTES
                        )
                        positive_loss = finite_comparison & (
                            accessibility_loss > 1e-8
                        )
                        scenario_id = scenario_identifier(
                            threshold,
                            closure_slug,
                            facility_slug,
                            topology,
                            snap,
                        )
                        primary = (
                            threshold,
                            closure_name,
                            facility_rule,
                            topology,
                            snap,
                        ) == PRIMARY

                        detail = pd.DataFrame(
                            {
                                "Scenario ID": scenario_id,
                                "Primary Scenario": primary,
                                "Hazard Scenario": hazard_name,
                                "Minimum Evidence Class": threshold,
                                "Road Closure Rule": closure_name,
                                "Facility Availability Rule": facility_rule,
                                "Topology Repair Threshold (m)": topology,
                                "Maximum Settlement Snap Distance (m)": snap,
                                "OSM Settlement ID": settlements[
                                    "OSM settlement ID"
                                ].to_numpy(),
                                "Settlement Name": settlements[
                                    "Settlement name"
                                ].to_numpy(),
                                "Place Type": settlements[
                                    "Place type"
                                ].to_numpy(),
                                "Settlement-to-Road Snap Distance (m)": snap_distance,
                                "Baseline Eligible": baseline_eligible,
                                "Baseline Health/Emergency Accessibility (minutes)": np.where(
                                    baseline_eligible,
                                    baseline_at_settlements,
                                    np.nan,
                                ),
                                "Post-Disruption Service Reachable": pd.array(
                                    np.where(
                                        baseline_eligible,
                                        post_reachable,
                                        pd.NA,
                                    ),
                                    dtype="boolean",
                                ),
                                "Post-Disruption Travel Time (minutes)": np.where(
                                    finite_comparison,
                                    post_at_settlements,
                                    np.nan,
                                ),
                                "Accessibility Loss (minutes)": accessibility_loss,
                                "Newly Isolated": pd.array(
                                    np.where(
                                        baseline_eligible,
                                        newly_isolated,
                                        pd.NA,
                                    ),
                                    dtype="boolean",
                                ),
                                "Accessibility Loss Is Infinite": pd.array(
                                    np.where(
                                        baseline_eligible,
                                        newly_isolated,
                                        pd.NA,
                                    ),
                                    dtype="boolean",
                                ),
                                "Accessibility Status": np.select(
                                    [
                                        ~baseline_eligible,
                                        newly_isolated,
                                        delayed,
                                    ],
                                    [
                                        "baseline ineligible",
                                        "newly isolated",
                                        "delay over 5 minutes",
                                    ],
                                    default="reachable with limited change",
                                ),
                            }
                        )
                        detail_frames.append(detail)

                        finite_losses = accessibility_loss[
                            finite_comparison
                        ]
                        positive_losses = accessibility_loss[positive_loss]
                        summary_rows.append(
                            {
                                "Scenario ID": scenario_id,
                                "Primary Scenario": primary,
                                "Hazard Scenario": hazard_name,
                                "Minimum Evidence Class": threshold,
                                "Road Closure Rule": closure_name,
                                "Facility Availability Rule": facility_rule,
                                "Topology Repair Threshold (m)": topology,
                                "Maximum Settlement Snap Distance (m)": snap,
                                "Closed Graph Edges": len(closed_edge_ids),
                                "Closed Edge Length (km)": closed_length_km,
                                "Removed Health/Emergency Destinations": removed_facilities,
                                "Baseline Eligible Settlements": int(
                                    baseline_eligible.sum()
                                ),
                                "Post-Disruption Reachable Settlements": int(
                                    (baseline_eligible & post_reachable).sum()
                                ),
                                "Newly Isolated Settlements": int(
                                    newly_isolated.sum()
                                ),
                                "Settlements Delayed over 5 Minutes": int(
                                    delayed.sum()
                                ),
                                "Settlements with Positive Accessibility Loss": int(
                                    positive_loss.sum()
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
                                "Maximum Finite Accessibility Loss (minutes)": (
                                    float(np.max(finite_losses))
                                    if finite_losses.size
                                    else np.nan
                                ),
                            }
                        )

        del adjacency
        gc.collect()

    detail_output = pd.concat(detail_frames, ignore_index=True)
    summary_output = pd.DataFrame(summary_rows)
    if len(summary_output) != 192:
        raise RuntimeError(
            f"Expected 192 scenarios, generated {len(summary_output)}."
        )
    expected_detail_rows = len(settlements) * len(summary_output)
    if len(detail_output) != expected_detail_rows:
        raise RuntimeError(
            f"Expected {expected_detail_rows} detail rows, generated "
            f"{len(detail_output)}."
        )
    if int(summary_output["Primary Scenario"].sum()) != 1:
        raise RuntimeError("The scenario grid must contain exactly one primary scenario.")
    if any(not str(column).isascii() for column in detail_output.columns):
        raise RuntimeError("Non-ASCII output column detected.")

    output_dir = root / OUTPUT_DIR
    exp_dir = root / EXP_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    exp_dir.mkdir(parents=True, exist_ok=True)
    detail_path = (
        output_dir
        / "settlement_disruption_accessibility_robustness_preprocessed.parquet"
    )
    summary_path = (
        output_dir
        / "accessibility_robustness_scenario_summary_preprocessed.parquet"
    )
    audit_path = exp_dir / "accessibility_robustness_grid_audit.csv"
    decisions_path = exp_dir / "accessibility_robustness_grid_decisions.json"
    detail_output.to_parquet(detail_path, index=False)
    summary_output.to_parquet(summary_path, index=False)
    pd.DataFrame(validation_rows).to_csv(audit_path, index=False)
    decisions = {
        "status": "confirmed_in_anasop_sections_5_to_7",
        "scenario_dimensions": {
            "minimum_hazard_evidence_class": list(
                reversed([row[1] for row in HAZARD_SCENARIOS])
            ),
            "road_closure_rule": [row[0] for row in CLOSURE_RULES],
            "facility_availability_rule": [
                row[0] for row in FACILITY_RULES
            ],
            "topology_repair_threshold_m": list(TOPOLOGY_THRESHOLDS_M),
            "maximum_settlement_snap_distance_m": list(SNAP_THRESHOLDS_M),
        },
        "primary_scenario": {
            "minimum_hazard_evidence_class": PRIMARY[0],
            "road_closure_rule": PRIMARY[1],
            "facility_availability_rule": PRIMARY[2],
            "topology_repair_threshold_m": PRIMARY[3],
            "maximum_settlement_snap_distance_m": PRIMARY[4],
        },
        "interpretation_limits": [
            "modeled closures are not field-confirmed closures",
            "directly exposed facilities are not confirmed failed facilities",
            "snap and topology thresholds are structural robustness assumptions",
        ],
    }
    decisions_path.write_text(
        json.dumps(decisions, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(
        {
            "scenario_rows": len(summary_output),
            "settlement_rows": len(detail_output),
            "primary_scenario_id": summary_output.loc[
                summary_output["Primary Scenario"], "Scenario ID"
            ].iloc[0],
            "detail": str(detail_path),
            "summary": str(summary_path),
            "audit": str(audit_path),
            "decisions": str(decisions_path),
        }
    )


if __name__ == "__main__":
    main()
