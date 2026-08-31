#!/usr/bin/env python3
"""Create a metadata-level briefing for Nepal survey files.

The script treats data/raw as read-only. It inventories every Stata file, records
SPSS files as alternate-format inputs, and screens variable names and labels for
disaster-research concepts without selecting final research variables.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd
import pyreadstat


DOMAIN_TERMS: dict[str, tuple[str, ...]] = {
    "geography": (
        "province", "district", "municipality", "municipal", "ward", "psu",
        "cluster", "vdc", "village", "region", "urban", "rural", "ecological",
        "latitude", "longitude", "location", "address", "area code", "stratum",
    ),
    "hazard_exposure": (
        "disaster", "shock", "flood", "landslide", "avalanche", "glacier",
        "drought", "earthquake", "storm", "rainfall", "heavy rain", "climate",
        "erosion", "hazard", "affected", "damage", "loss", "exposure", "risk",
    ),
    "vulnerability_welfare": (
        "poverty", "poor", "consumption", "food security", "food insecure",
        "income", "asset", "dwelling", "housing", "roof", "wall", "health",
        "disability", "education", "livelihood", "agriculture", "landholding",
        "livestock", "remittance", "social assistance", "coping", "loan", "debt",
        "migration", "access", "distance", "road", "hospital", "school", "market",
    ),
    "adaptation_preparedness": (
        "adaptation", "adapt", "preparedness", "prepared", "early warning",
        "warning", "evacuation", "insurance", "awareness", "perception",
        "response", "relief", "aid", "knowledge", "coping strategy", "resilience",
    ),
    "time": (
        "year", "month", "date", "wave", "season", "period", "day", "time",
    ),
}


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def classify_file(path: Path) -> tuple[str, str, bool]:
    text = path.as_posix()
    lower = text.lower()
    if "/niccs/climate-2022/" in lower:
        return "National Climate Change Survey", "2022", True
    if "/niccs/climate-2016/" in lower:
        detailed = "/data/data/" in lower and "/data_climate_change_survey/" not in lower
        return "National Climate Change Survey", "2016", detailed
    if "/nepal-vulnerability/" in lower:
        match = re.search(r"wave\s+(\d+)", text, flags=re.IGNORECASE)
        wave = f"201{5 + int(match.group(1))}" if match else "2016-2018"
        return "Household Risk and Vulnerability Survey", wave, True
    if "/nlss/nlss iv 2022_23/" in lower:
        return "Nepal Living Standards Survey", "2022-2023", "/stata format/" in lower
    if "/nlss/2011" in lower:
        return "Nepal Living Standards Survey", "2010-2011", False
    if "/nlss/2004/" in lower:
        return "Nepal Living Standards Survey", "2003-2004", False
    if "/nlss/1994/" in lower or "/nlss/nlss_sta-93/" in lower:
        return "Nepal Living Standards Survey", "1995-1996", False
    return "Other survey", "Unknown", False


def matched_domains(name: str, label: str) -> list[str]:
    text = f"{name} {label}".lower().replace("_", " ")
    matches: list[str] = []
    for domain, terms in DOMAIN_TERMS.items():
        if any(term in text for term in terms):
            matches.append(domain)
    return matches


def metadata_for(path: Path) -> tuple[Any, str | None]:
    try:
        _, meta = pyreadstat.read_dta(str(path), metadataonly=True)
        return meta, None
    except Exception as exc:  # noqa: BLE001
        return None, f"{type(exc).__name__}: {exc}"


def create_briefing(root: Path) -> dict[str, Any]:
    raw = root / "data" / "raw"
    output = root / "data" / "exp" / "data-briefing"
    tables = output / "tables"
    tables.mkdir(parents=True, exist_ok=True)

    all_files = [path for path in raw.rglob("*") if path.is_file()]
    dta_files = sorted(path for path in all_files if path.suffix.lower() == ".dta")
    sav_files = sorted(path for path in all_files if path.suffix.lower() == ".sav")
    inventory: list[dict[str, Any]] = []
    variables: list[dict[str, Any]] = []
    skipped: list[dict[str, str]] = []

    for path in dta_files:
        family, wave, detailed_scope = classify_file(path)
        meta, error = metadata_for(path)
        source = rel(root, path)
        if error:
            inventory.append(
                {
                    "survey_family": family,
                    "wave": wave,
                    "format": "dta",
                    "source_file": source,
                    "size_bytes": path.stat().st_size,
                    "rows": None,
                    "columns": None,
                    "detailed_scope": detailed_scope,
                    "read_status": "skipped",
                }
            )
            skipped.append({"source_file": source, "reason": error})
            continue

        names = list(meta.column_names or [])
        labels = list(meta.column_labels or [])
        if len(labels) < len(names):
            labels.extend([""] * (len(names) - len(labels)))
        inventory.append(
            {
                "survey_family": family,
                "wave": wave,
                "format": "dta",
                "source_file": source,
                "size_bytes": path.stat().st_size,
                "rows": meta.number_rows,
                "columns": len(names),
                "detailed_scope": detailed_scope,
                "read_status": "read",
            }
        )
        for name, label in zip(names, labels, strict=False):
            label_text = "" if label is None else str(label)
            domains = matched_domains(str(name), label_text)
            variables.append(
                {
                    "survey_family": family,
                    "wave": wave,
                    "source_file": source,
                    "variable": str(name),
                    "variable_label": label_text,
                    "domains": ";".join(domains),
                    "geographic_candidate": "geography" in domains,
                    "time_candidate": "time" in domains,
                    "detailed_scope": detailed_scope,
                }
            )

    for path in sav_files:
        family, wave, detailed_scope = classify_file(path)
        inventory.append(
            {
                "survey_family": family,
                "wave": wave,
                "format": "sav",
                "source_file": rel(root, path),
                "size_bytes": path.stat().st_size,
                "rows": None,
                "columns": None,
                "detailed_scope": detailed_scope,
                "read_status": "alternate_format_not_read",
            }
        )

    inventory_df = pd.DataFrame(inventory)
    variables_df = pd.DataFrame(variables)
    candidates_df = variables_df[variables_df["domains"].ne("")].copy()
    geography_df = variables_df[variables_df["geographic_candidate"]].copy()
    time_df = variables_df[variables_df["time_candidate"]].copy()

    inventory_df.to_csv(tables / "survey_file_inventory.csv", index=False)
    variables_df.to_csv(tables / "survey_variable_catalog.csv", index=False)
    candidates_df.to_csv(tables / "survey_candidate_variables.csv", index=False)
    geography_df.to_csv(tables / "survey_geographic_candidates.csv", index=False)
    time_df.to_csv(tables / "survey_time_candidates.csv", index=False)
    pd.DataFrame(skipped).to_csv(tables / "survey_skipped_files.csv", index=False)

    readable = inventory_df[inventory_df["read_status"].eq("read")]
    family_counts = readable.groupby(["survey_family", "wave"], dropna=False).agg(
        files=("source_file", "count"),
        min_rows=("rows", "min"),
        max_rows=("rows", "max"),
        variables=("columns", "sum"),
    ).reset_index()
    family_counts.to_csv(tables / "survey_family_summary.csv", index=False)

    domain_counts = Counter()
    for value in candidates_df["domains"]:
        domain_counts.update(value.split(";"))

    report = [
        "# Supplementary Survey Metadata Briefing",
        "",
        "This audit inventories Stata metadata without changing or rewriting raw survey files.",
        "SPSS files are recorded as alternate-format copies and are not read when Stata versions are available.",
        "",
        "## Coverage",
        "",
        f"- Stata files discovered: {len(dta_files)}",
        f"- Stata files readable: {len(readable)}",
        f"- SPSS alternate-format files recorded: {len(sav_files)}",
        f"- Variable records catalogued: {len(variables_df)}",
        f"- Candidate variable records: {len(candidates_df)}",
        f"- Geographic candidate records: {len(geography_df)}",
        f"- Time candidate records: {len(time_df)}",
        f"- Files skipped because of format errors: {len(skipped)}",
        "",
        "## Candidate Domains",
        "",
    ]
    for domain in DOMAIN_TERMS:
        report.append(f"- {domain}: {domain_counts.get(domain, 0)}")
    report.extend(
        [
            "",
            "## Interpretation Boundary",
            "",
            "Keyword screening identifies candidates for review; it does not select final variables or establish causal relationships.",
            "Geographic candidates must be checked for disclosure restrictions and compatibility with current administrative boundaries before spatial linkage.",
        ]
    )
    (output / "survey_metadata_README.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    return {
        "stata_files_found": len(dta_files),
        "stata_files_read": int(len(readable)),
        "spss_files_recorded": len(sav_files),
        "variables_catalogued": int(len(variables_df)),
        "candidate_variables": int(len(candidates_df)),
        "geographic_candidates": int(len(geography_df)),
        "time_candidates": int(len(time_df)),
        "skipped_files": len(skipped),
        "output": rel(root, output),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    result = create_briefing(Path(args.root).expanduser().resolve())
    print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
