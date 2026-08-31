#!/usr/bin/env python3
"""Create an auditable survey-variable selection and naming proposal.

This script is exploratory. It does not modify raw data or create processed data.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from typing import Any

import pandas as pd
import pyreadstat
from pandas.api.types import infer_dtype


NCCS = "data/raw/NICCS/Climate-2022/Data 2022/NCCS 2022/Data"
HRVS = (
    "data/raw/Nepal-Vulnerability/NPL_2016-2018_HRVS_v01_M_STATA12/"
    "NPL_2016-2018_HRVS_v01_M_STATA12"
)
NLSS = "data/raw/NLSS/NLSS IV 2022_23/data/stata format"


SPECS: list[dict[str, Any]] = [
    {
        "group": "NCCS 2022 Household Preparedness",
        "path": f"{NCCS}/S01.dta",
        "variables": ["psu", "hhld", "respsex", "respage", "a13", "a14", "a15", "b01"],
        "role": "identifier and household context",
        "status": "partly-testable for baseline vulnerability",
    },
    {
        "group": "NCCS 2022 Household Preparedness",
        "path": f"{NCCS}/S04.dta",
        "variables": [
            "psu", "hhld", "d01", "d02", "d03", "d04", "d07", "d09", "d10",
            "d11", "d12", "d13", "d14", "d15", "d16", "d17",
        ],
        "role": "financial, social, and service-access capacity",
        "status": "partly-testable for baseline vulnerability",
    },
    {
        "group": "NCCS 2022 Household Preparedness",
        "path": f"{NCCS}/S06.dta",
        "variables": ["psu", "hhld", "f01", "f06", "f07", "f08", "f09a", "f09b", "f09c", "f09d", "f09e"],
        "role": "warning and preparedness",
        "status": "partly-testable for baseline vulnerability",
    },
    {
        "group": "NCCS 2022 Household Preparedness",
        "path": f"{NCCS}/S11.dta",
        "variables": [
            "psu", "hhld", "k01", "k16", "k19", "k31", "k32", "k36", "k38",
            "k39", "k40", "k41", "k42", "k43", "k44", "k45",
        ],
        "role": "adaptation and risk reduction",
        "status": "partly-testable for baseline vulnerability",
    },
    {
        "group": "NCCS 2022 Household Preparedness",
        "path": f"{NCCS}/Weight.dta",
        "variables": [
            "PSU", "HHLD", "AltGrp", "RiskRating", "Prov", "ProvName", "Stratrum",
            "StratrumName", "UrbRur", "EcoBelt", "Wght",
        ],
        "role": "survey design, supported geography, and weight",
        "status": "required reference variables",
    },
    {
        "group": "NCCS 2022 Disaster Experience",
        "path": f"{NCCS}/S06_3.dta",
        "variables": [
            "psu", "hhld", "f15sn", "f16desc", "f17", "f18", "f19a", "f19b",
            "f19c", "f20a", "f20b", "f20c",
        ],
        "role": "historical disaster incidence and prevention",
        "status": "partly-testable for historical vulnerability",
    },
    {
        "group": "NCCS 2022 Disaster Experience",
        "path": f"{NCCS}/S07_1.dta",
        "variables": [
            "psu", "hhld", "g01sn", "g02desc", "g03yr", "g04", "g05", "g06",
            "g07", "g08", "g09", "g10", "g11", "g12", "g13", "g14",
        ],
        "role": "historical human and livelihood effects",
        "status": "partly-testable for historical vulnerability",
    },
    {
        "group": "NCCS 2022 Disaster Experience",
        "path": f"{NCCS}/S07_2.dta",
        "variables": [
            "psu", "hhld", "g15sn", "g16desc", "g17yn", "g18", "g19", "g20",
            "g21", "g22", "g23", "g24", "g25", "g26",
        ],
        "role": "historical monetary losses",
        "status": "partly-testable for historical vulnerability",
    },
    {
        "group": "NLSS IV Household Vulnerability",
        "path": f"{NLSS}/poverty.dta",
        "variables": [
            "psu_number", "hh_number", "prov", "domain", "hhsize", "hhs_wt", "ind_wt",
            "ad_4", "paasche", "pcep_food", "pcep_nonfood", "pcep", "pline", "fpline",
            "nfpline", "poor", "quintile_pcep",
        ],
        "role": "poverty, expenditure, and survey design",
        "status": "partly-testable for baseline vulnerability",
    },
    {
        "group": "NLSS IV Household Vulnerability",
        "path": f"{NLSS}/S17.dta",
        "variables": [
            "psu_number", "hh_number", "q17_01", "q17_02", "q17_03", "q17_04", "q17_05",
            "q17_06_a", "q17_06_b", "q17_07_a", "q17_07_b", "q17_08_a", "q17_08_b",
            "q17_09_a", "q17_09_b", "q17_10_a", "q17_10_b", "q17_11_a", "q17_11_b",
            "q17_12_a", "q17_12_b", "q17_13_a", "q17_13_b",
        ],
        "role": "subjective welfare and service constraints",
        "status": "partly-testable for baseline vulnerability",
    },
    {
        "group": "NLSS IV Facility Access",
        "path": f"{NLSS}/S03.dta",
        "variables": [
            "psu_number", "dist_name", "hh_number", "s03_code", "s03_desc", "q03_01",
            "q03_02_a", "q03_02_b", "q03_02_c", "q03_03", "q03_04",
        ],
        "role": "facility-specific travel and use",
        "status": "partly-testable for service accessibility",
    },
]


HRVS_SHOCK_VARIABLES = [
    "hhid", "psu", "district", "vdc", "shockid", "s15q02", "s15q03", "s15q04",
    "s15q05a", "s15q07a", "s15q08a", "s15q09a", "s15q10a", "s15q10b_1",
    "s15q10b_2", "s15q10b_3", "s15q10b_4", "s15q10b_5", "s15q10b_6",
    "s15q10c_1", "s15q10c_2", "s15q10c_3", "s15q10d", "s15q10e", "s15q11a",
    "s15q12a", "s15q13a", "s15q13b",
]

for wave, year in [(1, 2016), (2, 2017), (3, 2018)]:
    SPECS.extend(
        [
            {
                "group": "HRVS 2016-2018 Shock Panel",
                "path": f"{HRVS}/Wave {wave} - Household/Section_0.dta",
                "variables": ["hhid", "psu", "district", "vdc", "wt_hh"],
                "role": f"wave {year} identifiers and survey weight",
                "status": "required panel reference variables",
            },
            {
                "group": "HRVS 2016-2018 Shock Panel",
                "path": f"{HRVS}/Wave {wave} - Household/Section_15a.dta",
                "variables": HRVS_SHOCK_VARIABLES,
                "role": f"wave {year} shock loss, assistance, and coping",
                "status": "partly-testable for historical coping",
            },
        ]
    )


NAME_OVERRIDES = {
    "psu": "PSU ID",
    "PSU": "PSU ID",
    "psu_number": "PSU ID",
    "hhld": "Household ID",
    "HHLD": "Household ID",
    "hh_number": "Household ID",
    "hhid": "Household ID",
    "dist_name": "District",
    "district": "District",
    "vdc": "VDC",
    "Wght": "Survey Weight",
    "wt_hh": "Survey Weight",
    "hhs_wt": "Household Survey Weight",
    "ind_wt": "Individual Survey Weight",
    "Prov": "Province Code",
    "prov": "Province Code",
    "ProvName": "Province",
    "UrbRur": "Urban Rural Classification",
    "EcoBelt": "Ecological Belt",
    "AltGrp": "Altitude Group",
    "Stratrum": "Stratum ID",
    "StratrumName": "Stratum",
    "shockid": "Shock Type",
    "poor": "Poverty Status",
    "pcep": "Per Capita Expenditure",
    "pcep_food": "Per Capita Food Expenditure",
    "pcep_nonfood": "Per Capita Nonfood Expenditure",
}

REFERENCE_NAMES = {
    "PSU ID",
    "Household ID",
    "District",
    "VDC",
    "Survey Weight",
    "Household Survey Weight",
    "Individual Survey Weight",
    "Province Code",
    "Province",
    "Stratum ID",
    "Stratum",
    "FACILITY CODE",
}


def ascii_clean(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"^\s*(?:\{[^}]+\}|[A-Za-z]?\d+(?:\.\d+)?[A-Za-z]?)\s*[.:]?\s*", "", value)
    value = value.replace("&", "and").replace("'", "")
    value = re.sub(r"[^A-Za-z0-9 .,_%/()+-]+", " ", value)
    return re.sub(r"\s+", " ", value).strip(" .")


def suggested_name(variable: str, label: str) -> str:
    if variable in NAME_OVERRIDES:
        return NAME_OVERRIDES[variable]
    cleaned = ascii_clean(label)
    return cleaned if cleaned else variable.replace("_", " ").title()


def run(root: Path) -> dict[str, int]:
    rows: list[dict[str, Any]] = []

    for spec in SPECS:
        source = root / spec["path"]
        frame, metadata = pyreadstat.read_dta(
            str(source), usecols=spec["variables"], apply_value_formats=True
        )
        labels = dict(zip(metadata.column_names or [], metadata.column_labels or [], strict=False))
        used_names: dict[str, int] = {}
        for variable in spec["variables"]:
            if variable not in labels:
                continue
            name = suggested_name(variable, "" if labels.get(variable) is None else str(labels[variable]))
            normalized = re.sub(r"\s+", " ", name).casefold()
            used_names[normalized] = used_names.get(normalized, 0) + 1
            if used_names[normalized] > 1:
                name = f"{name} ({variable})"
            series = frame[variable]
            dtype = str(series.dtype)
            null_pct = round(float(series.isna().mean() * 100), 1) if len(series) else 0.0
            sample = ", ".join(str(value)[:20] for value in series.dropna().head(3).tolist())
            if null_pct == 100.0:
                continue
            prep = "none"
            inferred = infer_dtype(series.astype(object).dropna(), skipna=True)
            if str(dtype) == "category":
                if inferred in {"mixed", "mixed-integer", "mixed-integer-float"}:
                    prep = "decode labels; to_string"
                else:
                    prep = "decode labels; to_category"
            elif str(dtype) == "str" or inferred in {"string", "unicode", "bytes"}:
                prep = "strip_whitespace"
            rows.append(
                {
                    "output_group": spec["group"],
                    "source_dataset": spec["path"],
                    "original_name": variable,
                    "readable_name": name,
                    "full_name": name,
                    "dtype": dtype,
                    "null_pct": null_pct,
                    "sample_values": sample,
                    "feasibility_status": spec["status"],
                    "research_role": spec["role"],
                    "proposed_preprocessing": prep,
                    "proposed_final_variable": (
                        "no" if name in REFERENCE_NAMES or name.endswith("S.No") else "yes"
                    ),
                }
            )

    output = root / "data/exp/data-preprocessing"
    output.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    frame.to_csv(output / "selection_proposal.csv", index=False)

    lines = [
        "# Survey Preprocessing Selection Proposal",
        "",
        "This is a proposal for user confirmation. No raw or processed data were changed.",
        "",
        "## Common Rules",
        "",
        "- Preserve identifiers and survey weights; do not impute them.",
        "- Decode labelled categories to readable English values while retaining auditable source mappings in scripts.",
        "- Do not impute missing values, clip loss amounts, or apply logarithms at this stage.",
        "- Exclude personal names, contact information, and masked public geocodes.",
        "- Add survey year or wave when harmonizing repeated observations.",
        "",
    ]
    for group, part in frame.groupby("output_group", sort=False):
        lines.extend(
            [
                f"## {group}",
                "",
                f"Proposed source modules: {part['source_dataset'].nunique()}; proposed source-variable rows: {len(part)}.",
                "",
                "| original_name | readable_name | dtype | null_pct | feasibility_status | sample_values |",
                "|---|---|---|---:|---|---|",
            ]
        )
        for row in part.itertuples(index=False):
            sample = str(row.sample_values).replace("|", "/")[:42]
            lines.append(
                f"| {row.original_name} | {row.readable_name} | {row.dtype} | {row.null_pct} | "
                f"{row.feasibility_status} | {sample} |"
            )
        lines.append("")
    (output / "selection_proposal.md").write_text("\n".join(lines), encoding="utf-8")
    return {
        "output_groups": int(frame["output_group"].nunique()),
        "source_modules": int(frame["source_dataset"].nunique()),
        "source_variable_rows": int(len(frame)),
        "unique_readable_names": int(frame[["output_group", "readable_name"]].drop_duplicates().shape[0]),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    result = run(Path(args.root).expanduser().resolve())
    for key, value in result.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
