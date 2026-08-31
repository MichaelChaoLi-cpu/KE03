#!/usr/bin/env python3
"""Generate focused exploratory summaries for disaster-relevant survey modules."""

from __future__ import annotations

import argparse
import json
import math
import os
import tempfile
from pathlib import Path
from typing import Any

import pandas as pd
import pyreadstat

cache_root = Path(tempfile.gettempdir()) / "miliframe_cache"
cache_root.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("XDG_CACHE_HOME", str(cache_root))
os.environ.setdefault("MPLCONFIGDIR", str(cache_root / "matplotlib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


NCCS_BASE = "data/raw/NICCS/Climate-2022/Data 2022/NCCS 2022/Data"
HRVS_BASE = (
    "data/raw/Nepal-Vulnerability/NPL_2016-2018_HRVS_v01_M_STATA12/"
    "NPL_2016-2018_HRVS_v01_M_STATA12"
)
NLSS4_BASE = "data/raw/NLSS/NLSS IV 2022_23/data/stata format"


MODULES: list[dict[str, Any]] = [
    {
        "dataset": "NCCS 2022",
        "module": "location",
        "path": f"{NCCS_BASE}/S01.dta",
        "variables": ["psu", "prov", "dist", "ward", "latitude", "longitude"],
    },
    {
        "dataset": "NCCS 2022",
        "module": "service_access",
        "path": f"{NCCS_BASE}/S04.dta",
        "variables": ["d11", "d12", "d13", "d14", "d15", "d16"],
    },
    {
        "dataset": "NCCS 2022",
        "module": "warning_preparedness",
        "path": f"{NCCS_BASE}/S06.dta",
        "variables": ["f01", "f06", "f07", "f08"],
    },
    {
        "dataset": "NCCS 2022",
        "module": "disaster_experience",
        "path": f"{NCCS_BASE}/S06_3.dta",
        "variables": ["f16desc", "f17", "f18", "f20a", "f20b", "f20c"],
    },
    {
        "dataset": "NCCS 2022",
        "module": "disaster_effects",
        "path": f"{NCCS_BASE}/S07_1.dta",
        "variables": ["g02desc", "g03yr", "g04", "g05", "g09", "g10", "g11", "g12", "g13", "g14"],
    },
    {
        "dataset": "NCCS 2022",
        "module": "monetary_losses",
        "path": f"{NCCS_BASE}/S07_2.dta",
        "variables": ["g16desc", "g17yn", "g18", "g19", "g20", "g21", "g22", "g23", "g24", "g25", "g26"],
    },
    {
        "dataset": "NCCS 2022",
        "module": "adaptation",
        "path": f"{NCCS_BASE}/S11.dta",
        "variables": ["k01", "k07", "k16", "k19", "k31", "k36", "k42", "k43", "k45"],
    },
    {
        "dataset": "NCCS 2022",
        "module": "weights_and_risk",
        "path": f"{NCCS_BASE}/Weight.dta",
        "variables": ["PSU", "RiskRating", "Prov", "ProvName", "UrbRur", "EcoBelt", "Wght"],
    },
    {
        "dataset": "NLSS IV 2022-2023",
        "module": "facility_access",
        "path": f"{NLSS4_BASE}/S03.dta",
        "variables": ["psu_number", "dist_name", "s03_code", "s03_desc", "q03_01", "q03_02_a", "q03_02_b", "q03_02_c", "q03_03", "q03_04"],
    },
    {
        "dataset": "NLSS IV 2022-2023",
        "module": "service_assessment",
        "path": f"{NLSS4_BASE}/S17.dta",
        "variables": ["psu_number", "q17_03", "q17_04", "q17_06_a", "q17_06_b", "q17_08_a", "q17_08_b", "q17_10_a", "q17_10_b"],
    },
    {
        "dataset": "NLSS IV 2022-2023",
        "module": "poverty",
        "path": f"{NLSS4_BASE}/poverty.dta",
        "variables": ["psu_number", "prov", "ad_4", "pcep_food", "pcep_nonfood", "pcep", "pline", "poor"],
    },
    {
        "dataset": "NLSS IV 2022-2023",
        "module": "weights",
        "path": f"{NLSS4_BASE}/weight.dta",
        "variables": ["psu_number", "urbrur", "prov_name", "prov_code", "hhs_wt"],
    },
]

for wave_number, year in [(1, 2016), (2, 2017), (3, 2018)]:
    wave = f"Wave {wave_number}"
    MODULES.extend(
        [
            {
                "dataset": f"HRVS {year}",
                "module": "community_location",
                "path": f"{HRVS_BASE}/{wave} - Community/Section_0.dta",
                "variables": ["district", "psu", "s00q01"],
            },
            {
                "dataset": f"HRVS {year}",
                "module": "community_shocks",
                "path": f"{HRVS_BASE}/{wave} - Community/Section_4a.dta",
                "variables": ["district", "psu", "shockid", "s04q02", "s04q03", "s04q04"],
            },
            {
                "dataset": f"HRVS {year}",
                "module": "household_shocks_and_coping",
                "path": f"{HRVS_BASE}/{wave} - Household/Section_15a.dta",
                "variables": [
                    "hhid", "district", "vdc", "psu", "shockid", "s15q02", "s15q03",
                    "s15q04", "s15q05a", "s15q07a", "s15q08a", "s15q09a", "s15q10a",
                    "s15q10b_3", "s15q10b_4", "s15q10b_6", "s15q10e", "s15q13a", "s15q13b",
                ],
            },
        ]
    )


NO_PLOT = {
    "psu", "PSU", "psu_number", "hhid", "prov", "Prov", "prov_code",
    "dist", "district", "dist_name", "ward", "vdc", "s00q01", "latitude", "longitude",
}


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def safe(value: str) -> str:
    return "".join(char if char.isalnum() or char in "-_" else "_" for char in value).strip("_")


def summarize_series(
    dataset: str,
    module: str,
    source: str,
    variable: str,
    label: str,
    series: pd.Series,
    value_labels: dict[Any, str],
) -> dict[str, Any]:
    total = len(series)
    non_missing = series.dropna()
    numeric = pd.to_numeric(non_missing, errors="coerce")
    top = non_missing.value_counts(dropna=False).head(10)
    top_values: list[dict[str, Any]] = []
    for key, count in top.items():
        label_value = value_labels.get(key)
        if label_value is None and isinstance(key, (int, float)):
            label_value = value_labels.get(float(key))
        top_values.append(
            {
                "value": str(key),
                "label": "" if label_value is None else str(label_value),
                "count": int(count),
            }
        )
    return {
        "dataset": dataset,
        "module": module,
        "source_file": source,
        "variable": variable,
        "variable_label": label,
        "rows": total,
        "non_missing": int(non_missing.size),
        "missing": int(series.isna().sum()),
        "missing_pct": round(float(series.isna().mean()), 6) if total else None,
        "unique": int(non_missing.nunique()),
        "mean": float(numeric.mean()) if numeric.notna().any() else None,
        "std": float(numeric.std()) if numeric.notna().sum() > 1 else None,
        "min": float(numeric.min()) if numeric.notna().any() else None,
        "median": float(numeric.median()) if numeric.notna().any() else None,
        "max": float(numeric.max()) if numeric.notna().any() else None,
        "top_values_json": json.dumps(top_values, ensure_ascii=False),
    }


def plot_distribution(
    series: pd.Series,
    value_labels: dict[Any, str],
    title: str,
    output_path: Path,
) -> bool:
    clean = series.dropna()
    if clean.empty or clean.nunique() <= 1:
        return False
    unique = clean.nunique()
    fig, ax = plt.subplots(figsize=(9, 5.5))
    if unique <= 20:
        counts = clean.value_counts().head(20)
        labels: list[str] = []
        for key in counts.index:
            mapped = value_labels.get(key)
            if mapped is None and isinstance(key, (int, float)):
                mapped = value_labels.get(float(key))
            labels.append(str(mapped) if mapped is not None else str(key))
        positions = list(range(len(counts)))
        ax.bar(positions, counts.values, color="#4472C4")
        ax.set_xticks(positions, labels, rotation=40, ha="right")
        ax.set_ylabel("Count")
    else:
        numeric = pd.to_numeric(clean, errors="coerce").dropna()
        if numeric.empty:
            counts = clean.astype(str).value_counts().head(20)
            counts.sort_values().plot(kind="barh", ax=ax, color="#5B9BD5")
            ax.set_xlabel("Count")
        else:
            bins = min(50, max(10, int(math.sqrt(len(numeric)))))
            ax.hist(numeric, bins=bins, color="#4472C4", edgecolor="white")
            ax.set_ylabel("Count")
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)
    return True


def update_anasop(root: Path, metrics: dict[str, Any]) -> None:
    path = root / "docs" / "AnaSOP.md"
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else ["# AnaSOP", "Analysis Standard Operating Procedure", ""]
    section = [
        "## 3. Data Overview",
        "",
        "### Data Scope",
        "",
        "- The available evidence comprises three principal household-survey families, repeated survey years, spatial boundary layers, and supporting questionnaires and reports.",
        f"- The metadata audit read {metrics['stata_read']} Stata modules and catalogued {metrics['variables_catalogued']} variable records.",
        f"- Focused descriptive screening summarized {metrics['focused_variables']} disaster-relevant candidate variables and generated {metrics['plots']} distribution plots.",
        "- The most recent climate-focused survey preserves PSU, province, ecological-belt, and risk-stratum identifiers, but the public district, ward, latitude, and longitude values are masked; direct raster linkage requires a restricted PSU-coordinate file or a verified administrative crosswalk.",
        "- A three-wave household panel contains repeated shock, loss, coping, assistance, and welfare measures with district and PSU identifiers.",
        "- The latest living-standards survey contains poverty, service access, transport, housing, and welfare measures with PSU and broader geographic identifiers.",
        "",
        "### Time-Series Candidates",
        "",
        f"Potential temporal structure was detected in {metrics['time_candidates']} variable records, including repeated survey waves and event-recall fields.",
        "Time-series visualizations have not been generated pending explicit user confirmation.",
        "",
        "### Data Limitations",
        "",
        "- Survey modules are relational and their row counts are not additive; household, person, plot, event, and community files have different units of observation.",
        "- Public NCCS 2022 district and ward values are constant zero and its latitude and longitude values are also zero; field names alone must not be interpreted as usable geocodes.",
        "- Public-use geographic identifiers may be subject to disclosure restrictions and must be validated before household-level spatial outputs are released.",
        "- Some local boundary layers use superseded administrative systems and require replacement or crosswalks to current administrative units.",
        "- Existing surveys predate the 2026 disaster and cannot by themselves identify realized household impacts from that event without new follow-up outcomes.",
        "- Candidate screening is exploratory and does not constitute final variable selection or causal evidence.",
        "- Technical source names, paths, and original variable names are retained only in the data-briefing artifacts.",
    ]
    start = next((i for i, line in enumerate(lines) if line.strip() == "## 3. Data Overview"), None)
    if start is None:
        if lines and lines[-1].strip():
            lines.append("")
        lines.extend(section)
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        lines[start:end] = section
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def run(root: Path) -> dict[str, Any]:
    output = root / "data" / "exp" / "data-briefing"
    tables = output / "tables"
    figures = output / "figures" / "survey-distributions"
    tables.mkdir(parents=True, exist_ok=True)
    figures.mkdir(parents=True, exist_ok=True)
    summaries: list[dict[str, Any]] = []
    plot_rows: list[dict[str, str]] = []
    module_rows: list[dict[str, Any]] = []
    skipped: list[dict[str, str]] = []

    for spec in MODULES:
        path = root / spec["path"]
        if not path.exists():
            skipped.append({"source_file": spec["path"], "reason": "file not found"})
            continue
        try:
            _, metadata = pyreadstat.read_dta(str(path), metadataonly=True)
            available = set(metadata.column_names or [])
            requested = [name for name in spec["variables"] if name in available]
            missing_requested = [name for name in spec["variables"] if name not in available]
            frame, metadata = pyreadstat.read_dta(str(path), usecols=requested)
        except Exception as exc:  # noqa: BLE001
            skipped.append({"source_file": spec["path"], "reason": f"{type(exc).__name__}: {exc}"})
            continue

        labels = dict(zip(metadata.column_names or [], metadata.column_labels or [], strict=False))
        value_label_maps = metadata.variable_value_labels or {}
        module_rows.append(
            {
                "dataset": spec["dataset"],
                "module": spec["module"],
                "source_file": spec["path"],
                "rows": len(frame),
                "variables_read": len(requested),
                "requested_not_found": ";".join(missing_requested),
            }
        )
        for variable in requested:
            label = "" if labels.get(variable) is None else str(labels.get(variable))
            series = frame[variable]
            value_labels = value_label_maps.get(variable, {})
            summaries.append(
                summarize_series(
                    spec["dataset"], spec["module"], spec["path"], variable, label, series, value_labels
                )
            )
            if variable in NO_PLOT:
                continue
            plot_name = f"{safe(spec['dataset'])}__{safe(spec['module'])}__{safe(variable)}.png"
            plot_path = figures / plot_name
            if plot_distribution(series, value_labels, f"{spec['dataset']} — {label or variable}", plot_path):
                plot_rows.append(
                    {
                        "dataset": spec["dataset"],
                        "module": spec["module"],
                        "variable": variable,
                        "variable_label": label,
                        "plot_file": rel(output, plot_path),
                    }
                )

    summary_df = pd.DataFrame(summaries)
    modules_df = pd.DataFrame(module_rows)
    plots_df = pd.DataFrame(plot_rows)
    summary_df.to_csv(tables / "survey_selected_variable_summary.csv", index=False)
    modules_df.to_csv(tables / "survey_focused_module_inventory.csv", index=False)
    plots_df.to_csv(tables / "survey_distribution_plot_inventory.csv", index=False)
    pd.DataFrame(skipped).to_csv(tables / "survey_detail_skipped_files.csv", index=False)

    location_source = root / f"{NCCS_BASE}/S01.dta"
    location, _ = pyreadstat.read_dta(
        str(location_source), usecols=["psu", "prov", "dist", "ward", "latitude", "longitude"]
    )
    valid_coords = location["latitude"].between(26, 31) & location["longitude"].between(80, 89)
    geographic = pd.DataFrame(
        [
            {
                "dataset": "NCCS 2022",
                "rows": len(location),
                "unique_psu": location["psu"].nunique(dropna=True),
                "unique_province": location["prov"].nunique(dropna=True),
                "unique_district": location["dist"].nunique(dropna=True),
                "unique_ward": location["ward"].nunique(dropna=True),
                "valid_coordinate_rows": int(valid_coords.sum()),
                "missing_coordinate_rows": int(location[["latitude", "longitude"]].isna().any(axis=1).sum()),
                "latitude_min": location.loc[valid_coords, "latitude"].min(),
                "latitude_max": location.loc[valid_coords, "latitude"].max(),
                "longitude_min": location.loc[valid_coords, "longitude"].min(),
                "longitude_max": location.loc[valid_coords, "longitude"].max(),
            }
        ]
    )
    geographic.to_csv(tables / "survey_geographic_coverage_summary.csv", index=False)

    event_area_rows: list[dict[str, Any]] = []
    for wave_number, year in [(1, 2016), (2, 2017), (3, 2018)]:
        household_source = root / f"{HRVS_BASE}/Wave {wave_number} - Household/Section_0.dta"
        household, _ = pyreadstat.read_dta(
            str(household_source), usecols=["hhid", "psu", "district"], apply_value_formats=True
        )
        for district_name in ["Nuwakot", "Rasuwa"]:
            selected = household[
                household["district"].astype(str).str.casefold() == district_name.casefold()
            ]
            event_area_rows.append(
                {
                    "dataset": f"HRVS {year}",
                    "district": district_name,
                    "households": selected["hhid"].nunique(dropna=True),
                    "unique_psu": selected["psu"].nunique(dropna=True),
                    "interpretation": "panel coverage" if not selected.empty else "not sampled",
                }
            )

    nlss_source = root / f"{NLSS4_BASE}/S03.dta"
    nlss, _ = pyreadstat.read_dta(
        str(nlss_source), usecols=["psu_number", "dist_name", "hh_number"]
    )
    for district_name in ["Nuwakot", "Rasuwa"]:
        selected = nlss[
            nlss["dist_name"].astype(str).str.casefold() == district_name.casefold()
        ][["psu_number", "hh_number"]].drop_duplicates()
        event_area_rows.append(
            {
                "dataset": "NLSS IV 2022-2023",
                "district": district_name,
                "households": len(selected),
                "unique_psu": selected["psu_number"].nunique(dropna=True),
                "interpretation": "recent cross-section; use small cells cautiously",
            }
        )
    pd.DataFrame(event_area_rows).to_csv(tables / "survey_event_area_coverage.csv", index=False)
    coord = location.loc[valid_coords, ["longitude", "latitude"]].dropna()
    if not coord.empty:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(coord["longitude"], coord["latitude"], s=5, alpha=0.25, color="#C00000")
        ax.set_title("NCCS 2022 geocoded survey observations")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        fig.tight_layout()
        coord_path = figures / "NCCS_2022__coordinate_coverage.png"
        fig.savefig(coord_path, dpi=180)
        plt.close(fig)
        plot_rows.append(
            {
                "dataset": "NCCS 2022",
                "module": "location",
                "variable": "coordinates",
                "variable_label": "Geocoded survey coverage",
                "plot_file": rel(output, coord_path),
            }
        )
        pd.DataFrame(plot_rows).to_csv(tables / "survey_distribution_plot_inventory.csv", index=False)

    metadata_summary = pd.read_csv(tables / "survey_family_summary.csv")
    variable_catalog = pd.read_csv(tables / "survey_variable_catalog.csv", low_memory=False)
    time_candidates = pd.read_csv(tables / "survey_time_candidates.csv", low_memory=False)
    metrics = {
        "stata_read": int(metadata_summary["files"].sum()),
        "variables_catalogued": int(len(variable_catalog)),
        "focused_variables": int(len(summary_df)),
        "plots": int(len(plot_rows)),
        "time_candidates": int(len(time_candidates)),
    }
    update_anasop(root, metrics)

    report = [
        "# Focused Disaster-Survey Briefing",
        "",
        "This focused screening reads selected variables from recent climate, vulnerability-panel, and living-standards modules.",
        "Selections are exploratory candidates only and do not constitute final variable choices.",
        "",
        "## Outputs",
        "",
        f"- Focused modules read: {len(modules_df)}",
        f"- Candidate variables summarized: {len(summary_df)}",
        f"- Distribution and coverage plots generated: {len(plot_rows)}",
        f"- Module read failures: {len(skipped)}",
        "",
        "## Spatial Linkage Finding",
        "",
        "The public NCCS 2022 files retain location field names, but district, ward, latitude, and longitude values are masked as zero. Direct linkage to satellite-derived exposure is therefore not currently feasible without a restricted PSU-coordinate file or verified crosswalk.",
        "The vulnerability panel supports district- and PSU-level longitudinal shock analysis and samples Nuwakot but not Rasuwa. The latest living-standards survey covers both districts, although its Rasuwa sample is only 12 households in one PSU.",
        "",
        "## Temporal Structure",
        "",
        "Repeated waves and event-recall fields were detected, but no time-series plots were produced because user confirmation is required.",
    ]
    (output / "survey_detail_README.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return {**metrics, "focused_modules": len(modules_df), "skipped_modules": len(skipped)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    result = run(Path(args.root).expanduser().resolve())
    print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
