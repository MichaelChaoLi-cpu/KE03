#!/usr/bin/env python3
"""Construct settlement priority scores and rank-robustness summaries."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd


ACCESSIBILITY = Path(
    "data/processed/geospatial/accessibility/"
    "settlement_disruption_accessibility_robustness_preprocessed.parquet"
)
POPULATION = Path(
    "data/processed/geospatial/population/"
    "settlement_population_allocation_sensitivity_preprocessed.parquet"
)
HAZARD = Path(
    "data/processed/geospatial/exposure/"
    "settlement_hazard_exposure_preprocessed.parquet"
)
VULNERABILITY = Path(
    "data/processed/survey/vulnerability/"
    "settlement_vulnerability_sensitivity_crosswalk_preprocessed.parquet"
)
OUTPUT_DIR = Path("data/processed/decision")
EXP_DIR = Path("data/exp/data-preprocessing")
RANDOM_SEED = 20_260_901
RANDOM_WEIGHT_DRAWS = 10_000
TOP_N = 10
GEOMETRIC_EPSILON = 0.01
PRIMARY_POPULATION_THRESHOLD_M = 3_000
POPULATION_THRESHOLDS_M = [500, 1_000, 2_000, 3_000]


def midrank_scale(values: pd.Series) -> pd.Series:
    count = int(values.notna().sum())
    if count == 0:
        return pd.Series(np.nan, index=values.index, dtype="float64")
    if count == 1:
        return pd.Series(0.5, index=values.index, dtype="float64")
    ranks = values.rank(method="average", ascending=True)
    return (ranks - 1.0) / (count - 1.0)


def competition_rank(values: pd.Series) -> pd.Series:
    return values.rank(method="min", ascending=False).astype("Int64")


def append_rank_samples(
    target: dict[str, list[np.ndarray]],
    settlement_ids: np.ndarray,
    ranks: np.ndarray,
) -> None:
    for index, settlement_id in enumerate(settlement_ids):
        target[str(settlement_id)].append(
            np.asarray(ranks[index], dtype="float64").reshape(-1)
        )


def concatenate_samples(
    samples: dict[str, list[np.ndarray]], settlement_id: str
) -> np.ndarray:
    arrays = samples.get(settlement_id, [])
    if not arrays:
        return np.asarray([], dtype="float64")
    return np.concatenate(arrays)


def summarize_rank_array(values: np.ndarray) -> dict[str, float | int]:
    if values.size == 0:
        return {
            "Specification Count": 0,
            "Top 10 Frequency": np.nan,
            "Median Rank": np.nan,
            "Rank IQR Lower": np.nan,
            "Rank IQR Upper": np.nan,
            "Rank P05": np.nan,
            "Rank P95": np.nan,
        }
    return {
        "Specification Count": int(values.size),
        "Top 10 Frequency": float(np.mean(values <= TOP_N)),
        "Median Rank": float(np.median(values)),
        "Rank IQR Lower": float(np.quantile(values, 0.25)),
        "Rank IQR Upper": float(np.quantile(values, 0.75)),
        "Rank P05": float(np.quantile(values, 0.05)),
        "Rank P95": float(np.quantile(values, 0.95)),
    }


def weighted_quantile(
    values: np.ndarray,
    weights: np.ndarray,
    probability: float,
) -> float:
    """Return a deterministic weighted quantile for a discrete rank mixture."""
    if values.size == 0 or values.size != weights.size:
        return np.nan
    order = np.argsort(values, kind="stable")
    ordered_values = values[order].astype("float64")
    ordered_weights = weights[order].astype("float64")
    total_weight = float(ordered_weights.sum())
    if total_weight <= 0:
        return np.nan
    ordered_weights /= total_weight
    midpoints = np.cumsum(ordered_weights) - 0.5 * ordered_weights
    return float(
        np.interp(
            probability,
            midpoints,
            ordered_values,
            left=ordered_values[0],
            right=ordered_values[-1],
        )
    )


def summarize_family_balanced_ranks(
    structural_values: np.ndarray,
    allocation_values: np.ndarray,
    weight_values: np.ndarray,
) -> dict[str, float | int]:
    """Summarize ranks with equal total influence for three robustness families."""
    families = [
        values[np.isfinite(values)]
        for values in (structural_values, allocation_values, weight_values)
    ]
    available = [values for values in families if values.size > 0]
    family_count = len(available)
    specification_count = int(sum(values.size for values in available))
    if family_count < 3:
        return {
            "Specification Count": specification_count,
            "Family Count": family_count,
            "Top 10 Frequency": np.nan,
            "Median Rank": np.nan,
            "Rank IQR Lower": np.nan,
            "Rank IQR Upper": np.nan,
            "Rank P05": np.nan,
            "Rank P95": np.nan,
        }

    values = np.concatenate(available)
    family_weight = 1.0 / family_count
    weights = np.concatenate(
        [np.full(values.size, family_weight / values.size) for values in available]
    )
    return {
        "Specification Count": specification_count,
        "Family Count": family_count,
        "Top 10 Frequency": float(
            np.mean([np.mean(values <= TOP_N) for values in available])
        ),
        "Median Rank": weighted_quantile(values, weights, 0.50),
        "Rank IQR Lower": weighted_quantile(values, weights, 0.25),
        "Rank IQR Upper": weighted_quantile(values, weights, 0.75),
        "Rank P05": weighted_quantile(values, weights, 0.05),
        "Rank P95": weighted_quantile(values, weights, 0.95),
    }


def score_priority_frame(scenario: pd.DataFrame) -> pd.DataFrame:
    """Apply the registered ranking set, components, and primary/sensitivity scores."""
    scenario = scenario.copy()
    included = (
        scenario["Baseline Eligible"].fillna(False)
        & scenario["Estimated Settlement Population"].gt(0)
        & (
            scenario["Maximum Evidence Class within 500 m"].ge(
                scenario["Minimum Evidence Class"]
            )
            | scenario["Newly Isolated"].fillna(False)
            | scenario["Accessibility Loss (minutes)"].fillna(0).gt(0)
        )
    )
    scenario["Included in Priority Ranking"] = included
    scenario["Hazard Priority Component"] = np.nan
    scenario["Exposure Priority Component"] = np.nan
    scenario["Accessibility Priority Component"] = np.nan
    scenario["Vulnerability Sensitivity Component"] = np.nan
    scenario["Intervention Priority"] = np.nan
    scenario["Priority Rank"] = pd.array([pd.NA] * len(scenario), dtype="Int64")
    scenario["Sensitivity Intervention Priority"] = np.nan
    scenario["Sensitivity Priority Rank"] = pd.array(
        [pd.NA] * len(scenario), dtype="Int64"
    )

    selected = scenario.loc[included].copy()
    if selected.empty:
        return scenario
    selected["Hazard Priority Component"] = midrank_scale(
        selected["Maximum Evidence Class within 500 m"]
    )
    selected["Exposure Priority Component"] = midrank_scale(
        selected["Estimated Settlement Population"]
    )
    accessibility_component = pd.Series(0.0, index=selected.index, dtype="float64")
    isolated = selected["Newly Isolated"].fillna(False)
    positive = (
        selected["Accessibility Loss (minutes)"].notna()
        & selected["Accessibility Loss (minutes)"].gt(0)
        & ~isolated
    )
    positive_count = int(positive.sum())
    if positive_count:
        accessibility_component.loc[positive] = (
            selected.loc[positive, "Accessibility Loss (minutes)"].rank(
                method="average", ascending=True
            )
            / (positive_count + 1.0)
        )
    accessibility_component.loc[isolated] = 1.0
    selected["Accessibility Priority Component"] = accessibility_component
    selected["Vulnerability Sensitivity Component"] = (
        selected["Shrinkage-Adjusted District Vulnerability Percentile"] / 100.0
    )
    selected["Intervention Priority"] = selected[
        [
            "Hazard Priority Component",
            "Exposure Priority Component",
            "Accessibility Priority Component",
        ]
    ].mean(axis=1)
    selected["Priority Rank"] = competition_rank(selected["Intervention Priority"])
    selected["Sensitivity Intervention Priority"] = selected[
        [
            "Hazard Priority Component",
            "Exposure Priority Component",
            "Accessibility Priority Component",
            "Vulnerability Sensitivity Component",
        ]
    ].mean(axis=1)
    selected["Sensitivity Priority Rank"] = competition_rank(
        selected["Sensitivity Intervention Priority"]
    )
    update_columns = [
        "Hazard Priority Component",
        "Exposure Priority Component",
        "Accessibility Priority Component",
        "Vulnerability Sensitivity Component",
        "Intervention Priority",
        "Priority Rank",
        "Sensitivity Intervention Priority",
        "Sensitivity Priority Rank",
    ]
    scenario.loc[selected.index, update_columns] = selected[update_columns]
    return scenario


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    required = [
        root / ACCESSIBILITY,
        root / POPULATION,
        root / HAZARD,
        root / VULNERABILITY,
    ]
    for path in required:
        if not path.exists():
            raise FileNotFoundError(path)

    accessibility = pd.read_parquet(root / ACCESSIBILITY)
    population = pd.read_parquet(root / POPULATION)
    hazard = pd.read_parquet(root / HAZARD)
    vulnerability = pd.read_parquet(root / VULNERABILITY)

    if population.duplicated(
        ["OSM Settlement ID", "Allocation Threshold (m)"]
    ).any():
        raise RuntimeError("Duplicate settlement-threshold rows in population data.")
    if sorted(population["Allocation Threshold (m)"].unique().tolist()) != POPULATION_THRESHOLDS_M:
        raise RuntimeError("Population-allocation sensitivity thresholds are incomplete.")
    for frame, name in (
        (hazard, "hazard exposure"),
        (vulnerability, "vulnerability crosswalk"),
    ):
        if frame["OSM Settlement ID"].duplicated().any():
            raise RuntimeError(f"Duplicate settlement ID in {name} data.")

    primary_population = population.loc[
        population["Allocation Threshold (m)"].eq(PRIMARY_POPULATION_THRESHOLD_M)
    ].copy()
    if primary_population["OSM Settlement ID"].duplicated().any():
        raise RuntimeError("Primary population allocation contains duplicate settlements.")

    population_join = primary_population[
        [
            "OSM Settlement ID",
            "Settlement Name",
            "Place Type",
            "Local Unit",
            "Local Unit P-Code",
            "District",
            "District P-Code",
            "Settlement Longitude",
            "Settlement Latitude",
            "Estimated Settlement Population",
            "Has Assigned Population",
        ]
    ].rename(
        columns={
            "Settlement Name": "Settlement Name (English Preferred)",
            "Place Type": "Population Place Type",
        }
    )
    hazard_join = hazard[
        [
            "OSM Settlement ID",
            "Direct Evidence Class",
            "Maximum Evidence Class within 500 m",
        ]
    ]
    vulnerability_join = vulnerability[
        [
            "OSM Settlement ID",
            "Reliability Category",
            "PSU Count",
            "Shrinkage-Adjusted District Vulnerability Percentile",
            "Sensitivity Settlement Ranking Use",
        ]
    ]

    detail = accessibility.merge(
        population_join,
        on="OSM Settlement ID",
        how="left",
        validate="many_to_one",
    ).merge(
        hazard_join,
        on="OSM Settlement ID",
        how="left",
        validate="many_to_one",
    ).merge(
        vulnerability_join,
        on="OSM Settlement ID",
        how="left",
        validate="many_to_one",
    )
    if detail["Estimated Settlement Population"].isna().any():
        raise RuntimeError("Priority inputs are missing settlement population rows.")
    if detail[
        "Shrinkage-Adjusted District Vulnerability Percentile"
    ].isna().any():
        raise RuntimeError("Priority inputs are missing vulnerability context rows.")
    detail["Direct Evidence Class"] = detail[
        "Direct Evidence Class"
    ].fillna(0).astype("int8")
    detail["Maximum Evidence Class within 500 m"] = detail[
        "Maximum Evidence Class within 500 m"
    ].fillna(0).astype("int8")

    scenario_rank_samples: dict[str, list[np.ndarray]] = defaultdict(list)
    scenario_inclusion_counts: dict[str, int] = defaultdict(int)
    calculated_frames: list[pd.DataFrame] = []

    for _, scenario in detail.groupby("Scenario ID", sort=False):
        scenario = score_priority_frame(scenario)
        selected = scenario.loc[scenario["Included in Priority Ranking"]].copy()
        if not selected.empty:
            settlement_ids = selected["OSM Settlement ID"].astype(str).to_numpy()
            ranks = selected["Priority Rank"].to_numpy(dtype="float64")
            append_rank_samples(
                scenario_rank_samples, settlement_ids, ranks[:, None]
            )
            for settlement_id in settlement_ids:
                scenario_inclusion_counts[settlement_id] += 1
        calculated_frames.append(scenario)

    scored = pd.concat(calculated_frames, ignore_index=True)
    primary = scored.loc[scored["Primary Scenario"]].copy()
    if primary["Scenario ID"].nunique() != 1 or len(primary) != len(primary_population):
        raise RuntimeError("Expected exactly one complete primary scenario.")
    primary_selected = primary.loc[
        primary["Included in Priority Ranking"]
    ].copy()

    allocation_rank_samples: dict[str, list[np.ndarray]] = defaultdict(list)
    allocation_inclusion_counts: dict[str, int] = defaultdict(int)
    allocation_frames: list[pd.DataFrame] = []
    primary_accessibility = accessibility.loc[accessibility["Primary Scenario"]].copy()
    if len(primary_accessibility) != len(primary_population):
        raise RuntimeError("Primary accessibility surface is incomplete.")
    for threshold_m, threshold_population in population.groupby(
        "Allocation Threshold (m)", sort=True
    ):
        threshold_join = threshold_population[
            [
                "OSM Settlement ID",
                "Settlement Name",
                "Place Type",
                "Local Unit",
                "Local Unit P-Code",
                "District",
                "District P-Code",
                "Settlement Longitude",
                "Settlement Latitude",
                "Allocation Threshold (m)",
                "Estimated Settlement Population",
                "Has Assigned Population",
            ]
        ].rename(
            columns={
                "Settlement Name": "Settlement Name (English Preferred)",
                "Place Type": "Population Place Type",
            }
        )
        allocation = primary_accessibility.merge(
            threshold_join,
            on="OSM Settlement ID",
            how="left",
            validate="one_to_one",
        ).merge(
            hazard_join,
            on="OSM Settlement ID",
            how="left",
            validate="one_to_one",
        ).merge(
            vulnerability_join,
            on="OSM Settlement ID",
            how="left",
            validate="one_to_one",
        )
        if allocation["Estimated Settlement Population"].isna().any():
            raise RuntimeError(f"Population allocation is incomplete for T={threshold_m} m.")
        allocation["Direct Evidence Class"] = allocation[
            "Direct Evidence Class"
        ].fillna(0).astype("int8")
        allocation["Maximum Evidence Class within 500 m"] = allocation[
            "Maximum Evidence Class within 500 m"
        ].fillna(0).astype("int8")
        allocation["Population Allocation Specification"] = f"T{int(threshold_m)}"
        allocation["Primary Population Allocation"] = int(threshold_m) == PRIMARY_POPULATION_THRESHOLD_M
        allocation = score_priority_frame(allocation)
        selected = allocation.loc[allocation["Included in Priority Ranking"]].copy()
        if not selected.empty:
            settlement_ids = selected["OSM Settlement ID"].astype(str).to_numpy()
            ranks = selected["Priority Rank"].to_numpy(dtype="float64")
            append_rank_samples(
                allocation_rank_samples, settlement_ids, ranks[:, None]
            )
            for settlement_id in settlement_ids:
                allocation_inclusion_counts[settlement_id] += 1
        allocation_frames.append(allocation)
    allocation_scored = pd.concat(allocation_frames, ignore_index=True)
    if allocation_scored["Population Allocation Specification"].nunique() != len(
        POPULATION_THRESHOLDS_M
    ):
        raise RuntimeError("Population-allocation robustness surface is incomplete.")

    component_columns = [
        "Hazard Priority Component",
        "Exposure Priority Component",
        "Accessibility Priority Component",
    ]
    component_matrix = primary_selected[component_columns].to_numpy(
        dtype="float64"
    )
    primary_ids = primary_selected["OSM Settlement ID"].astype(str).to_numpy()
    weight_rank_samples: dict[str, list[np.ndarray]] = defaultdict(list)

    deterministic_weights = {
        "Leave Out Hazard": np.asarray([0.0, 0.5, 0.5]),
        "Leave Out Exposure": np.asarray([0.5, 0.0, 0.5]),
        "Leave Out Accessibility": np.asarray([0.5, 0.5, 0.0]),
        "Emphasize Hazard": np.asarray([0.5, 0.25, 0.25]),
        "Emphasize Exposure": np.asarray([0.25, 0.5, 0.25]),
        "Emphasize Accessibility": np.asarray([0.25, 0.25, 0.5]),
    }
    for weights in deterministic_weights.values():
        scores = component_matrix @ weights
        ranks = pd.Series(scores).rank(
            method="min", ascending=False
        ).to_numpy(dtype="float64")
        append_rank_samples(
            weight_rank_samples, primary_ids, ranks[:, None]
        )

    geometric_scores = np.prod(
        np.power(
            GEOMETRIC_EPSILON + component_matrix,
            np.asarray([1 / 3, 1 / 3, 1 / 3]),
        ),
        axis=1,
    )
    geometric_ranks = pd.Series(geometric_scores).rank(
        method="min", ascending=False
    ).to_numpy(dtype="float64")
    append_rank_samples(
        weight_rank_samples, primary_ids, geometric_ranks[:, None]
    )

    rng = np.random.default_rng(RANDOM_SEED)
    random_weights = rng.dirichlet(
        np.ones(len(component_columns)), size=RANDOM_WEIGHT_DRAWS
    )
    random_scores = component_matrix @ random_weights.T
    random_ranks = pd.DataFrame(random_scores).rank(
        axis=0, method="min", ascending=False
    ).to_numpy(dtype="float64")
    append_rank_samples(weight_rank_samples, primary_ids, random_ranks)

    base = population_join.copy()
    base["OSM Settlement ID"] = base["OSM Settlement ID"].astype(str)
    primary_columns = primary[
        [
            "OSM Settlement ID",
            "Included in Priority Ranking",
            "Intervention Priority",
            "Priority Rank",
            "Sensitivity Intervention Priority",
            "Sensitivity Priority Rank",
            "Hazard Priority Component",
            "Exposure Priority Component",
            "Accessibility Priority Component",
            "Vulnerability Sensitivity Component",
        ]
    ].copy()
    primary_columns["OSM Settlement ID"] = primary_columns[
        "OSM Settlement ID"
    ].astype(str)
    stability = base.merge(
        primary_columns,
        on="OSM Settlement ID",
        how="left",
        validate="one_to_one",
    )
    robustness_rows: list[dict[str, object]] = []
    total_scenarios = int(scored["Scenario ID"].nunique())
    for row in stability.itertuples(index=False):
        settlement_id = str(row[0])
        scenario_values = concatenate_samples(
            scenario_rank_samples, settlement_id
        )
        allocation_values = concatenate_samples(
            allocation_rank_samples, settlement_id
        )
        weight_values = concatenate_samples(
            weight_rank_samples, settlement_id
        )
        scenario_summary = summarize_rank_array(scenario_values)
        allocation_summary = summarize_rank_array(allocation_values)
        weight_summary = summarize_rank_array(weight_values)
        balanced_summary = summarize_family_balanced_ranks(
            scenario_values,
            allocation_values,
            weight_values,
        )
        robustness_rows.append(
            {
                "OSM Settlement ID": settlement_id,
                "Scenario Inclusion Count": scenario_inclusion_counts.get(
                    settlement_id, 0
                ),
                "Scenario Inclusion Frequency": scenario_inclusion_counts.get(
                    settlement_id, 0
                )
                / total_scenarios,
                "Structural-Scenario Top-10 Frequency": scenario_summary[
                    "Top 10 Frequency"
                ],
                "Allocation-Threshold Inclusion Count": allocation_inclusion_counts.get(
                    settlement_id, 0
                ),
                "Allocation-Threshold Inclusion Frequency": allocation_inclusion_counts.get(
                    settlement_id, 0
                )
                / len(POPULATION_THRESHOLDS_M),
                "Allocation-Threshold Top-10 Frequency": allocation_summary[
                    "Top 10 Frequency"
                ],
                "Weight-Rule Top-10 Frequency": weight_summary[
                    "Top 10 Frequency"
                ],
                "Scenario Specification Count": scenario_summary[
                    "Specification Count"
                ],
                "Allocation Specification Count": allocation_summary[
                    "Specification Count"
                ],
                "Weight Specification Count": weight_summary[
                    "Specification Count"
                ],
                "Rank Stability": balanced_summary["Top 10 Frequency"],
                "Robustness Family Count": balanced_summary["Family Count"],
                "Robustness Specification Count": balanced_summary[
                    "Specification Count"
                ],
                "Median Priority Rank": balanced_summary["Median Rank"],
                "Priority Rank IQR Lower": balanced_summary[
                    "Rank IQR Lower"
                ],
                "Priority Rank IQR Upper": balanced_summary[
                    "Rank IQR Upper"
                ],
                "Priority Rank P05": balanced_summary["Rank P05"],
                "Priority Rank P95": balanced_summary["Rank P95"],
            }
        )
    robustness = stability.merge(
        pd.DataFrame(robustness_rows),
        on="OSM Settlement ID",
        how="left",
        validate="one_to_one",
    )
    robustness["Sensitivity Rank Shift"] = (
        robustness["Priority Rank"].astype("Float64")
        - robustness["Sensitivity Priority Rank"].astype("Float64")
    )

    scored["OSM Settlement ID"] = scored["OSM Settlement ID"].astype(str)
    primary["OSM Settlement ID"] = primary["OSM Settlement ID"].astype(str)
    ordered_primary = primary.sort_values(
        ["Included in Priority Ranking", "Priority Rank", "OSM Settlement ID"],
        ascending=[False, True, True],
        na_position="last",
    )
    if int(ordered_primary["Included in Priority Ranking"].sum()) == 0:
        raise RuntimeError("Primary ranking set is empty.")
    if not ordered_primary.loc[
        ordered_primary["Included in Priority Ranking"], "Priority Rank"
    ].notna().all():
        raise RuntimeError("Primary ranking contains missing ranks.")
    for column in (
        "Hazard Priority Component",
        "Exposure Priority Component",
        "Accessibility Priority Component",
        "Vulnerability Sensitivity Component",
        "Intervention Priority",
        "Sensitivity Intervention Priority",
    ):
        values = scored.loc[
            scored["Included in Priority Ranking"], column
        ]
        if not values.between(0, 1).all():
            raise RuntimeError(f"{column} falls outside [0, 1].")

    output_dir = root / OUTPUT_DIR
    exp_dir = root / EXP_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    exp_dir.mkdir(parents=True, exist_ok=True)
    detail_path = output_dir / "settlement_priority_scenarios_preprocessed.parquet"
    allocation_path = (
        output_dir
        / "settlement_priority_population_allocation_sensitivity_preprocessed.parquet"
    )
    primary_path = output_dir / "settlement_intervention_priority_preprocessed.parquet"
    robustness_path = output_dir / "settlement_priority_robustness_preprocessed.parquet"
    audit_path = exp_dir / "settlement_priority_metrics_audit.csv"
    decisions_path = exp_dir / "settlement_priority_metrics_decisions.json"
    scored.to_parquet(detail_path, index=False)
    allocation_scored.to_parquet(allocation_path, index=False)
    ordered_primary.to_parquet(primary_path, index=False)
    robustness.to_parquet(robustness_path, index=False)

    primary_ranked = ordered_primary.loc[
        ordered_primary["Included in Priority Ranking"]
    ]
    audit = pd.DataFrame(
        [
            {
                "Measure": "Structural scenarios",
                "Value": total_scenarios,
                "Status": "expected 192",
            },
            {
                "Measure": "Population-allocation specifications",
                "Value": len(POPULATION_THRESHOLDS_M),
                "Status": "independent 500 m, 1000 m, 2000 m, and 3000 m robustness family",
            },
            {
                "Measure": "Primary ranking settlements",
                "Value": len(primary_ranked),
                "Status": "positive population, baseline eligible, and hazard or access consequence",
            },
            {
                "Measure": "Primary newly isolated settlements ranked",
                "Value": int(primary_ranked["Newly Isolated"].fillna(False).sum()),
                "Status": "accessibility component fixed at 1",
            },
            {
                "Measure": "Random Dirichlet weight draws",
                "Value": RANDOM_WEIGHT_DRAWS,
                "Status": f"seed {RANDOM_SEED}",
            },
            {
                "Measure": "Robustness families",
                "Value": 3,
                "Status": "structural, population-allocation, and weight-rule families receive equal total influence",
            },
            {
                "Measure": "Primary vulnerability use",
                "Value": 0,
                "Status": "excluded from Intervention Priority",
            },
        ]
    )
    audit.to_csv(audit_path, index=False)
    decisions = {
        "status": "confirmed_in_anasop_sections_5_to_7",
        "primary_score": {
            "components": ["Hazard", "Exposure", "Accessibility"],
            "weights": [1 / 3, 1 / 3, 1 / 3],
            "vulnerability_included": False,
        },
        "sensitivity_score": {
            "components": [
                "Hazard",
                "Exposure",
                "Accessibility",
                "District contextual vulnerability",
            ],
            "weights": [0.25, 0.25, 0.25, 0.25],
            "interpretation": "district context only; not settlement measurement",
        },
        "robustness": {
            "structural_scenarios": total_scenarios,
            "population_allocation_thresholds_m": POPULATION_THRESHOLDS_M,
            "random_weight_draws": RANDOM_WEIGHT_DRAWS,
            "random_seed": RANDOM_SEED,
            "dirichlet_alpha": [1, 1, 1],
            "geometric_epsilon": GEOMETRIC_EPSILON,
            "rank_method": "descending competition rank",
            "rank_stability": "equal-family mean of structural-scenario, population-allocation, and primary-scenario weight-rule top-10 frequencies",
            "rank_intervals": "weighted quantiles assigning total weight one-third to each robustness family",
        },
    }
    decisions_path.write_text(
        json.dumps(decisions, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(
        {
            "structural_scenarios": total_scenarios,
            "primary_ranking_set": len(primary_ranked),
            "random_weight_draws": RANDOM_WEIGHT_DRAWS,
            "detail": str(detail_path),
            "allocation_sensitivity": str(allocation_path),
            "primary": str(primary_path),
            "robustness": str(robustness_path),
            "audit": str(audit_path),
            "decisions": str(decisions_path),
        }
    )
    print(
        primary_ranked[
            [
                "Priority Rank",
                "Settlement Name (English Preferred)",
                "District",
                "Maximum Evidence Class within 500 m",
                "Estimated Settlement Population",
                "Newly Isolated",
                "Accessibility Loss (minutes)",
                "Intervention Priority",
                "Sensitivity Priority Rank",
            ]
        ].head(TOP_N).to_string(index=False)
    )


if __name__ == "__main__":
    main()
