#!/usr/bin/env python3
"""Update only AnaSOP Section 4 from confirmed preprocessing decisions."""

from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from pathlib import Path


def construction_text(operations: list[str]) -> str:
    if "to_string" in operations:
        return "Decoded from approved value labels and stored as string to preserve mixed labels."
    if "to_category" in operations:
        return "Decoded from approved value labels and stored as a labelled category."
    if "strip_whitespace" in operations:
        return "Retained as text with leading and trailing whitespace removed."
    return "Retained in the source scale with no imputation, clipping, or transformation."


def run(root: Path) -> dict[str, int]:
    decisions = json.loads(
        (root / "data/exp/data-preprocessing/decisions.json").read_text(encoding="utf-8")
    )
    variables: OrderedDict[str, dict] = OrderedDict()
    for dataset in decisions["datasets"].values():
        for variable in dataset["variables"]:
            if variable["is_final_variable"] != "yes":
                continue
            name = variable["readable_name"]
            if name not in variables:
                variables[name] = variable

    section = [
        "## 4. Variable Construction  /  Key Variables",
        "",
        "The table records the approved initial survey variables. Roles and formal definitions may be refined after spatial data acquisition and figure-table planning.",
        "",
        "| variable_name | full_name | role | formal_definition | construction_or_coding | is_final_variable |",
        "|---|---|---|---|---|---|",
    ]
    for name, variable in variables.items():
        values = [
            name,
            variable["full_name"],
            variable.get("research_role", "TBD"),
            "TBD",
            construction_text(variable.get("preprocessing", [])),
            "yes",
        ]
        escaped = [str(value).replace("|", "\\|") for value in values]
        section.append("| " + " | ".join(escaped) + " |")

    path = root / "docs/AnaSOP.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines) if line.strip() == section[0]), None)
    if start is None:
        lines.extend([""] + section)
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        lines[start:end] = section
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {"final_variables": len(variables)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    print(run(Path(args.root).expanduser().resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
