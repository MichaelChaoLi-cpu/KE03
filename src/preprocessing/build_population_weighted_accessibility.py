#!/usr/bin/env python3
"""Join settlement population to disruption scenarios and aggregate affected population."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


POPULATION = Path(
    "data/processed/geospatial/population/"
    "settlement_population_allocation_preprocessed.parquet"
)
ACCESSIBILITY_DETAIL = Path(
    "data/processed/geospatial/accessibility/"
    "settlement_disruption_accessibility_preprocessed.parquet"
)
ACCESSIBILITY_SUMMARY = Path(
    "data/processed/geospatial/accessibility/"
    "accessibility_scenario_summary_preprocessed.parquet"
)
OUTPUT_DETAIL = Path(
    "data/processed/geospatial/accessibility/"
    "settlement_disruption_population_preprocessed.parquet"
)
OUTPUT_SUMMARY = Path(
    "data/processed/geospatial/accessibility/"
    "accessibility_scenario_population_summary_preprocessed.parquet"
)
AUDIT = Path(
    "data/exp/data-preprocessing/accessibility_population_integration_audit.csv"
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    required = [
        root / POPULATION,
        root / ACCESSIBILITY_DETAIL,
        root / ACCESSIBILITY_SUMMARY,
    ]
    for path in required:
        if not path.exists():
            raise FileNotFoundError(path)

    population = pd.read_parquet(root / POPULATION)
    accessibility = pd.read_parquet(root / ACCESSIBILITY_DETAIL)
    scenario_summary = pd.read_parquet(root / ACCESSIBILITY_SUMMARY)

    population_columns = [
        "OSM Settlement ID",
        "Settlement Name",
        "Estimated Settlement Population",
        "Allocation Threshold (m)",
        "Has Assigned Population",
        "Local Unit",
        "Local Unit P-Code",
        "District",
        "District P-Code",
    ]
    if population["OSM Settlement ID"].duplicated().any():
        raise RuntimeError("Settlement population table contains duplicate identifiers.")
    population_join = population[population_columns].rename(
        columns={"Settlement Name": "Settlement Name (English Preferred)"}
    )
    detail = accessibility.merge(
        population_join,
        on="OSM Settlement ID",
        how="left",
        validate="many_to_one",
    )
    if detail["Estimated Settlement Population"].isna().any():
        raise RuntimeError("Some accessibility settlements have no population row.")

    estimated_population = detail["Estimated Settlement Population"].to_numpy(
        dtype="float64"
    )
    baseline_eligible = detail["Baseline Eligible"].fillna(False).to_numpy(dtype=bool)
    post_reachable = detail["Post-Disruption Service Reachable"].fillna(False).to_numpy(
        dtype=bool
    )
    newly_isolated = detail["Newly Isolated"].fillna(False).to_numpy(dtype=bool)
    delayed = detail["Accessibility Status"].eq("delay over 5 minutes").to_numpy()
    positive_loss = detail["Accessibility Loss (minutes)"].fillna(0).gt(0).to_numpy()
    finite_loss = detail["Accessibility Loss (minutes)"].to_numpy(dtype="float64")

    detail["Baseline Eligible Population"] = np.where(
        baseline_eligible, estimated_population, 0.0
    )
    detail["Post-Disruption Reachable Population"] = np.where(
        baseline_eligible & post_reachable, estimated_population, 0.0
    )
    detail["Newly Isolated Population"] = np.where(
        newly_isolated, estimated_population, 0.0
    )
    detail["Population Delayed over 5 Minutes"] = np.where(
        delayed, estimated_population, 0.0
    )
    detail["Population with Positive Accessibility Loss"] = np.where(
        positive_loss, estimated_population, 0.0
    )
    detail["Population-Weighted Accessibility Loss (person-minutes)"] = np.where(
        np.isfinite(finite_loss), estimated_population * finite_loss, np.nan
    )

    group_columns = [
        "Scenario ID",
        "Hazard Scenario",
        "Minimum Evidence Class",
        "Road Closure Rule",
        "Facility Availability Rule",
        "Topology Repair Threshold (m)",
        "Maximum Settlement Snap Distance (m)",
    ]
    rows: list[dict[str, object]] = []
    for keys, group in detail.groupby(group_columns, sort=False, dropna=False):
        row = dict(zip(group_columns, keys, strict=True))
        finite = group["Accessibility Loss (minutes)"].notna()
        finite_population = float(
            group.loc[finite, "Estimated Settlement Population"].sum()
        )
        person_minutes = float(
            group["Population-Weighted Accessibility Loss (person-minutes)"].sum(
                min_count=1
            )
        )
        row.update(
            {
                "Allocated Settlement Population": float(
                    group["Estimated Settlement Population"].sum()
                ),
                "Baseline Eligible Population": float(
                    group["Baseline Eligible Population"].sum()
                ),
                "Post-Disruption Reachable Population": float(
                    group["Post-Disruption Reachable Population"].sum()
                ),
                "Newly Isolated Population": float(
                    group["Newly Isolated Population"].sum()
                ),
                "Population Delayed over 5 Minutes": float(
                    group["Population Delayed over 5 Minutes"].sum()
                ),
                "Population with Positive Accessibility Loss": float(
                    group["Population with Positive Accessibility Loss"].sum()
                ),
                "Population-Weighted Accessibility Loss (person-minutes)": person_minutes,
                "Population-Weighted Mean Finite Accessibility Loss (minutes)": (
                    person_minutes / finite_population
                    if finite_population > 0
                    else np.nan
                ),
                "Population Used for Finite Accessibility Loss": finite_population,
                "Population Allocation Threshold (m)": int(
                    group["Allocation Threshold (m)"].iloc[0]
                ),
                "Population Coverage Interpretation": (
                    "Settlement-level population metrics include only calibrated "
                    "population assigned within 3000 m inside the same allocation unit."
                ),
            }
        )
        rows.append(row)

    population_summary = pd.DataFrame(rows)
    summary = scenario_summary.merge(
        population_summary,
        on=group_columns,
        how="left",
        validate="one_to_one",
    )
    if summary["Newly Isolated Population"].isna().any():
        raise RuntimeError("Population summary did not match all accessibility scenarios.")
    if len(detail) != len(accessibility):
        raise RuntimeError("Population join changed the detail row count.")
    if detail.groupby("Scenario ID").size().nunique() != 1:
        raise RuntimeError("Scenario detail row counts are inconsistent.")
    if (summary["Newly Isolated Population"] < 0).any():
        raise RuntimeError("Negative isolated population detected.")
    if (
        summary["Post-Disruption Reachable Population"]
        + summary["Newly Isolated Population"]
        - summary["Baseline Eligible Population"]
    ).abs().max() > 1e-6:
        raise RuntimeError("Baseline-eligible population is not conserved after disruption.")
    if any(not str(column).isascii() for column in detail.columns):
        raise RuntimeError("Non-English detail column detected.")

    detail_path = root / OUTPUT_DETAIL
    summary_path = root / OUTPUT_SUMMARY
    audit_path = root / AUDIT
    detail_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    detail.to_parquet(detail_path, index=False)
    summary.to_parquet(summary_path, index=False)
    summary.to_csv(audit_path, index=False)

    display_columns = [
        "Scenario ID",
        "Newly Isolated Settlements",
        "Newly Isolated Population",
        "Settlements Delayed over 5 Minutes",
        "Population Delayed over 5 Minutes",
        "Population-Weighted Mean Finite Accessibility Loss (minutes)",
    ]
    print(summary[display_columns].to_string(index=False))
    print(
        {
            "detail": str(detail_path),
            "summary": str(summary_path),
            "audit": str(audit_path),
        }
    )


if __name__ == "__main__":
    main()
