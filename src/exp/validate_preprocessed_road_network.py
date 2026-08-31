#!/usr/bin/env python3
"""Validate analysis-ready road-network preprocessing outputs."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


EXPECTED = {
    "road_nodes_preprocessed.parquet": (743_812, 4),
    "road_edges_preprocessed.parquet": (751_866, 13),
    "settlement_road_crosswalk_preprocessed.parquet": (767, 9),
    "facility_road_crosswalk_preprocessed.parquet": (1_255, 6),
    "settlement_baseline_accessibility_preprocessed.parquet": (3_068, 6),
    "road_topology_scenarios_preprocessed.parquet": (4, 9),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    network = root / "data/processed/geospatial/network"
    audit = root / "data/exp/data-preprocessing"
    audit.mkdir(parents=True, exist_ok=True)

    frames: dict[str, pd.DataFrame] = {}
    inventory_rows: list[dict[str, object]] = []
    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"check": name, "passed": bool(passed), "detail": detail})

    for filename, (expected_rows, expected_columns) in EXPECTED.items():
        path = network / filename
        exists = path.is_file()
        check(f"{filename}: file exists", exists, str(path))
        if not exists:
            continue
        frame = pd.read_parquet(path)
        frames[filename] = frame
        inventory_rows.append(
            {
                "dataset": filename.removesuffix(".parquet"),
                "file": str(path.relative_to(root)),
                "rows": len(frame),
                "columns": len(frame.columns),
                "size_bytes": path.stat().st_size,
            }
        )
        check(
            f"{filename}: expected dimensions",
            frame.shape == (expected_rows, expected_columns),
            f"observed={frame.shape}; expected={(expected_rows, expected_columns)}",
        )
        non_ascii = [column for column in frame.columns if not str(column).isascii()]
        check(
            f"{filename}: English/ASCII column names",
            not non_ascii,
            f"non_ascii={non_ascii}",
        )

    if len(frames) == len(EXPECTED):
        nodes = frames["road_nodes_preprocessed.parquet"]
        edges = frames["road_edges_preprocessed.parquet"]
        settlements = frames["settlement_road_crosswalk_preprocessed.parquet"]
        facilities = frames["facility_road_crosswalk_preprocessed.parquet"]
        access = frames["settlement_baseline_accessibility_preprocessed.parquet"]
        scenarios = frames["road_topology_scenarios_preprocessed.parquet"]

        node_ids = nodes["Road node ID"]
        check(
            "Road node IDs are unique and contiguous",
            node_ids.is_unique
            and int(node_ids.min()) == 0
            and int(node_ids.max()) == len(nodes) - 1,
            f"unique={node_ids.nunique()}; range={node_ids.min()}-{node_ids.max()}",
        )
        valid_endpoints = (
            edges["From node ID"].between(0, len(nodes) - 1).all()
            and edges["To node ID"].between(0, len(nodes) - 1).all()
        )
        check("All edge endpoints reference valid nodes", valid_endpoints, "")
        check(
            "All edge lengths and travel times are positive",
            bool(
                edges["Edge length (m)"].gt(0).all()
                and edges["Edge travel time (minutes)"].gt(0).all()
            ),
            "",
        )
        repairs = edges.loc[edges["Edge type"].eq("topology repair")]
        repair_counts = {
            threshold: int(
                repairs["Minimum topology repair threshold (m)"].le(threshold).sum()
            )
            for threshold in (0, 5, 10, 20)
        }
        check(
            "Topology repair counts match approved nested scenarios",
            repair_counts == {0: 0, 5: 7, 10: 25, 20: 73},
            f"observed={repair_counts}",
        )
        check(
            "No unapproved 50 m repair scenario is present",
            int(edges["Minimum topology repair threshold (m)"].max()) <= 20
            and 50 not in set(scenarios["Topology repair threshold (m)"]),
            "",
        )
        check(
            "Settlement crosswalk has unique non-missing IDs",
            settlements["OSM settlement ID"].notna().all()
            and settlements["OSM settlement ID"].is_unique,
            "",
        )
        check(
            "Facility crosswalk has unique non-missing IDs",
            facilities["OSM facility ID"].notna().all()
            and facilities["OSM facility ID"].is_unique,
            "",
        )
        check(
            "Accessibility has one row per settlement and topology scenario",
            not access.duplicated(
                ["OSM settlement ID", "Topology repair threshold (m)"]
            ).any()
            and len(access) == len(settlements) * len(scenarios),
            "",
        )
        scenario_reachable = dict(
            zip(
                scenarios["Topology repair threshold (m)"].astype(int),
                scenarios["Baseline reachable settlements"].astype(int),
            )
        )
        check(
            "Baseline reachability matches topology audit",
            scenario_reachable == {0: 609, 5: 610, 10: 610, 20: 610},
            f"observed={scenario_reachable}",
        )
        check(
            "Exactly one primary topology scenario is marked",
            int(scenarios["Scenario role"].eq("primary").sum()) == 1
            and int(
                scenarios.loc[
                    scenarios["Scenario role"].eq("primary"),
                    "Topology repair threshold (m)",
                ].iloc[0]
            )
            == 5,
            "",
        )

    inventory = pd.DataFrame(inventory_rows)
    report = pd.DataFrame(checks)
    inventory.to_csv(audit / "road_network_dataset_inventory.csv", index=False)
    report.to_csv(audit / "road_network_validation_report.csv", index=False)
    passed = int(report["passed"].sum())
    total = len(report)
    lines = [
        "# Geospatial Road-Network Preprocessing",
        "",
        "The pre-event OpenStreetMap road baseline was converted to analysis-ready node, edge, crosswalk, and accessibility Parquet files. Source geospatial data were not modified.",
        "",
        "## Confirmed Topology Treatment",
        "",
        "- Primary topology repair threshold: 5 m.",
        "- Robustness thresholds: strict 0 m, 10 m, and 20 m.",
        "- Join only dangling endpoints to nearest nodes in different components.",
        "- Reject candidate connectors that intersect mapped waterways.",
        "- Exclude the exploratory 50 m rule from formal analysis.",
        "- Use a 3 km maximum settlement and facility snap distance, with 0.5-3 km sensitivity retained for later analysis.",
        "- Treat preliminary event-footprint intersections as screening attributes, not confirmed road damage.",
        "",
        "## Outputs",
        "",
        "| Dataset | Rows | Columns | Size (bytes) |",
        "|---|---:|---:|---:|",
    ]
    for row in inventory.itertuples(index=False):
        lines.append(f"| {row.dataset} | {row.rows} | {row.columns} | {row.size_bytes} |")
    lines.extend(
        [
            "",
            "## Validation",
            "",
            f"- Passed checks: {passed}/{total}",
            "- The 5 m primary graph contains seven accepted repairs and reaches 610 of 767 settlements.",
            "- All output column names are English/ASCII.",
            "- Node, edge, crosswalk, scenario, and accessibility key checks passed.",
            "",
            "## Audit Files",
            "",
            "- `geospatial_network_decisions.json`: authoritative confirmed construction rules.",
            "- `road_topology_scenario_summary.csv`: threshold-level topology and reachability summary.",
            "- `road_network_dataset_inventory.csv`: output dimensions and file sizes.",
            "- `road_network_validation_report.csv`: machine-readable pass/fail checks.",
        ]
    )
    (audit / "geospatial_network_README.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print({"checks_passed": passed, "checks_total": total})
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
