#!/usr/bin/env python3
"""Convert the approved survey selection proposal into decisions.json."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd


def source_slug(source: str) -> str:
    stem = Path(source).stem.lower()
    if "Climate-2022" in source:
        return f"nccs_2022_{stem}"
    if "NLSS IV 2022_23" in source:
        return f"nlss_iv_{stem}"
    wave_match = re.search(r"Wave (\d+)", source)
    if wave_match:
        return f"hrvs_wave_{wave_match.group(1)}_{stem}"
    return re.sub(r"[^a-z0-9]+", "_", stem).strip("_")


def run(root: Path) -> dict[str, int]:
    proposal_path = root / "data/exp/data-preprocessing/selection_proposal.csv"
    proposal = pd.read_csv(proposal_path, keep_default_na=False)
    datasets: dict[str, dict] = {}

    for source, part in proposal.groupby("source_dataset", sort=False):
        slug = source_slug(source)
        variables = []
        for row in part.itertuples(index=False):
            preprocessing: list[str] = []
            if row.proposed_preprocessing == "strip_whitespace":
                preprocessing = ["strip_whitespace"]
            elif row.proposed_preprocessing == "decode labels; to_category":
                preprocessing = ["to_category"]
            elif row.proposed_preprocessing == "decode labels; to_string":
                preprocessing = ["to_string"]
            variables.append(
                {
                    "original_name": row.original_name,
                    "readable_name": row.readable_name,
                    "full_name": row.full_name,
                    "is_final_variable": row.proposed_final_variable,
                    "preprocessing": preprocessing,
                    "research_role": row.research_role,
                    "output_group": row.output_group,
                }
            )
        datasets[source] = {
            "output": f"data/processed/modules/{slug}_preprocessed.parquet",
            "script": f"src/preprocessing/preprocess_{slug}.py",
            "output_group": part.iloc[0]["output_group"],
            "variables": variables,
        }

    decisions = {
        "approval": {
            "status": "confirmed",
            "rules": [
                "preserve identifiers and survey weights",
                "decode labelled categories to readable English values",
                "do not impute missing values",
                "do not clip monetary losses",
                "do not apply logarithmic transformations",
                "exclude personal identifiers, masked public geocodes, and fully missing variables",
            ],
        },
        "datasets": datasets,
    }
    output = root / "data/exp/data-preprocessing/decisions.json"
    output.write_text(json.dumps(decisions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "datasets": len(datasets),
        "variables": sum(len(item["variables"]) for item in datasets.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    result = run(Path(args.root).expanduser().resolve())
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
