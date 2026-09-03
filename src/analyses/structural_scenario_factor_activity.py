"""Audit which nominal structural-scenario factors change decision outcomes.

The 192-scenario factorial varies five factors. This audit compares each factor
while holding the other four fixed, distinguishes graph changes from changes in
population accessibility outcomes, and checks whether any factor changes the
top-ten settlement set. It does not modify the registered primary scenario.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
PRIORITY_SCENARIOS = (
    ROOT
    / "data"
    / "processed"
    / "decision"
    / "settlement_priority_scenarios_preprocessed.parquet"
)
ACCESSIBILITY_SUMMARY = (
    ROOT
    / "data"
    / "processed"
    / "geospatial"
    / "accessibility"
    / "accessibility_robustness_scenario_summary_preprocessed.parquet"
)
RESULT_OUTPUT = (
    ROOT
    / "data"
    / "results"
    / "supplementary"
    / "structural_scenario_factor_activity.csv"
)
AUDIT_OUTPUT = (
    ROOT
    / "data"
    / "exp"
    / "data-preprocessing"
    / "structural_scenario_factor_activity_audit.csv"
)
STATE_OUTPUT = (
    ROOT
    / "data"
    / "exp"
    / "data-preprocessing"
    / "structural_scenario_effective_states.csv"
)
SUMMARY_OUTPUT = (
    ROOT
    / "data"
    / "exp"
    / "data-preprocessing"
    / "structural_scenario_factor_activity_summary.json"
)

FACTOR_COLUMNS = {
    "Hazard evidence threshold": "Minimum Evidence Class",
    "Road closure rule": "Road Closure Rule",
    "Facility availability": "Facility Availability Rule",
    "Topology repair threshold": "Topology Repair Threshold (m)",
    "Settlement snap distance": "Maximum Settlement Snap Distance (m)",
}
METADATA_COLUMNS = list(FACTOR_COLUMNS.values())
OUTCOME_COLUMNS = [
    "Newly Isolated Population",
    "Population Delayed over 5 Minutes",
    "Population-Weighted Accessibility Loss (person-minutes)",
]


def stable_levels(values: pd.Series) -> str:
    """Return compact, deterministic factor levels for the audit table."""
    unique = values.drop_duplicates().tolist()
    if all(isinstance(value, (int, float, np.integer, np.floating)) for value in unique):
        unique = sorted(unique)
        return ", ".join(f"{float(value):g}" for value in unique)
    return " | ".join(sorted(str(value) for value in unique))


def build_scenario_summary() -> pd.DataFrame:
    detail = pd.read_parquet(PRIORITY_SCENARIOS)
    accessibility = pd.read_parquet(ACCESSIBILITY_SUMMARY)

    if detail["Scenario ID"].nunique() != 192:
        raise RuntimeError("Expected exactly 192 structural scenarios")
    per_scenario_counts = detail.groupby("Scenario ID").size()
    if per_scenario_counts.nunique() != 1 or int(per_scenario_counts.iloc[0]) != 767:
        raise RuntimeError("Every structural scenario must contain the 767-settlement study base")

    population = detail["Estimated Settlement Population"].fillna(0.0).astype(float)
    finite_loss = detail["Accessibility Loss (minutes)"].astype(float)
    detail = detail.assign(
        _isolated_population=np.where(
            detail["Newly Isolated"].fillna(False), population, 0.0
        ),
        _delayed_population=np.where(
            detail["Accessibility Status"].eq("delay over 5 minutes"), population, 0.0
        ),
        _person_minutes=np.where(
            np.isfinite(finite_loss), population * np.maximum(finite_loss, 0.0), 0.0
        ),
    )

    summary = (
        detail.groupby(["Scenario ID", *METADATA_COLUMNS], dropna=False, sort=False)
        .agg(
            **{
                "Newly Isolated Population": ("_isolated_population", "sum"),
                "Population Delayed over 5 Minutes": ("_delayed_population", "sum"),
                "Population-Weighted Accessibility Loss (person-minutes)": (
                    "_person_minutes",
                    "sum",
                ),
                "Newly Isolated Settlements": ("Newly Isolated", "sum"),
                "Baseline Eligible Settlements": ("Baseline Eligible", "sum"),
            }
        )
        .reset_index()
    )

    top_ten_detail = detail.loc[
        detail["Priority Rank"].notna() & detail["Priority Rank"].le(10)
    ].copy()
    top_ten_sets = (
        top_ten_detail.groupby("Scenario ID")["OSM Settlement ID"]
        .apply(lambda values: "|".join(sorted(values.astype(str))))
        .rename("Top-10 Settlement Set")
    )
    top_ten_orders = (
        top_ten_detail.sort_values(
            ["Scenario ID", "Priority Rank", "OSM Settlement ID"], kind="stable"
        )
        .groupby("Scenario ID")["OSM Settlement ID"]
        .apply(lambda values: "|".join(values.astype(str)))
        .rename("Top-10 Settlement Order")
    )
    top_ten = pd.concat([top_ten_sets, top_ten_orders], axis=1).reset_index()
    summary = summary.merge(top_ten, on="Scenario ID", how="left", validate="one_to_one")

    graph_columns = [
        "Scenario ID",
        "Closed Graph Edges",
        "Closed Edge Length (km)",
        "Removed Health/Emergency Destinations",
    ]
    summary = summary.merge(
        accessibility[graph_columns],
        on="Scenario ID",
        how="left",
        validate="one_to_one",
    )
    if summary.isna().any().any():
        missing = summary.columns[summary.isna().any()].tolist()
        raise RuntimeError(f"Scenario summary contains missing values: {missing}")
    if len(summary) != 192:
        raise RuntimeError("Scenario aggregation did not preserve all 192 scenarios")
    return summary


def build_factor_activity(summary: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for factor, factor_column in FACTOR_COLUMNS.items():
        held_columns = [column for column in METADATA_COLUMNS if column != factor_column]
        comparison_groups = list(summary.groupby(held_columns, dropna=False, sort=False))
        expected_group_count = int(len(summary) / summary[factor_column].nunique())
        if len(comparison_groups) != expected_group_count:
            raise RuntimeError(f"Unexpected paired-group count for {factor}")

        graph_active = 0
        access_active = 0
        top_ten_active = 0
        top_ten_order_active = 0
        max_deltas = {column: 0.0 for column in OUTCOME_COLUMNS}
        max_edge_delta = 0
        max_closed_length_delta = 0.0
        max_destination_delta = 0

        for _, group in comparison_groups:
            if group[factor_column].nunique() != summary[factor_column].nunique():
                raise RuntimeError(f"Incomplete paired comparison for {factor}")
            edge_delta = int(group["Closed Graph Edges"].max() - group["Closed Graph Edges"].min())
            length_delta = float(
                group["Closed Edge Length (km)"].max()
                - group["Closed Edge Length (km)"].min()
            )
            destination_delta = int(
                group["Removed Health/Emergency Destinations"].max()
                - group["Removed Health/Emergency Destinations"].min()
            )
            if edge_delta or length_delta > 1e-9 or destination_delta:
                graph_active += 1
            max_edge_delta = max(max_edge_delta, edge_delta)
            max_closed_length_delta = max(max_closed_length_delta, length_delta)
            max_destination_delta = max(max_destination_delta, destination_delta)

            deltas = {
                column: float(group[column].max() - group[column].min())
                for column in OUTCOME_COLUMNS
            }
            if any(delta > 1e-6 for delta in deltas.values()):
                access_active += 1
            for column, delta in deltas.items():
                max_deltas[column] = max(max_deltas[column], delta)
            if group["Top-10 Settlement Set"].nunique() > 1:
                top_ten_active += 1
            if group["Top-10 Settlement Order"].nunique() > 1:
                top_ten_order_active += 1

        rows.append(
            {
                "Factor": factor,
                "Levels": stable_levels(summary[factor_column]),
                "Paired Comparison Groups": len(comparison_groups),
                "Graph-Active Groups": graph_active,
                "Access-Outcome-Active Groups": access_active,
                "Maximum Closed-Edge Count Change": max_edge_delta,
                "Maximum Closed-Length Change (km)": max_closed_length_delta,
                "Maximum Removed-Destination Change": max_destination_delta,
                "Maximum Newly Isolated Population Change": max_deltas[
                    "Newly Isolated Population"
                ],
                "Maximum Delayed Population Change": max_deltas[
                    "Population Delayed over 5 Minutes"
                ],
                "Maximum Person-Minutes Change": max_deltas[
                    "Population-Weighted Accessibility Loss (person-minutes)"
                ],
                "Top-10-Set Change Groups": top_ten_active,
                "Top-10-Order Change Groups": top_ten_order_active,
            }
        )
    return pd.DataFrame(rows)


def build_effective_states(summary: pd.DataFrame) -> pd.DataFrame:
    rounded = summary.copy()
    for column in OUTCOME_COLUMNS:
        rounded[column] = rounded[column].round(3)
    states = (
        rounded.groupby(OUTCOME_COLUMNS, dropna=False)
        .agg(
            **{
                "Scenario Count": ("Scenario ID", "size"),
                "Example Scenario ID": ("Scenario ID", "first"),
                "Distinct Top-10 Sets": ("Top-10 Settlement Set", "nunique"),
            }
        )
        .reset_index()
        .sort_values(OUTCOME_COLUMNS, kind="stable")
        .reset_index(drop=True)
    )
    states.insert(0, "Effective State", np.arange(1, len(states) + 1))
    return states


def validate(
    summary: pd.DataFrame,
    activity: pd.DataFrame,
    states: pd.DataFrame,
) -> dict[str, object]:
    primary_id = "H3_destroyed_roads_only_r5_t3000"
    primary = summary.loc[summary["Scenario ID"].eq(primary_id)]
    if len(primary) != 1:
        raise RuntimeError("Registered primary scenario is missing or duplicated")
    primary = primary.iloc[0]
    expected_primary = {
        "Newly Isolated Population": 13_906.314996764064,
        "Population Delayed over 5 Minutes": 24_487.6662966609,
        "Population-Weighted Accessibility Loss (person-minutes)": 540_233.148351905,
    }
    for column, expected in expected_primary.items():
        if not np.isclose(float(primary[column]), expected):
            raise RuntimeError(f"Primary scenario mismatch for {column}")

    if len(states) != 10:
        raise RuntimeError("Expected ten distinct aggregate accessibility states")
    distinct_top_ten = int(summary["Top-10 Settlement Set"].nunique())
    if distinct_top_ten != 1:
        raise RuntimeError("Expected one common top-ten settlement set")
    distinct_top_ten_orders = int(summary["Top-10 Settlement Order"].nunique())
    if distinct_top_ten_orders != 3:
        raise RuntimeError("Expected three top-ten orderings")

    activity_by_factor = activity.set_index("Factor")
    if int(activity_by_factor.loc["Road closure rule", "Access-Outcome-Active Groups"]) != 0:
        raise RuntimeError("Road closure rule unexpectedly changes accessibility outcomes")
    if int(activity_by_factor.loc["Topology repair threshold", "Access-Outcome-Active Groups"]) != 0:
        raise RuntimeError("Topology threshold unexpectedly changes accessibility outcomes")
    if int(activity["Top-10-Set Change Groups"].sum()) != 0:
        raise RuntimeError("A factor unexpectedly changes the top-ten set")

    return {
        "status": "validated",
        "primary_scenario_id": primary_id,
        "nominal_structural_scenarios": len(summary),
        "distinct_aggregate_accessibility_states": len(states),
        "distinct_top_ten_sets": distinct_top_ten,
        "distinct_top_ten_orderings": distinct_top_ten_orders,
        "primary_outcomes": {
            column: float(primary[column]) for column in OUTCOME_COLUMNS
        },
        "interpretation": (
            "The factorial is a factor-activity sensitivity audit. Repeated nominal "
            "scenarios must not be treated as independent evidence of top-ten stability."
        ),
    }


def main() -> None:
    summary = build_scenario_summary()
    activity = build_factor_activity(summary)
    states = build_effective_states(summary)
    audit_summary = validate(summary, activity, states)

    for path in (RESULT_OUTPUT, AUDIT_OUTPUT, STATE_OUTPUT, SUMMARY_OUTPUT):
        path.parent.mkdir(parents=True, exist_ok=True)
    activity.to_csv(RESULT_OUTPUT, index=False)
    activity.to_csv(AUDIT_OUTPUT, index=False)
    states.to_csv(STATE_OUTPUT, index=False)
    SUMMARY_OUTPUT.write_text(
        json.dumps(audit_summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(activity.to_string(index=False))
    print(json.dumps(audit_summary, indent=2, sort_keys=True))
    print(f"Wrote {RESULT_OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {AUDIT_OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {STATE_OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {SUMMARY_OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
