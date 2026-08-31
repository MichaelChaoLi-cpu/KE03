#!/usr/bin/env python3
"""Build the consolidated NCCS 2022 historical disaster-experience dataset."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
MODULES = ROOT / "data/processed/modules"
OUTPUT = ROOT / "data/processed/nccs_2022_disaster_experience_preprocessed.parquet"
HOUSEHOLD_KEYS = ["PSU ID", "Household ID"]


def with_event_key(frame: pd.DataFrame, source_column: str) -> pd.DataFrame:
    result = frame.copy()
    result["_event_key"] = result[source_column].astype("string")
    return result


def main() -> None:
    incidence = with_event_key(
        pd.read_parquet(MODULES / "nccs_2022_s06_3_preprocessed.parquet"), "F.15 S.No"
    )
    effects = with_event_key(
        pd.read_parquet(MODULES / "nccs_2022_s07_1_preprocessed.parquet"), "G.01 S.No"
    )
    losses = with_event_key(
        pd.read_parquet(MODULES / "nccs_2022_s07_2_preprocessed.parquet"), "G.15 S.No"
    )
    event_keys = HOUSEHOLD_KEYS + ["_event_key"]
    for name, frame in [("incidence", incidence), ("effects", effects), ("losses", losses)]:
        if frame.duplicated(event_keys).any():
            raise ValueError(f"Duplicate household-event keys in {name}")
    result = incidence.merge(effects, on=event_keys, how="inner", validate="one_to_one")
    result = result.merge(losses, on=event_keys, how="inner", validate="one_to_one")
    weights = pd.read_parquet(
        MODULES / "nccs_2022_weight_preprocessed.parquet",
        columns=HOUSEHOLD_KEYS + ["Survey Weight"],
    )
    result = result.merge(weights, on=HOUSEHOLD_KEYS, how="left", validate="many_to_one")
    result = result.drop(columns="_event_key")
    if len(result) != 123652:
        raise ValueError(f"Expected 123,652 household-event rows; found {len(result):,}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_parquet(OUTPUT, index=False, engine="pyarrow")
    print(f"Saved {len(result):,} rows x {len(result.columns)} cols -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
