"""Generate Appendix Table A3 and its PNG preview.

Plan: compare the primary accessibility result with seven pre-specified
structural sensitivity scenarios spanning hazard evidence, closure rules,
facility availability, topology repair, and settlement-to-road linkage.

Framework: AnaSOP Sections 5-7 and workflow step 5. Population-weighted
outcomes use the calibrated settlement allocation within 3 km. Road closures
and facility losses are modeled assumptions, not field-confirmed conditions.
"""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import tempfile

import numpy as np
import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[2]
ACCESSIBILITY = (
    ROOT
    / "data"
    / "processed"
    / "geospatial"
    / "accessibility"
    / "settlement_disruption_accessibility_robustness_preprocessed.parquet"
)
POPULATION = (
    ROOT
    / "data"
    / "processed"
    / "geospatial"
    / "population"
    / "settlement_population_allocation_preprocessed.parquet"
)
PRIMARY_SUMMARY = (
    ROOT
    / "data"
    / "processed"
    / "geospatial"
    / "accessibility"
    / "accessibility_scenario_population_summary_preprocessed.parquet"
)
OUTPUT = (
    ROOT
    / "data"
    / "results"
    / "tables"
    / "Table_accessibility_and_isolation_scenarios.xlsx"
)
PREVIEW = (
    ROOT
    / "data"
    / "exp"
    / "table_previews"
    / "Table_accessibility_and_isolation_scenarios.png"
)

TITLE = "Accessibility and Isolation Scenarios"
HEADERS = [
    "Scenario",
    "Hazard evidence\nclass",
    "Topology repair\nthreshold (m)",
    "Settlement snap\ndistance (m)",
    "Closure / facility rule",
    "Newly isolated\npopulation",
    "Population delayed\n>5 min",
    "Population-weighted loss\n(person-minutes)",
]

# One primary result plus seven compact, interpretable sensitivity checks.
SCENARIOS = [
    ("Primary", "H3_destroyed_roads_only_r5_t3000"),
    ("Class 2 footprint", "H2_destroyed_roads_only_r5_t3000"),
    ("Class 1 footprint", "H1_destroyed_roads_only_r5_t3000"),
    ("Broader road closure", "H3_all_candidate_roads_only_r5_t3000"),
    ("Class 1 + facility loss", "H1_destroyed_facility_loss_r5_t3000"),
    ("No topology repair", "H3_destroyed_roads_only_r0_t3000"),
    ("20 m topology repair", "H3_destroyed_roads_only_r20_t3000"),
    ("500 m settlement snap", "H3_destroyed_roads_only_r5_t500"),
]


def summarize_scenarios() -> pd.DataFrame:
    """Aggregate population outcomes from the complete 192-scenario surface."""
    accessibility = pd.read_parquet(ACCESSIBILITY)
    population = pd.read_parquet(POPULATION)[
        ["OSM Settlement ID", "Estimated Settlement Population"]
    ]
    if population["OSM Settlement ID"].duplicated().any():
        raise RuntimeError("Settlement population identifiers are not unique")

    detail = accessibility.merge(
        population,
        on="OSM Settlement ID",
        how="left",
        validate="many_to_one",
    )
    if detail["Estimated Settlement Population"].isna().any():
        raise RuntimeError("Accessibility rows are missing settlement population")
    if detail["Scenario ID"].nunique() != 192:
        raise RuntimeError("Expected the complete 192-scenario accessibility surface")

    pop = detail["Estimated Settlement Population"].astype(float)
    finite_loss = detail["Accessibility Loss (minutes)"].astype(float)
    detail["Newly Isolated Population"] = np.where(
        detail["Newly Isolated"].fillna(False), pop, 0.0
    )
    detail["Population Delayed over 5 Minutes"] = np.where(
        detail["Accessibility Status"].eq("delay over 5 minutes"), pop, 0.0
    )
    detail["Population-Weighted Accessibility Loss (person-minutes)"] = np.where(
        np.isfinite(finite_loss), pop * finite_loss, np.nan
    )

    group_columns = [
        "Scenario ID",
        "Primary Scenario",
        "Minimum Evidence Class",
        "Road Closure Rule",
        "Facility Availability Rule",
        "Topology Repair Threshold (m)",
        "Maximum Settlement Snap Distance (m)",
    ]
    summary = (
        detail.groupby(group_columns, sort=False, dropna=False)
        .agg(
            **{
                "Newly Isolated Population": (
                    "Newly Isolated Population",
                    "sum",
                ),
                "Population Delayed over 5 Minutes": (
                    "Population Delayed over 5 Minutes",
                    "sum",
                ),
                "Population-Weighted Accessibility Loss (person-minutes)": (
                    "Population-Weighted Accessibility Loss (person-minutes)",
                    "sum",
                ),
            }
        )
        .reset_index()
        .set_index("Scenario ID")
    )

    selected_ids = [scenario_id for _, scenario_id in SCENARIOS]
    missing = sorted(set(selected_ids) - set(summary.index))
    if missing:
        raise RuntimeError(f"Planned scenarios are missing: {missing}")
    selected = summary.loc[selected_ids].copy()
    if selected.index.duplicated().any() or len(selected) != 8:
        raise RuntimeError("AnaSOP requires eight unique accessibility scenarios")
    if not bool(selected.iloc[0]["Primary Scenario"]):
        raise RuntimeError("The first row must be the registered primary scenario")
    if int(selected["Primary Scenario"].sum()) != 1:
        raise RuntimeError("The compact table must contain one primary scenario")

    # Reconcile the primary result to the existing population integration output.
    primary_reference = pd.read_parquet(PRIMARY_SUMMARY)
    primary_reference = primary_reference.loc[
        primary_reference["Scenario ID"].eq("H3_destroyed_roads_only")
    ].iloc[0]
    for column in [
        "Newly Isolated Population",
        "Population Delayed over 5 Minutes",
        "Population-Weighted Accessibility Loss (person-minutes)",
    ]:
        if not np.isclose(selected.iloc[0][column], primary_reference[column]):
            raise RuntimeError(f"Primary robustness aggregation disagrees for {column}")
    return selected


def compact_rule(row: pd.Series) -> str:
    closure = (
        "Destroyed"
        if row["Road Closure Rule"] == "Destroyed only"
        else "All candidates"
    )
    facility = (
        "roads"
        if row["Facility Availability Rule"] == "Road disruption only"
        else "roads + exposed facilities"
    )
    return f"{closure} / {facility}"


def build_rows(summary: pd.DataFrame) -> list[list[object]]:
    rows: list[list[object]] = []
    for (label, _), (_, row) in zip(SCENARIOS, summary.iterrows(), strict=True):
        rows.append(
            [
                label,
                int(row["Minimum Evidence Class"]),
                int(row["Topology Repair Threshold (m)"]),
                int(row["Maximum Settlement Snap Distance (m)"]),
                compact_rule(row),
                int(round(float(row["Newly Isolated Population"]))),
                int(round(float(row["Population Delayed over 5 Minutes"]))),
                int(
                    round(
                        float(
                            row[
                                "Population-Weighted Accessibility Loss (person-minutes)"
                            ]
                        )
                    )
                ),
            ]
        )
    if len(rows) != 8 or any(len(row) != 8 for row in rows):
        raise RuntimeError("AnaSOP requires exactly 8 rows and 8 columns")
    return rows


def build_workbook(rows: list[list[object]]) -> None:
    """Create the authoritative XLSX in the approved compact table style."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PREVIEW.parent.mkdir(parents=True, exist_ok=True)

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Accessibility"
    sheet.sheet_view.showGridLines = False
    sheet.freeze_panes = "A3"

    sheet.merge_cells("A1:H1")
    sheet["A1"] = TITLE
    sheet["A1"].font = Font(name="Aptos Display", size=17, bold=True, color="FFFFFF")
    sheet["A1"].fill = PatternFill("solid", fgColor="17324D")
    sheet["A1"].alignment = Alignment(horizontal="left", vertical="center")
    sheet.row_dimensions[1].height = 32

    for column, header in enumerate(HEADERS, start=1):
        cell = sheet.cell(row=2, column=column, value=header)
        cell.font = Font(name="Aptos", size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="3182BD")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    sheet.row_dimensions[2].height = 42

    body_font = Font(name="Aptos", size=9.5, color="25313A")
    inner = Side(style="thin", color="D6DEE5")
    outer = Side(style="medium", color="535D66")
    for row_idx, values in enumerate(rows, start=3):
        for col_idx, value in enumerate(values, start=1):
            cell = sheet.cell(row=row_idx, column=col_idx, value=value)
            cell.font = body_font
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            if row_idx == 3:
                cell.fill = PatternFill("solid", fgColor="E2F0D9")
            elif row_idx % 2 == 0:
                cell.fill = PatternFill("solid", fgColor="F4F7F9")
            cell.border = Border(bottom=inner)
        sheet.cell(row=row_idx, column=1).font = Font(
            name="Aptos", size=9.5, bold=True, color="17324D"
        )
        for col_idx in (2, 3, 4, 6, 7, 8):
            sheet.cell(row=row_idx, column=col_idx).alignment = Alignment(
                horizontal="center", vertical="center", wrap_text=True
            )
        for col_idx in (6, 7, 8):
            sheet.cell(row=row_idx, column=col_idx).number_format = "#,##0"
        sheet.row_dimensions[row_idx].height = 34

    widths = [28, 17, 21, 20, 34, 22, 23, 28]
    for index, width in enumerate(widths, start=1):
        sheet.column_dimensions[get_column_letter(index)].width = width

    table = Table(displayName="AccessibilityScenarios", ref="A2:H10")
    table.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium2",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=False,
        showColumnStripes=False,
    )
    sheet.add_table(table)

    for col_idx in range(1, 9):
        sheet.cell(row=2, column=col_idx).border = Border(top=outer, bottom=outer)
        sheet.cell(row=10, column=col_idx).border = Border(bottom=outer)
    for row_idx in range(2, 11):
        left = sheet.cell(row=row_idx, column=1)
        right = sheet.cell(row=row_idx, column=8)
        left.border = Border(left=outer, top=left.border.top, bottom=left.border.bottom)
        right.border = Border(right=outer, top=right.border.top, bottom=right.border.bottom)

    sheet.auto_filter.ref = "A2:H10"
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    sheet.page_setup.orientation = "landscape"
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A3
    sheet.page_setup.fitToWidth = 1
    sheet.page_setup.fitToHeight = 1
    sheet.print_area = "A1:H10"
    sheet.page_margins.left = 0.2
    sheet.page_margins.right = 0.2
    sheet.page_margins.top = 0.25
    sheet.page_margins.bottom = 0.25
    sheet.page_margins.header = 0
    sheet.page_margins.footer = 0
    workbook.save(OUTPUT)


def render_preview() -> None:
    """Render the workbook print area to a tightly cropped PNG."""
    soffice = shutil.which("soffice") or "/opt/homebrew/bin/soffice"
    pdftoppm = shutil.which("pdftoppm")
    if not Path(soffice).exists() or pdftoppm is None:
        raise RuntimeError("LibreOffice and pdftoppm are required for PNG rendering")

    with tempfile.TemporaryDirectory(prefix="ke03-table-preview-") as temp_name:
        temp_dir = Path(temp_name)
        profile = temp_dir / "lo-profile"
        subprocess.run(
            [
                soffice,
                f"-env:UserInstallation={profile.as_uri()}",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                str(temp_dir),
                str(OUTPUT),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        pdf = temp_dir / f"{OUTPUT.stem}.pdf"
        preview_stem = temp_dir / "preview"
        subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", "180", str(pdf), str(preview_stem)],
            check=True,
            capture_output=True,
            text=True,
        )
        rendered = Image.open(preview_stem.with_suffix(".png")).convert("RGB")
        background = Image.new("RGB", rendered.size, "white")
        content_bounds = ImageChops.difference(rendered, background).getbbox()
        if content_bounds is None:
            raise RuntimeError("Rendered PNG contains no visible table content")
        left, top, right, bottom = content_bounds
        padding = 24
        rendered.crop(
            (
                max(0, left - padding),
                max(0, top - padding),
                min(rendered.width, right + padding),
                min(rendered.height, bottom + padding),
            )
        ).save(PREVIEW, dpi=(180, 180))


def validate_outputs(rows: list[list[object]]) -> None:
    """Validate workbook values, dimensions, error cells, and PNG output."""
    workbook = load_workbook(OUTPUT, data_only=False, read_only=False)
    sheet = workbook["Accessibility"]
    observed_headers = [sheet.cell(row=2, column=col).value for col in range(1, 9)]
    observed_rows = [
        [sheet.cell(row=row, column=col).value for col in range(1, 9)]
        for row in range(3, 11)
    ]
    if observed_headers != HEADERS or observed_rows != rows:
        raise RuntimeError("Workbook values do not match the planned 8-by-8 table")
    for row in sheet.iter_rows(min_row=1, max_row=10, min_col=1, max_col=8):
        for cell in row:
            if isinstance(cell.value, str) and cell.value.startswith("#"):
                raise RuntimeError(f"Spreadsheet error value in {cell.coordinate}: {cell.value}")
            if cell.data_type == "f":
                raise RuntimeError(f"Unexpected formula in {cell.coordinate}")
    if not PREVIEW.exists() or PREVIEW.stat().st_size < 10_000:
        raise RuntimeError("PNG preview is missing or unexpectedly small")


def main() -> None:
    summary = summarize_scenarios()
    rows = build_rows(summary)
    build_workbook(rows)
    render_preview()
    validate_outputs(rows)
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {PREVIEW.relative_to(ROOT)}")
    print("Validated 8 rows x 8 columns; one primary plus seven robustness scenarios")


if __name__ == "__main__":
    main()
