#!/usr/bin/env python3
"""Build the NLSS IV facility-access long dataset."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "data/processed/modules/nlss_iv_s03_preprocessed.parquet"
OUTPUT = ROOT / "data/processed/nlss_iv_facility_access_preprocessed.parquet"
KEYS = ["PSU ID", "Household ID", "FACILITY CODE"]


def main() -> None:
    result = pd.read_parquet(MODULE)
    if result.duplicated(KEYS).any():
        raise ValueError("Duplicate household-facility keys in facility-access data")
    if len(result) != 220800:
        raise ValueError(f"Expected 220,800 household-facility rows; found {len(result):,}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_parquet(OUTPUT, index=False, engine="pyarrow")
    print(f"Saved {len(result):,} rows x {len(result.columns)} cols -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
