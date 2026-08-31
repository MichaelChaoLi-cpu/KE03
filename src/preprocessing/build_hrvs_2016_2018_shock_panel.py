#!/usr/bin/env python3
"""Build the harmonized 2016-2018 HRVS household-shock panel."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
MODULES = ROOT / "data/processed/modules"
OUTPUT = ROOT / "data/processed/hrvs_2016_2018_shock_panel_preprocessed.parquet"
KEYS = ["Household ID", "PSU ID"]


def main() -> None:
    waves = []
    for wave, year in [(1, 2016), (2, 2017), (3, 2018)]:
        household = pd.read_parquet(MODULES / f"hrvs_wave_{wave}_section_0_preprocessed.parquet")
        shocks = pd.read_parquet(MODULES / f"hrvs_wave_{wave}_section_15a_preprocessed.parquet")
        if household.duplicated(KEYS).any():
            raise ValueError(f"Duplicate household keys in HRVS wave {wave}")
        result = shocks.merge(
            household[KEYS + ["Survey Weight"]], on=KEYS, how="left", validate="many_to_one"
        )
        result.insert(0, "Survey Year", year)
        result.insert(1, "Survey Wave", wave)
        waves.append(result)
    panel = pd.concat(waves, ignore_index=True, sort=False)
    expected = 7972 + 2627 + 1493
    if len(panel) != expected:
        raise ValueError(f"Expected {expected:,} shock rows; found {len(panel):,}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    panel.to_parquet(OUTPUT, index=False, engine="pyarrow")
    print(f"Saved {len(panel):,} rows x {len(panel.columns)} cols -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
