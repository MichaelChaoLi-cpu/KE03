#!/usr/bin/env python3
"""Build count-constrained road-repair portfolios and robustness outputs."""

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
ACCESSIBILITY_DIR = Path("data/processed/geospatial/accessibility")
POPULATION_DIR = Path("data/processed/geospatial/population")
DECISION_DIR = Path("data/processed/decision")
EXP_DIR = Path("data/exp/data-preprocessing")

PRIMARY_TOPOLOGY_THRESHOLD_M = 5
PRIMARY_SNAP_DISTANCE_M = 3_000
PRIMARY_EVIDENCE_CLASS = 3
PRIMARY_DAMAGE_GRADES = {"Destroyed"}
REPORT_PORTFOLIO_SIZES = (1, 2, 3, 5)
MAX_FORWARD_STEPS = max(REPORT_PORTFOLIO_SIZES)
TOLERANCE = 1e-8


def build_adjacency(
    node_count: int, edges: pd.DataFrame
) -> list[list[tuple[int, float, int]]]:
    adjacency: list[list[tuple[int, float, int]]] = [
        [] for _ in range(node_count)
    ]
    for edge_id, left, right, minutes in edges.itertuples(
        index=False, name=None
    ):
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


def update_after_reopening(
    adjacency: list[list[tuple[int, float, int]]],
    previous_distances: np.ndarray,
    updated_closed_edges: np.ndarray,
    reopened_edge_ids: np.ndarray,
    edge_from: np.ndarray,
    edge_to: np.ndarray,
    edge_minutes: np.ndarray,
) -> np.ndarray:
    """Update shortest paths after reopening edges without a full restart."""
    distances = previous_distances.copy()
    queue: list[tuple[float, int]] = []
    for edge_id in reopened_edge_ids:
        edge_id = int(edge_id)
        left = int(edge_from[edge_id])
        right = int(edge_to[edge_id])
        cost = float(edge_minutes[edge_id])
        left_to_right = distances[left] + cost
        if left_to_right < distances[right]:
            distances[right] = left_to_right
            heapq.heappush(queue, (left_to_right, right))
        right_to_left = distances[right] + cost
        if right_to_left < distances[left]:
            distances[left] = right_to_left
            heapq.heappush(queue, (right_to_left, left))
    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbour, cost, edge_id in adjacency[node]:
            if updated_closed_edges[edge_id]:
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
) -> set[int]:
    direct_class = facility_exposure.assign(
        **{"OSM Facility ID": facility_exposure["OSM Facility ID"].astype(str)}
    ).set_index("OSM Facility ID")["Direct Evidence Class"]
    selected = facilities.loc[
        facilities["Included health/emergency destination"]
    ]
    nodes: set[int] = set()
    for _, row in selected.iterrows():
        facility_id = str(row["OSM facility ID"])
        evidence_class = direct_class.get(facility_id, pd.NA)
        exposed = (
            not pd.isna(evidence_class) and int(evidence_class) >= threshold
        )
        if not (remove_exposed and exposed):
            nodes.add(int(row["Nearest road node ID"]))
    if not nodes:
        raise RuntimeError("A scenario removed every health/emergency destination.")
    return nodes


def portfolio_metrics(
    original_post_at_settlements: np.ndarray,
    repaired_at_settlements: np.ndarray,
    baseline_eligible: np.ndarray,
    newly_isolated: np.ndarray,
    population: np.ndarray,
) -> dict[str, float | int | bool]:
    repaired_reachable = baseline_eligible & np.isfinite(
        repaired_at_settlements
    )
    restored = newly_isolated & repaired_reachable
    finite_comparison = (
        baseline_eligible
        & np.isfinite(original_post_at_settlements)
        & np.isfinite(repaired_at_settlements)
    )
    improvement = np.full(len(population), np.nan, dtype="float64")
    improvement[finite_comparison] = (
        original_post_at_settlements[finite_comparison]
        - repaired_at_settlements[finite_comparison]
    )
    minimum_improvement = float(
        np.nanmin(improvement, initial=0.0)
    )
    if minimum_improvement < -TOLERANCE:
        raise RuntimeError(
            "A road-repair portfolio worsened a finite shortest path: "
            f"minimum improvement={minimum_improvement}."
        )
    improvement = np.where(
        np.isfinite(improvement), np.maximum(improvement, 0.0), np.nan
    )
    positive_finite = np.isfinite(improvement) & (improvement > TOLERANCE)
    reconnected_population = float(population[restored].sum())
    person_minutes = float(
        np.nansum(population[positive_finite] * improvement[positive_finite])
    )
    return {
        "Settlements Reconnected by Portfolio": int(restored.sum()),
        "Portfolio Population Reconnected": reconnected_population,
        "Settlements with Finite Improvement from Portfolio": int(
            positive_finite.sum()
        ),
        "Population with Finite Improvement from Portfolio": float(
            population[positive_finite].sum()
        ),
        "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)": person_minutes,
        "Portfolio Retains Positive Benefit": bool(
            reconnected_population > TOLERANCE or person_minutes > TOLERANCE
        ),
    }


def path_inputs(root: Path) -> dict[str, Path]:
    return {
        "nodes": root / NETWORK_DIR / "road_nodes_preprocessed.parquet",
        "edges": root / NETWORK_DIR / "road_edges_preprocessed.parquet",
        "settlements": root
        / NETWORK_DIR
        / "settlement_road_crosswalk_preprocessed.parquet",
        "facilities": root
        / NETWORK_DIR
        / "facility_road_crosswalk_preprocessed.parquet",
        "damage": root
        / EXPOSURE_DIR
        / "road_damage_scenario_exposure_preprocessed.parquet",
        "facility_exposure": root
        / EXPOSURE_DIR
        / "facility_hazard_exposure_preprocessed.parquet",
        "accessibility": root
        / ACCESSIBILITY_DIR
        / "settlement_disruption_accessibility_robustness_preprocessed.parquet",
        "population": root
        / POPULATION_DIR
        / "settlement_population_allocation_preprocessed.parquet",
        "candidates": root
        / DECISION_DIR
        / "road_repair_candidate_benefits_preprocessed.parquet",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    paths = path_inputs(root)
    for path in paths.values():
        if not path.exists():
            raise FileNotFoundError(path)

    nodes = pd.read_parquet(paths["nodes"])
    edges_all = pd.read_parquet(paths["edges"])
    settlements = pd.read_parquet(paths["settlements"])
    facilities = pd.read_parquet(paths["facilities"])
    damage = pd.read_parquet(paths["damage"])
    facility_exposure = pd.read_parquet(paths["facility_exposure"])
    accessibility = pd.read_parquet(paths["accessibility"])
    population_table = pd.read_parquet(paths["population"])
    candidates = pd.read_parquet(paths["candidates"])

    node_ids = nodes["Road node ID"].to_numpy(dtype="int64")
    if not np.array_equal(node_ids, np.arange(len(nodes), dtype="int64")):
        raise RuntimeError("Road node IDs are not contiguous zero-based values.")
    if settlements["OSM settlement ID"].duplicated().any():
        raise RuntimeError("Settlement crosswalk has duplicate IDs.")
    if candidates["Road Repair Candidate ID"].duplicated().any():
        raise RuntimeError("Road-repair candidate IDs are not unique.")

    maximum_edge_id = int(edges_all["Edge ID"].max())
    edge_from = np.full(maximum_edge_id + 1, -1, dtype="int64")
    edge_to = np.full(maximum_edge_id + 1, -1, dtype="int64")
    edge_minutes = np.full(maximum_edge_id + 1, np.nan, dtype="float64")
    all_edge_ids = edges_all["Edge ID"].to_numpy(dtype="int64")
    edge_from[all_edge_ids] = edges_all["From node ID"].to_numpy(dtype="int64")
    edge_to[all_edge_ids] = edges_all["To node ID"].to_numpy(dtype="int64")
    edge_minutes[all_edge_ids] = edges_all[
        "Edge travel time (minutes)"
    ].to_numpy(dtype="float64")

    settlement_ids = settlements["OSM settlement ID"].astype(str)
    settlement_nodes = settlements["Nearest road node ID"].to_numpy(
        dtype="int64"
    )
    population_join = population_table.assign(
        **{"OSM Settlement ID": population_table["OSM Settlement ID"].astype(str)}
    ).set_index("OSM Settlement ID").reindex(settlement_ids)
    if population_join["Estimated Settlement Population"].isna().any():
        raise RuntimeError("Settlement population inputs are incomplete.")
    settlement_population = population_join[
        "Estimated Settlement Population"
    ].to_numpy(dtype="float64")

    primary_edges = edges_all.loc[
        edges_all["Minimum topology repair threshold (m)"].le(
            PRIMARY_TOPOLOGY_THRESHOLD_M
        ),
        [
            "Edge ID",
            "From node ID",
            "To node ID",
            "Edge travel time (minutes)",
        ],
    ].copy()
    primary_edge_ids = set(primary_edges["Edge ID"].astype(int))
    primary_damage = damage.loc[
        damage["Maximum Intersecting Evidence Class"].ge(
            PRIMARY_EVIDENCE_CLASS
        )
        & damage["CEMS Damage Grade"].isin(PRIMARY_DAMAGE_GRADES)
        & damage["Edge ID"].isin(primary_edge_ids)
    ].copy()
    if primary_damage["Edge ID"].duplicated().any():
        raise RuntimeError("Primary damaged-edge inputs contain duplicates.")
    candidate_edge_groups = {
        f"OSM-{str(osm_id)}": group["Edge ID"]
        .astype("int64")
        .drop_duplicates()
        .to_numpy()
        for osm_id, group in primary_damage.groupby(
            "OSM Feature ID", sort=True, dropna=False
        )
    }
    if set(candidate_edge_groups) != set(
        candidates["Road Repair Candidate ID"].astype(str)
    ):
        raise RuntimeError("Candidate table and primary edge groups disagree.")

    candidate_info = candidates.assign(
        **{
            "Road Repair Candidate ID": candidates[
                "Road Repair Candidate ID"
            ].astype(str)
        }
    ).set_index("Road Repair Candidate ID")
    candidate_order = sorted(candidate_edge_groups)
    primary_adjacency = build_adjacency(len(nodes), primary_edges)
    primary_closed = np.zeros(maximum_edge_id + 1, dtype=bool)
    primary_closed[primary_damage["Edge ID"].to_numpy(dtype="int64")] = True
    all_primary_sources = service_nodes(
        facilities, facility_exposure, PRIMARY_EVIDENCE_CLASS, False
    )
    primary_post = dijkstra(
        primary_adjacency, all_primary_sources, primary_closed
    )
    primary_post_settlements = primary_post[settlement_nodes]

    saved_primary = accessibility.loc[
        accessibility["Primary Scenario"]
    ].assign(
        **{
            "OSM Settlement ID": accessibility.loc[
                accessibility["Primary Scenario"], "OSM Settlement ID"
            ].astype(str)
        }
    ).set_index("OSM Settlement ID").reindex(settlement_ids)
    if len(saved_primary) != len(settlements):
        raise RuntimeError("Primary accessibility scenario is incomplete.")
    baseline_eligible = saved_primary["Baseline Eligible"].fillna(False).to_numpy(
        dtype=bool
    )
    newly_isolated = saved_primary["Newly Isolated"].fillna(False).to_numpy(
        dtype=bool
    )
    saved_reachable = saved_primary[
        "Post-Disruption Service Reachable"
    ].fillna(False).to_numpy(dtype=bool)
    computed_reachable = baseline_eligible & np.isfinite(
        primary_post_settlements
    )
    primary_reachable_mismatches = int(
        np.count_nonzero(computed_reachable != (baseline_eligible & saved_reachable))
    )
    if primary_reachable_mismatches:
        raise RuntimeError(
            "Primary disruption reachability does not reproduce the saved grid."
        )

    selected_ids: list[str] = []
    current_closed = primary_closed.copy()
    current_distances = primary_post.copy()
    selection_rows: list[dict[str, object]] = []
    previous_reconnected = -np.inf
    previous_improvement = -np.inf
    for step in range(1, MAX_FORWARD_STEPS + 1):
        best_id: str | None = None
        best_key: tuple[float, float, float] | None = None
        best_distances: np.ndarray | None = None
        best_closed: np.ndarray | None = None
        best_metrics: dict[str, float | int | bool] | None = None
        remaining = [item for item in candidate_order if item not in selected_ids]
        for candidate_number, candidate_id in enumerate(remaining, start=1):
            group_edges = candidate_edge_groups[candidate_id]
            reopened = group_edges[current_closed[group_edges]]
            trial_closed = current_closed.copy()
            trial_closed[reopened] = False
            trial_distances = update_after_reopening(
                primary_adjacency,
                current_distances,
                trial_closed,
                reopened,
                edge_from,
                edge_to,
                edge_minutes,
            )
            metrics = portfolio_metrics(
                primary_post_settlements,
                trial_distances[settlement_nodes],
                baseline_eligible,
                newly_isolated,
                settlement_population,
            )
            key = (
                float(metrics["Portfolio Population Reconnected"]),
                float(
                    metrics[
                        "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)"
                    ]
                ),
                -float(candidate_info.loc[candidate_id, "Repair Section Length (m)"]),
            )
            if best_key is None or key > best_key:
                best_id = candidate_id
                best_key = key
                best_distances = trial_distances
                best_closed = trial_closed
                best_metrics = metrics
            if candidate_number % 50 == 0 or candidate_number == len(remaining):
                print(
                    f"Forward step {step}: evaluated {candidate_number}/{len(remaining)} candidates",
                    flush=True,
                )
        if (
            best_id is None
            or best_distances is None
            or best_closed is None
            or best_metrics is None
        ):
            raise RuntimeError("Forward selection failed to identify a candidate.")
        selected_ids.append(best_id)
        current_distances = best_distances
        current_closed = best_closed
        reconnected = float(best_metrics["Portfolio Population Reconnected"])
        improvement = float(
            best_metrics[
                "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)"
            ]
        )
        if (
            reconnected + TOLERANCE < previous_reconnected
            or improvement + TOLERANCE < previous_improvement
        ):
            raise RuntimeError("Forward portfolio benefits are not monotone.")
        previous_reconnected = reconnected
        previous_improvement = improvement
        selection_rows.append(
            {
                "Forward Selection Step": step,
                "Selected Road Repair Candidate ID": best_id,
                "Selected Critical Road Section": candidate_info.loc[
                    best_id, "Critical Road Section"
                ],
                "Selected Repair Section Length (m)": float(
                    candidate_info.loc[best_id, "Repair Section Length (m)"]
                ),
                "Selected Road Repair Candidate IDs": ";".join(selected_ids),
                "Selected Critical Road Sections": "; ".join(
                    str(candidate_info.loc[item, "Critical Road Section"])
                    for item in selected_ids
                ),
                "Cumulative Repair Section Length (m)": float(
                    candidate_info.loc[
                        selected_ids, "Repair Section Length (m)"
                    ].sum()
                ),
                **best_metrics,
            }
        )
        print(
            f"Selected step {step}: {best_id}; population reconnected={reconnected:.6f}; "
            f"finite improvement={improvement:.6f} person-minutes",
            flush=True,
        )

    selection = pd.DataFrame(selection_rows)
    expected_first = str(
        candidates.sort_values("Primary Repair Benefit Rank").iloc[0][
            "Road Repair Candidate ID"
        ]
    )
    first_candidate_matches_marginal = selected_ids[0] == expected_first
    if not first_candidate_matches_marginal:
        raise RuntimeError(
            "The first forward candidate does not match the validated marginal ranking."
        )
    full_k5 = dijkstra(primary_adjacency, all_primary_sources, current_closed)
    finite_both = np.isfinite(full_k5) & np.isfinite(current_distances)
    k5_reachability_mismatches = int(
        np.count_nonzero(np.isfinite(full_k5) != np.isfinite(current_distances))
    )
    k5_maximum_distance_difference = (
        float(np.max(np.abs(full_k5[finite_both] - current_distances[finite_both])))
        if finite_both.any()
        else 0.0
    )
    if k5_reachability_mismatches or k5_maximum_distance_difference > TOLERANCE:
        raise RuntimeError("Incremental shortest-path validation failed at K=5.")

    report_selection = selection.loc[
        selection["Forward Selection Step"].isin(REPORT_PORTFOLIO_SIZES)
    ].copy()
    selected_prefixes = {
        int(row["Forward Selection Step"]): str(
            row["Selected Road Repair Candidate IDs"]
        ).split(";")
        for _, row in report_selection.iterrows()
    }

    del primary_adjacency, full_k5
    gc.collect()

    access_indexed = accessibility.assign(
        **{"OSM Settlement ID": accessibility["OSM Settlement ID"].astype(str)}
    ).set_index(["Scenario ID", "OSM Settlement ID"])
    scenario_metadata = accessibility[
        [
            "Scenario ID",
            "Primary Scenario",
            "Hazard Scenario",
            "Minimum Evidence Class",
            "Road Closure Rule",
            "Facility Availability Rule",
            "Topology Repair Threshold (m)",
            "Maximum Settlement Snap Distance (m)",
        ]
    ].drop_duplicates()
    if len(scenario_metadata) != 192:
        raise RuntimeError(
            f"Expected 192 structural scenarios, found {len(scenario_metadata)}."
        )

    base_columns = [
        "Hazard Scenario",
        "Minimum Evidence Class",
        "Road Closure Rule",
        "Facility Availability Rule",
        "Topology Repair Threshold (m)",
    ]
    scenario_rows: list[dict[str, object]] = []
    scenario_validation_mismatches = 0
    for topology in sorted(
        scenario_metadata["Topology Repair Threshold (m)"].unique()
    ):
        topology = int(topology)
        topology_edges = edges_all.loc[
            edges_all["Minimum topology repair threshold (m)"].le(topology),
            [
                "Edge ID",
                "From node ID",
                "To node ID",
                "Edge travel time (minutes)",
            ],
        ].copy()
        included_ids = set(topology_edges["Edge ID"].astype(int))
        adjacency = build_adjacency(len(nodes), topology_edges)
        topology_metadata = scenario_metadata.loc[
            scenario_metadata["Topology Repair Threshold (m)"].eq(topology)
        ]
        base_metadata = topology_metadata[base_columns].drop_duplicates()
        for base_number, (_, base) in enumerate(
            base_metadata.iterrows(), start=1
        ):
            threshold = int(base["Minimum Evidence Class"])
            if base["Road Closure Rule"] == "Destroyed only":
                grades = {"Destroyed"}
            elif base["Road Closure Rule"] == "All disruption candidates":
                grades = {"Possibly damaged", "Damaged", "Destroyed"}
            else:
                raise RuntimeError(
                    f"Unknown road closure rule: {base['Road Closure Rule']}"
                )
            remove_exposed = (
                base["Facility Availability Rule"]
                == "Road and directly exposed facility disruption"
            )
            closure_eligible = (
                damage["Maximum Intersecting Evidence Class"].ge(threshold)
                & damage["CEMS Damage Grade"].isin(grades)
                & damage["Edge ID"].isin(included_ids)
            )
            closed_ids = damage.loc[
                closure_eligible, "Edge ID"
            ].astype("int64").drop_duplicates().to_numpy()
            closed = np.zeros(maximum_edge_id + 1, dtype=bool)
            closed[closed_ids] = True
            sources = service_nodes(
                facilities, facility_exposure, threshold, remove_exposed
            )
            original_post = dijkstra(adjacency, sources, closed)
            original_post_settlements = original_post[settlement_nodes]

            matching = topology_metadata.loc[
                topology_metadata["Minimum Evidence Class"].eq(threshold)
                & topology_metadata["Road Closure Rule"].eq(
                    base["Road Closure Rule"]
                )
                & topology_metadata["Facility Availability Rule"].eq(
                    base["Facility Availability Rule"]
                )
            ].sort_values("Maximum Settlement Snap Distance (m)")
            for _, meta in matching.iterrows():
                saved = access_indexed.xs(
                    str(meta["Scenario ID"]), level="Scenario ID"
                ).reindex(settlement_ids)
                eligible = saved["Baseline Eligible"].fillna(False).to_numpy(
                    dtype=bool
                )
                expected = saved[
                    "Post-Disruption Service Reachable"
                ].fillna(False).to_numpy(dtype=bool)
                computed = eligible & np.isfinite(original_post_settlements)
                scenario_validation_mismatches += int(
                    np.count_nonzero(computed != (eligible & expected))
                )

            current_scenario_closed = closed.copy()
            current_scenario_distances = original_post.copy()
            for step, selected_id in enumerate(selected_ids, start=1):
                group_edges = candidate_edge_groups[selected_id]
                included_group = np.array(
                    [item for item in group_edges if int(item) in included_ids],
                    dtype="int64",
                )
                reopened = included_group[
                    current_scenario_closed[included_group]
                ]
                current_scenario_closed[reopened] = False
                current_scenario_distances = update_after_reopening(
                    adjacency,
                    current_scenario_distances,
                    current_scenario_closed,
                    reopened,
                    edge_from,
                    edge_to,
                    edge_minutes,
                )
                if step not in REPORT_PORTFOLIO_SIZES:
                    continue
                repaired_at_settlements = current_scenario_distances[
                    settlement_nodes
                ]
                prefix = selected_prefixes[step]
                for _, meta in matching.iterrows():
                    scenario_id = str(meta["Scenario ID"])
                    saved = access_indexed.xs(
                        scenario_id, level="Scenario ID"
                    ).reindex(settlement_ids)
                    eligible = saved["Baseline Eligible"].fillna(False).to_numpy(
                        dtype=bool
                    )
                    isolated = saved["Newly Isolated"].fillna(False).to_numpy(
                        dtype=bool
                    )
                    metrics = portfolio_metrics(
                        original_post_settlements,
                        repaired_at_settlements,
                        eligible,
                        isolated,
                        settlement_population,
                    )
                    scenario_rows.append(
                        {
                            "Scenario ID": scenario_id,
                            "Primary Scenario": bool(meta["Primary Scenario"]),
                            "Hazard Scenario": meta["Hazard Scenario"],
                            "Minimum Evidence Class": threshold,
                            "Road Closure Rule": base["Road Closure Rule"],
                            "Facility Availability Rule": base[
                                "Facility Availability Rule"
                            ],
                            "Topology Repair Threshold (m)": topology,
                            "Maximum Settlement Snap Distance (m)": int(
                                meta["Maximum Settlement Snap Distance (m)"]
                            ),
                            "Repair Portfolio Size (sections)": step,
                            "Selected Road Repair Candidate IDs": ";".join(prefix),
                            "Selected Critical Road Sections": "; ".join(
                                str(
                                    candidate_info.loc[
                                        item, "Critical Road Section"
                                    ]
                                )
                                for item in prefix
                            ),
                            "Cumulative Repair Section Length (m)": float(
                                candidate_info.loc[
                                    prefix, "Repair Section Length (m)"
                                ].sum()
                            ),
                            **metrics,
                            "Interpretation": (
                                "fixed primary forward-selection portfolio evaluated with joint rerouting; "
                                "modeled screening result, not an engineering or cost-optimal plan"
                            ),
                        }
                    )
            print(
                f"Topology {topology} m: completed base scenario "
                f"{base_number}/{len(base_metadata)}",
                flush=True,
            )
        del adjacency
        gc.collect()

    if scenario_validation_mismatches:
        raise RuntimeError(
            "Scenario routing did not reproduce saved accessibility reachability: "
            f"mismatches={scenario_validation_mismatches}."
        )
    scenario_output = pd.DataFrame(scenario_rows).sort_values(
        ["Repair Portfolio Size (sections)", "Scenario ID"]
    ).reset_index(drop=True)
    expected_rows = len(scenario_metadata) * len(REPORT_PORTFOLIO_SIZES)
    if len(scenario_output) != expected_rows:
        raise RuntimeError(
            f"Expected {expected_rows} portfolio-scenario rows, found "
            f"{len(scenario_output)}."
        )
    retention = scenario_output.groupby(
        "Repair Portfolio Size (sections)"
    )["Portfolio Retains Positive Benefit"].mean()
    scenario_output["Portfolio Structural-Scenario Retention"] = (
        scenario_output["Repair Portfolio Size (sections)"].map(retention)
    )

    summary_rows: list[dict[str, object]] = []
    for portfolio_size, group in scenario_output.groupby(
        "Repair Portfolio Size (sections)", sort=True
    ):
        primary = group.loc[group["Primary Scenario"]]
        if len(primary) != 1:
            raise RuntimeError(
                f"Portfolio K={portfolio_size} has {len(primary)} primary rows."
            )
        primary = primary.iloc[0]
        summary_rows.append(
            {
                "Repair Portfolio Size (sections)": int(portfolio_size),
                "Selected Road Repair Candidate IDs": primary[
                    "Selected Road Repair Candidate IDs"
                ],
                "Selected Critical Road Sections": primary[
                    "Selected Critical Road Sections"
                ],
                "Cumulative Repair Section Length (m)": primary[
                    "Cumulative Repair Section Length (m)"
                ],
                "Primary Portfolio Population Reconnected": primary[
                    "Portfolio Population Reconnected"
                ],
                "Primary Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)": primary[
                    "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)"
                ],
                "Minimum Scenario Population Reconnected": float(
                    group["Portfolio Population Reconnected"].min()
                ),
                "Median Scenario Population Reconnected": float(
                    group["Portfolio Population Reconnected"].median()
                ),
                "Maximum Scenario Population Reconnected": float(
                    group["Portfolio Population Reconnected"].max()
                ),
                "Minimum Scenario Finite Improvement (person-minutes)": float(
                    group[
                        "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)"
                    ].min()
                ),
                "Median Scenario Finite Improvement (person-minutes)": float(
                    group[
                        "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)"
                    ].median()
                ),
                "Maximum Scenario Finite Improvement (person-minutes)": float(
                    group[
                        "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)"
                    ].max()
                ),
                "Portfolio Structural-Scenario Retention": float(
                    retention.loc[portfolio_size]
                ),
                "Eligible Structural Scenarios": len(group),
                "Interpretation": (
                    "count-constrained joint-rerouting screening portfolio; "
                    "not globally optimal, cost-optimal, or engineering validated"
                ),
            }
        )
    summary = pd.DataFrame(summary_rows)

    if any(not str(column).isascii() for column in scenario_output.columns):
        raise RuntimeError("Non-ASCII scenario-output column detected.")
    if any(not str(column).isascii() for column in summary.columns):
        raise RuntimeError("Non-ASCII summary-output column detected.")
    if not summary["Repair Portfolio Size (sections)"].tolist() == list(
        REPORT_PORTFOLIO_SIZES
    ):
        raise RuntimeError("Portfolio summary sizes are incomplete or unordered.")

    output_dir = root / DECISION_DIR
    exp_dir = root / EXP_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    exp_dir.mkdir(parents=True, exist_ok=True)
    scenario_path = (
        output_dir / "road_repair_portfolio_scenarios_preprocessed.parquet"
    )
    summary_path = (
        output_dir / "road_repair_portfolio_summary_preprocessed.parquet"
    )
    audit_path = exp_dir / "road_repair_portfolio_audit.csv"
    decisions_path = exp_dir / "road_repair_portfolio_decisions.json"
    scenario_output.to_parquet(scenario_path, index=False)
    summary.to_parquet(summary_path, index=False)
    pd.DataFrame(
        [
            {
                "Measure": "Primary repair candidates",
                "Value": len(candidate_order),
                "Status": "non-overlapping OSM road-feature groups",
            },
            {
                "Measure": "Forward-selection steps",
                "Value": MAX_FORWARD_STEPS,
                "Status": "joint rerouting after every selected section",
            },
            {
                "Measure": "Reported portfolio sizes",
                "Value": ";".join(map(str, REPORT_PORTFOLIO_SIZES)),
                "Status": "confirmed by human",
            },
            {
                "Measure": "Structural scenarios",
                "Value": len(scenario_metadata),
                "Status": "complete pre-specified scenario grid",
            },
            {
                "Measure": "Portfolio-scenario rows",
                "Value": len(scenario_output),
                "Status": "four fixed primary portfolios per scenario",
            },
            {
                "Measure": "First candidate matches marginal ranking",
                "Value": first_candidate_matches_marginal,
                "Status": "must be true",
            },
            {
                "Measure": "Primary reachability mismatches",
                "Value": primary_reachable_mismatches,
                "Status": "must equal zero",
            },
            {
                "Measure": "Scenario reachability mismatches",
                "Value": scenario_validation_mismatches,
                "Status": "must equal zero",
            },
            {
                "Measure": "K=5 incremental/full reachability mismatches",
                "Value": k5_reachability_mismatches,
                "Status": "must equal zero",
            },
            {
                "Measure": "K=5 maximum incremental/full time difference",
                "Value": k5_maximum_distance_difference,
                "Status": "minutes; must be numerical precision",
            },
        ]
    ).to_csv(audit_path, index=False)
    decisions = {
        "status": "confirmed_by_human",
        "portfolio_sizes_sections": list(REPORT_PORTFOLIO_SIZES),
        "selection_method": (
            "forward selection by cumulative population reconnected, then cumulative finite "
            "population-weighted travel-time improvement, then shorter added section"
        ),
        "routing_rule": (
            "jointly reopen the selected primary candidate edge groups and rerun shortest paths; "
            "do not add single-section marginal benefits"
        ),
        "missing_and_transformation_rules": {
            "imputation": "none",
            "clipping": "none",
            "log_transformation": "none",
        },
        "robustness_rule": (
            "evaluate each fixed primary portfolio over all 192 structural scenarios and define "
            "retention as the share with positive reconnection or finite time-improvement benefit"
        ),
        "final_variables": [
            "Repair Portfolio Size (sections)",
            "Portfolio Population Reconnected",
            "Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)",
            "Portfolio Structural-Scenario Retention",
        ],
        "interpretation_limits": [
            "modeled screening output rather than a field-confirmed repair plan",
            "not globally optimal or cost-optimal",
            "no engineering feasibility, cost, duration, crew, or capacity evidence",
        ],
    }
    decisions_path.write_text(
        json.dumps(decisions, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(
        {
            "portfolio_scenarios": str(scenario_path),
            "portfolio_scenario_shape": scenario_output.shape,
            "portfolio_summary": str(summary_path),
            "portfolio_summary_shape": summary.shape,
            "audit": str(audit_path),
            "decisions": str(decisions_path),
        }
    )
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
