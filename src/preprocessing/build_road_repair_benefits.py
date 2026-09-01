#!/usr/bin/env python3
"""Estimate marginal access benefits from restoring one damaged road section."""

from __future__ import annotations

import argparse
import heapq
import json
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import LineString, MultiLineString


NETWORK_DIR = Path("data/processed/geospatial/network")
EXPOSURE = Path(
    "data/processed/geospatial/exposure/"
    "road_damage_scenario_exposure_preprocessed.parquet"
)
ACCESSIBILITY = Path(
    "data/processed/geospatial/accessibility/"
    "settlement_disruption_accessibility_robustness_preprocessed.parquet"
)
POPULATION = Path(
    "data/processed/geospatial/population/"
    "settlement_population_allocation_preprocessed.parquet"
)
OUTPUT_DIR = Path("data/processed/decision")
EXP_DIR = Path("data/exp/data-preprocessing")
PRIMARY_TOPOLOGY_THRESHOLD_M = 5
PRIMARY_SNAP_DISTANCE_M = 3_000
PRIMARY_EVIDENCE_CLASS = 3
PRIMARY_DAMAGE_GRADE = "Destroyed"
CRS = "EPSG:32645"


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


def first_nonmissing(values: pd.Series) -> str | None:
    nonmissing = values.dropna().astype(str)
    nonmissing = nonmissing.loc[nonmissing.str.strip().ne("")]
    return nonmissing.iloc[0] if not nonmissing.empty else None


def section_label(osm_feature_id: str, road_name: str | None, road_class: str) -> str:
    if road_name:
        return f"{road_name} (OSM {osm_feature_id})"
    return f"Unnamed {road_class} road (OSM {osm_feature_id})"


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
        "damage": root / EXPOSURE,
        "accessibility": root / ACCESSIBILITY,
        "population": root / POPULATION,
    }
    for path in paths.values():
        if not path.exists():
            raise FileNotFoundError(path)

    nodes = pd.read_parquet(paths["nodes"])
    edges_all = pd.read_parquet(paths["edges"])
    settlements = pd.read_parquet(paths["settlements"])
    facilities = pd.read_parquet(paths["facilities"])
    damage = pd.read_parquet(paths["damage"])
    accessibility = pd.read_parquet(paths["accessibility"])
    population = pd.read_parquet(paths["population"])

    node_ids = nodes["Road node ID"].to_numpy(dtype="int64")
    if not np.array_equal(node_ids, np.arange(len(nodes), dtype="int64")):
        raise RuntimeError("Road node identifiers are not contiguous zero-based IDs.")
    if population["OSM Settlement ID"].duplicated().any():
        raise RuntimeError("Settlement population table contains duplicate IDs.")

    edges = edges_all.loc[
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
    included_edge_ids = set(edges["Edge ID"].astype(int))
    primary_damage = damage.loc[
        damage["Maximum Intersecting Evidence Class"].ge(
            PRIMARY_EVIDENCE_CLASS
        )
        & damage["CEMS Damage Grade"].eq(PRIMARY_DAMAGE_GRADE)
        & damage["Edge ID"].isin(included_edge_ids)
    ].copy()
    if primary_damage["Edge ID"].duplicated().any():
        raise RuntimeError("Primary damaged-edge table contains duplicate edge IDs.")
    if primary_damage.empty:
        raise RuntimeError("No primary-scenario damaged road edges found.")

    maximum_edge_id = int(edges_all["Edge ID"].max())
    primary_closed = np.zeros(maximum_edge_id + 1, dtype=bool)
    primary_closed[
        primary_damage["Edge ID"].to_numpy(dtype="int64")
    ] = True
    adjacency = build_adjacency(len(nodes), edges)
    service_nodes = set(
        facilities.loc[
            facilities["Included health/emergency destination"],
            "Nearest road node ID",
        ].astype(int)
    )
    if not service_nodes:
        raise RuntimeError("No primary health/emergency service nodes found.")

    settlement_nodes = settlements["Nearest road node ID"].to_numpy(
        dtype="int64"
    )
    snap_distance = settlements[
        "Settlement-to-road snap distance (m)"
    ].to_numpy(dtype="float64")
    on_network = snap_distance <= PRIMARY_SNAP_DISTANCE_M
    primary_post_distances = dijkstra(
        adjacency, service_nodes, primary_closed
    )
    primary_post_at_settlements = primary_post_distances[settlement_nodes]
    computed_post_reachable = on_network & np.isfinite(
        primary_post_at_settlements
    )

    saved_primary = accessibility.loc[
        accessibility["Primary Scenario"]
    ].set_index("OSM Settlement ID").reindex(
        settlements["OSM settlement ID"]
    )
    if len(saved_primary) != len(settlements):
        raise RuntimeError("Primary accessibility output is incomplete.")
    baseline_eligible = saved_primary["Baseline Eligible"].fillna(False).to_numpy(
        dtype=bool
    )
    saved_post_reachable = saved_primary[
        "Post-Disruption Service Reachable"
    ].fillna(False).to_numpy(dtype=bool)
    reachable_mismatches = int(
        np.count_nonzero(
            (baseline_eligible & computed_post_reachable)
            != (baseline_eligible & saved_post_reachable)
        )
    )
    saved_post_minutes = saved_primary[
        "Post-Disruption Travel Time (minutes)"
    ].to_numpy(dtype="float64")
    finite_both = np.isfinite(saved_post_minutes) & np.isfinite(
        primary_post_at_settlements
    )
    maximum_post_difference = (
        float(
            np.max(
                np.abs(
                    saved_post_minutes[finite_both]
                    - primary_post_at_settlements[finite_both]
                )
            )
        )
        if finite_both.any()
        else 0.0
    )
    if reachable_mismatches or maximum_post_difference > 1e-8:
        raise RuntimeError(
            "Primary disruption validation failed: "
            f"reachable mismatches={reachable_mismatches}, "
            f"max travel-time difference={maximum_post_difference}."
        )

    population_join = population.set_index("OSM Settlement ID").reindex(
        settlements["OSM settlement ID"]
    )
    if population_join["Estimated Settlement Population"].isna().any():
        raise RuntimeError("Settlement repair inputs are missing population rows.")
    settlement_population = population_join[
        "Estimated Settlement Population"
    ].to_numpy(dtype="float64")
    settlement_name = population_join["Settlement Name"].astype(str).to_numpy()
    district = population_join["District"].astype(str).to_numpy()
    newly_isolated = saved_primary["Newly Isolated"].fillna(False).to_numpy(
        dtype=bool
    )

    edge_lookup = edges_all.set_index("Edge ID")
    node_coordinates = nodes.set_index("Road node ID")[[
        "Easting (m)",
        "Northing (m)",
    ]]
    candidate_groups = list(
        primary_damage.groupby("OSM Feature ID", sort=True, dropna=False)
    )
    candidate_rows: list[dict[str, object]] = []
    settlement_frames: list[pd.DataFrame] = []
    geometries: list[LineString | MultiLineString] = []

    for candidate_index, (osm_feature_id, group) in enumerate(
        candidate_groups, start=1
    ):
        osm_feature_id = str(osm_feature_id)
        candidate_edge_ids = group["Edge ID"].astype("int64").drop_duplicates()
        repaired_closed = primary_closed.copy()
        repaired_closed[candidate_edge_ids.to_numpy()] = False
        repaired_distances = dijkstra(
            adjacency, service_nodes, repaired_closed
        )
        repaired_at_settlements = repaired_distances[settlement_nodes]
        repaired_reachable = on_network & np.isfinite(repaired_at_settlements)
        restored_access = (
            baseline_eligible & newly_isolated & repaired_reachable
        )
        finite_before = (
            baseline_eligible
            & computed_post_reachable
            & repaired_reachable
        )
        finite_improvement = np.full(
            len(settlements), np.nan, dtype="float64"
        )
        finite_improvement[finite_before] = (
            primary_post_at_settlements[finite_before]
            - repaired_at_settlements[finite_before]
        )
        finite_improvement[
            np.isclose(finite_improvement, 0.0, atol=1e-10)
        ] = 0.0
        if np.nanmin(finite_improvement, initial=0.0) < -1e-8:
            raise RuntimeError(
                f"Repair candidate {osm_feature_id} worsened a finite path."
            )
        finite_improvement = np.where(
            np.isfinite(finite_improvement),
            np.maximum(finite_improvement, 0.0),
            np.nan,
        )
        positive_finite = np.isfinite(finite_improvement) & (
            finite_improvement > 1e-8
        )
        post_repair_loss = np.full(
            len(settlements), np.nan, dtype="float64"
        )
        baseline_minutes = saved_primary[
            "Baseline Health/Emergency Accessibility (minutes)"
        ].to_numpy(dtype="float64")
        comparable_after_repair = baseline_eligible & repaired_reachable
        post_repair_loss[comparable_after_repair] = (
            repaired_at_settlements[comparable_after_repair]
            - baseline_minutes[comparable_after_repair]
        )
        post_repair_loss[
            np.isclose(post_repair_loss, 0.0, atol=1e-10)
        ] = 0.0

        restored_population = float(
            settlement_population[restored_access].sum()
        )
        improved_population = float(
            settlement_population[positive_finite].sum()
        )
        person_minutes_improved = float(
            np.nansum(
                settlement_population[positive_finite]
                * finite_improvement[positive_finite]
            )
        )
        reconnected_person_minutes = float(
            np.nansum(
                settlement_population[restored_access]
                * repaired_at_settlements[restored_access]
            )
        )
        population_weighted_reconnected_time = (
            reconnected_person_minutes / restored_population
            if restored_population > 0
            else np.nan
        )
        road_name = first_nonmissing(group["Road Name"])
        road_class = first_nonmissing(group["Road Class"]) or "unclassified"
        critical_label = section_label(
            osm_feature_id, road_name, road_class
        )
        repair_length_m = float(
            edge_lookup.loc[candidate_edge_ids, "Edge length (m)"].sum()
        )
        critical = (
            restored_population > 1e-8 or person_minutes_improved > 1e-8
        )
        candidate_rows.append(
            {
                "Road Repair Candidate ID": f"OSM-{osm_feature_id}",
                "Critical Road Section": critical_label,
                "Is Critical Road Section": critical,
                "OSM Feature ID": osm_feature_id,
                "Road Name": road_name,
                "Road Class": road_class,
                "CEMS Damage Grade": PRIMARY_DAMAGE_GRADE,
                "Maximum Intersecting Evidence Class": int(
                    group["Maximum Intersecting Evidence Class"].max()
                ),
                "CEMS Feature IDs": ";".join(
                    sorted(
                        {
                            item
                            for values in group["CEMS Feature IDs"].dropna()
                            for item in str(values).split(";")
                            if item
                        }
                    )
                ),
                "Evidence AOIs": ";".join(
                    sorted(
                        {
                            item
                            for values in group["Evidence AOIs"].dropna()
                            for item in str(values).split(";")
                            if item
                        }
                    )
                ),
                "Closed Graph Edges Reopened": len(candidate_edge_ids),
                "Repair Section Length (m)": repair_length_m,
                "Restored Access after Repair": bool(restored_access.any()),
                "Settlements Reconnected": int(restored_access.sum()),
                "Population Reconnected": restored_population,
                "Population-Weighted Mean Reconnected Travel Time after Repair (minutes)": population_weighted_reconnected_time,
                "Settlements with Finite Travel-Time Improvement": int(
                    positive_finite.sum()
                ),
                "Population with Finite Travel-Time Improvement": improved_population,
                "Population-Weighted Finite Travel-Time Improvement (person-minutes)": person_minutes_improved,
                "Interpretation": (
                    "marginal single-section restoration under the primary modeled disruption; "
                    "not a field-confirmed repair, engineering feasibility assessment, or cost estimate"
                ),
            }
        )

        settlement_frames.append(
            pd.DataFrame(
                {
                    "Road Repair Candidate ID": f"OSM-{osm_feature_id}",
                    "Critical Road Section": critical_label,
                    "OSM Settlement ID": settlements[
                        "OSM settlement ID"
                    ].astype(str).to_numpy(),
                    "Settlement Name (English Preferred)": settlement_name,
                    "District": district,
                    "Estimated Settlement Population": settlement_population,
                    "Baseline Eligible": baseline_eligible,
                    "Newly Isolated before Repair": newly_isolated,
                    "Post-Repair Service Reachable": pd.array(
                        np.where(
                            baseline_eligible,
                            repaired_reachable,
                            pd.NA,
                        ),
                        dtype="boolean",
                    ),
                    "Restored Access after Repair": pd.array(
                        np.where(
                            baseline_eligible,
                            restored_access,
                            pd.NA,
                        ),
                        dtype="boolean",
                    ),
                    "Post-Repair Travel Time (minutes)": np.where(
                        comparable_after_repair,
                        repaired_at_settlements,
                        np.nan,
                    ),
                    "Accessibility Loss after Repair (minutes)": post_repair_loss,
                    "Finite Travel-Time Improvement after Repair (minutes)": finite_improvement,
                }
            )
        )

        segments: list[LineString] = []
        for edge_id in candidate_edge_ids:
            edge = edge_lookup.loc[edge_id]
            left = node_coordinates.loc[int(edge["From node ID"])]
            right = node_coordinates.loc[int(edge["To node ID"])]
            segments.append(
                LineString(
                    [
                        (float(left.iloc[0]), float(left.iloc[1])),
                        (float(right.iloc[0]), float(right.iloc[1])),
                    ]
                )
            )
        geometries.append(
            segments[0] if len(segments) == 1 else MultiLineString(segments)
        )
        if candidate_index % 25 == 0 or candidate_index == len(candidate_groups):
            print(
                f"Processed {candidate_index}/{len(candidate_groups)} road repair candidates"
            )

    candidates = pd.DataFrame(candidate_rows)
    settlement_detail = pd.concat(settlement_frames, ignore_index=True)
    candidates = candidates.sort_values(
        [
            "Population Reconnected",
            "Population-Weighted Finite Travel-Time Improvement (person-minutes)",
            "Population with Finite Travel-Time Improvement",
            "Repair Section Length (m)",
            "Road Repair Candidate ID",
        ],
        ascending=[False, False, False, True, True],
    ).reset_index(drop=True)
    candidates["Primary Repair Benefit Rank"] = np.arange(
        1, len(candidates) + 1
    )
    ordered_columns = [
        "Primary Repair Benefit Rank",
        *[
            column
            for column in candidates.columns
            if column != "Primary Repair Benefit Rank"
        ],
    ]
    candidates = candidates[ordered_columns]

    candidate_geometry = gpd.GeoDataFrame(
        pd.DataFrame(candidate_rows), geometry=geometries, crs=CRS
    ).merge(
        candidates[
            ["Road Repair Candidate ID", "Primary Repair Benefit Rank"]
        ],
        on="Road Repair Candidate ID",
        how="left",
        validate="one_to_one",
    )
    candidate_geometry = candidate_geometry.sort_values(
        "Primary Repair Benefit Rank"
    )

    if len(candidates) != primary_damage["OSM Feature ID"].nunique():
        raise RuntimeError("Road repair candidate count does not match OSM units.")
    restored_by_candidate = settlement_detail.groupby(
        "Road Repair Candidate ID"
    )["Restored Access after Repair"].sum()
    expected_restored = candidates.set_index("Road Repair Candidate ID")[
        "Settlements Reconnected"
    ]
    if not restored_by_candidate.astype(int).equals(
        expected_restored.reindex(restored_by_candidate.index).astype(int)
    ):
        raise RuntimeError("Settlement and candidate reconnection totals disagree.")
    if any(not str(column).isascii() for column in candidates.columns):
        raise RuntimeError("Non-ASCII candidate column detected.")
    if any(not str(column).isascii() for column in settlement_detail.columns):
        raise RuntimeError("Non-ASCII settlement-detail column detected.")

    output_dir = root / OUTPUT_DIR
    exp_dir = root / EXP_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    exp_dir.mkdir(parents=True, exist_ok=True)
    candidate_path = output_dir / "road_repair_candidate_benefits_preprocessed.parquet"
    settlement_path = output_dir / "settlement_road_repair_benefits_preprocessed.parquet"
    geometry_path = output_dir / "road_repair_candidate_benefits.gpkg"
    audit_path = exp_dir / "road_repair_benefits_audit.csv"
    decisions_path = exp_dir / "road_repair_benefits_decisions.json"
    candidates.to_parquet(candidate_path, index=False)
    settlement_detail.to_parquet(settlement_path, index=False)
    candidate_geometry.to_file(
        geometry_path,
        layer="road_repair_candidates",
        driver="GPKG",
    )
    critical = candidates.loc[candidates["Is Critical Road Section"]]
    audit = pd.DataFrame(
        [
            {
                "Measure": "Primary closed graph edges",
                "Value": len(primary_damage),
                "Status": "class 3 and Destroyed",
            },
            {
                "Measure": "Unique OSM road repair candidates",
                "Value": len(candidates),
                "Status": "non-overlapping graph-edge groups",
            },
            {
                "Measure": "Critical road sections with modeled benefit",
                "Value": len(critical),
                "Status": "reconnection or finite travel-time improvement",
            },
            {
                "Measure": "Candidates reconnecting population",
                "Value": int(candidates["Population Reconnected"].gt(0).sum()),
                "Status": "marginal one-section-at-a-time simulation",
            },
            {
                "Measure": "Primary accessibility reachable mismatches",
                "Value": reachable_mismatches,
                "Status": "must equal zero",
            },
            {
                "Measure": "Maximum primary post-disruption time difference",
                "Value": maximum_post_difference,
                "Status": "minutes; must be numerical precision",
            },
        ]
    )
    audit.to_csv(audit_path, index=False)
    decisions = {
        "status": "confirmed_by_human",
        "candidate_unit": "one OSM road feature containing one or more primary-scenario closed graph edges",
        "repair_simulation": "reopen all primary-closed graph edges of one candidate while all other primary closures remain closed",
        "critical_section_rule": "positive population reconnection or positive finite population-weighted travel-time improvement",
        "primary_scenario": {
            "minimum_hazard_evidence_class": PRIMARY_EVIDENCE_CLASS,
            "damage_grade": PRIMARY_DAMAGE_GRADE,
            "topology_repair_threshold_m": PRIMARY_TOPOLOGY_THRESHOLD_M,
            "maximum_settlement_snap_distance_m": PRIMARY_SNAP_DISTANCE_M,
            "facility_availability": "retain all mapped health and emergency destinations",
        },
        "interpretation_limits": [
            "marginal benefit of one restored section, not an optimized repair portfolio",
            "no engineering feasibility, repair duration, or repair cost information",
            "closures and repair effects are modeled rather than field confirmed",
        ],
    }
    decisions_path.write_text(
        json.dumps(decisions, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(
        {
            "candidate_sections": len(candidates),
            "critical_sections": len(critical),
            "population_reconnection_candidates": int(
                candidates["Population Reconnected"].gt(0).sum()
            ),
            "candidate_summary": str(candidate_path),
            "settlement_detail": str(settlement_path),
            "geometry": str(geometry_path),
            "audit": str(audit_path),
            "decisions": str(decisions_path),
        }
    )
    print(
        candidates[
            [
                "Primary Repair Benefit Rank",
                "Critical Road Section",
                "Road Class",
                "Repair Section Length (m)",
                "Settlements Reconnected",
                "Population Reconnected",
                "Population-Weighted Finite Travel-Time Improvement (person-minutes)",
            ]
        ].head(10).to_string(index=False)
    )


if __name__ == "__main__":
    main()
