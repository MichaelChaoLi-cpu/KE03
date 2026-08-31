#!/usr/bin/env python3
"""Build the consolidated NCCS 2022 household preparedness dataset."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
MODULES = ROOT / "data/processed/modules"
OUTPUT = ROOT / "data/processed/nccs_2022_household_preparedness_preprocessed.parquet"
KEYS = ["PSU ID", "Household ID"]


def main() -> None:
    paths = [
        MODULES / "nccs_2022_weight_preprocessed.parquet",
        MODULES / "nccs_2022_s01_preprocessed.parquet",
        MODULES / "nccs_2022_s04_preprocessed.parquet",
        MODULES / "nccs_2022_s06_preprocessed.parquet",
        MODULES / "nccs_2022_s11_preprocessed.parquet",
    ]
    frames = [pd.read_parquet(path) for path in paths]
    for path, frame in zip(paths, frames, strict=True):
        if frame.duplicated(KEYS).any():
            raise ValueError(f"Duplicate household keys in {path.name}")
    result = frames[0]
    for frame in frames[1:]:
        result = result.merge(frame, on=KEYS, how="inner", validate="one_to_one")
    if len(result) != 6508:
        raise ValueError(f"Expected 6,508 households; found {len(result):,}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_parquet(OUTPUT, index=False, engine="pyarrow")
    print(f"Saved {len(result):,} rows x {len(result.columns)} cols -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
