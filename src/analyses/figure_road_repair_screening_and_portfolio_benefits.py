"""Generate the road-repair screening and portfolio-benefits figure.

Plan: Map the selected road sections, separate population reconnection from
finite-delay improvement, and show the primary portfolio benefit plateau and
structural-scenario retention.

Framework: AnaSOP Section 6.7 single-section graph restoration, lexicographic
benefit screening, count-constrained forward selection with joint rerouting,
and workflow step 10. Results are modeled screening evidence, not an
engineering repair order, cost-effectiveness estimate, or global optimum.
"""

from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import PercentFormatter
from pyproj import Transformer
from rasterio.coords import BoundingBox


ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "data" / "processed" / "geospatial"
DECISION = ROOT / "data" / "processed" / "decision"
OUTPUT = (
    ROOT
    / "data"
    / "results"
    / "figures"
    / "Figure_road_repair_screening_and_portfolio_benefits.png"
)

CANDIDATE_PATH = DECISION / "road_repair_candidate_benefits_preprocessed.parquet"
CANDIDATE_GPKG = DECISION / "road_repair_candidate_benefits.gpkg"
SETTLEMENT_BENEFIT_PATH = DECISION / "settlement_road_repair_benefits_preprocessed.parquet"
PORTFOLIO_PATH = DECISION / "road_repair_portfolio_summary_preprocessed.parquet"
SETTLEMENT_PRIORITY_PATH = DECISION / "settlement_intervention_priority_preprocessed.parquet"
ADMIN_PATH = GEO / "base" / "event_area_admin.gpkg"
OSM_PATH = GEO / "base" / "osm_pre_event_aoi.gpkg"

CRS = "EPSG:32645"
RECONNECTION_ID = "OSM-379104232"
FINITE_IMPROVEMENT_ID = "OSM-533216634"
SECTION_COLORS = {
    RECONNECTION_ID: "#2166ac",
    FINITE_IMPROVEMENT_ID: "#f28e2b",
}
SECTION_LABELS = {
    RECONNECTION_ID: "A",
    FINITE_IMPROVEMENT_ID: "B",
}


def add_panel_heading(ax: plt.Axes, label: str, subtitle: str) -> None:
    ax.text(
        0.014,
        0.986,
        f"{label}: {subtitle}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        fontweight="bold",
        color="#20252b",
        bbox={
            "facecolor": "white",
            "edgecolor": "#d2d7dc",
            "linewidth": 0.5,
            "alpha": 0.94,
            "pad": 3.0,
        },
        zorder=50,
    )


def style_frame(ax: plt.Axes) -> None:
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_linewidth(1.25)
        spine.set_edgecolor("#535d66")


def add_graticule(ax: plt.Axes, bounds: BoundingBox) -> None:
    to_lonlat = Transformer.from_crs(CRS, "EPSG:4326", always_xy=True)
    to_utm = Transformer.from_crs("EPSG:4326", CRS, always_xy=True)
    lon_min, lat_min = to_lonlat.transform(bounds.left, bounds.bottom)
    lon_max, lat_max = to_lonlat.transform(bounds.right, bounds.top)

    lon_ticks = np.arange(np.floor(lon_min * 10) / 10, np.ceil(lon_max * 10) / 10 + 0.01, 0.1)
    lat_ticks = np.arange(np.floor(lat_min * 10) / 10, np.ceil(lat_max * 10) / 10 + 0.01, 0.1)
    lat_path = np.linspace(lat_min - 0.05, lat_max + 0.05, 120)
    lon_path = np.linspace(lon_min - 0.05, lon_max + 0.05, 120)

    for lon in lon_ticks:
        x, y = to_utm.transform(np.full_like(lat_path, lon), lat_path)
        ax.plot(x, y, color="#7d8894", linewidth=0.35, alpha=0.28, zorder=12)
        x_label, _ = to_utm.transform(lon, lat_min)
        if bounds.left <= x_label <= bounds.right:
            ax.text(
                x_label,
                bounds.bottom - 0.018 * (bounds.top - bounds.bottom),
                f"{lon:.1f}°E",
                fontsize=7,
                color="#56616c",
                ha="center",
                va="top",
                clip_on=False,
                zorder=30,
            )

    for lat in lat_ticks:
        x, y = to_utm.transform(lon_path, np.full_like(lon_path, lat))
        ax.plot(x, y, color="#7d8894", linewidth=0.35, alpha=0.28, zorder=12)
        _, y_label = to_utm.transform(lon_min, lat)
        if bounds.bottom <= y_label <= bounds.top:
            ax.text(
                bounds.left - 0.015 * (bounds.right - bounds.left),
                y_label,
                f"{lat:.1f}°N",
                fontsize=7,
                color="#56616c",
                ha="right",
                va="center",
                clip_on=False,
                zorder=30,
            )


def add_north_arrow(ax: plt.Axes) -> None:
    ax.annotate(
        "N",
        xy=(0.065, 0.91),
        xytext=(0.065, 0.79),
        xycoords="axes fraction",
        textcoords="axes fraction",
        ha="center",
        va="center",
        fontsize=8,
        fontweight="bold",
        color="#26323c",
        arrowprops={"arrowstyle": "-|>", "color": "#26323c", "lw": 1.15},
        zorder=60,
    )


def add_scale_bar(ax: plt.Axes, bounds: BoundingBox) -> None:
    length_m = 10_000
    x0 = bounds.left + 0.36 * (bounds.right - bounds.left)
    y0 = bounds.bottom + 0.055 * (bounds.top - bounds.bottom)
    ax.plot([x0, x0 + length_m], [y0, y0], color="#20272e", linewidth=2.0, zorder=60)
    ax.plot([x0, x0], [y0 - 600, y0 + 600], color="#20272e", linewidth=1.0, zorder=60)
    ax.plot(
        [x0 + length_m, x0 + length_m],
        [y0 - 600, y0 + 600],
        color="#20272e",
        linewidth=1.0,
        zorder=60,
    )
    ax.text(
        x0 + length_m / 2,
        y0 + 1150,
        "10 km",
        ha="center",
        va="bottom",
        fontsize=7,
        color="#20272e",
        zorder=60,
    )


def prepare_map_bounds(candidates: gpd.GeoDataFrame) -> BoundingBox:
    min_x, min_y, max_x, max_y = candidates.total_bounds
    return BoundingBox(
        left=min_x - 8_000,
        bottom=min_y - 7_000,
        right=max_x + 8_000,
        top=max_y + 7_000,
    )


def plot_map(
    ax: plt.Axes,
    candidates: gpd.GeoDataFrame,
    settlements: gpd.GeoDataFrame,
    districts: gpd.GeoDataFrame,
    local_units: gpd.GeoDataFrame,
    local_roads: gpd.GeoDataFrame,
    major_roads: gpd.GeoDataFrame,
    bounds: BoundingBox,
) -> None:
    if not local_roads.empty:
        local_roads.plot(ax=ax, color="#d8dde1", linewidth=0.22, alpha=0.68, zorder=3)
    if not major_roads.empty:
        major_roads.plot(ax=ax, color="#9fa8af", linewidth=0.52, alpha=0.82, zorder=4)

    candidates.loc[~candidates["Is Critical Road Section"]].plot(
        ax=ax,
        color="#b57a7e",
        linewidth=0.72,
        alpha=0.72,
        zorder=7,
    )
    selected = candidates.loc[candidates["Is Critical Road Section"]].copy()
    for candidate_id in [RECONNECTION_ID, FINITE_IMPROVEMENT_ID]:
        section = selected.loc[selected["Road Repair Candidate ID"].eq(candidate_id)]
        if len(section) != 1:
            raise RuntimeError(f"Expected one selected repair section for {candidate_id}")
        section.plot(
            ax=ax,
            color=SECTION_COLORS[candidate_id],
            linewidth=2.7,
            alpha=1.0,
            zorder=11,
        )
        point = section.geometry.iloc[0].centroid
        label = ax.text(
            point.x,
            point.y,
            SECTION_LABELS[candidate_id],
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color="white",
            zorder=20,
        )
        label.set_path_effects([path_effects.withStroke(linewidth=3.2, foreground="#26323c")])

    reconnected = settlements.loc[settlements["Restored Access after Repair"]]
    improved = settlements.loc[
        settlements["Finite Travel-Time Improvement after Repair (minutes)"].fillna(0).gt(0)
    ]
    if not improved.empty:
        improved.plot(
            ax=ax,
            marker="o",
            color=SECTION_COLORS[FINITE_IMPROVEMENT_ID],
            edgecolor="white",
            linewidth=0.35,
            markersize=22,
            alpha=0.92,
            zorder=13,
        )
    if not reconnected.empty:
        reconnected.plot(
            ax=ax,
            marker="*",
            color=SECTION_COLORS[RECONNECTION_ID],
            edgecolor="white",
            linewidth=0.45,
            markersize=80,
            zorder=14,
        )

    local_units.boundary.plot(ax=ax, color="#a7afb6", linewidth=0.28, alpha=0.62, zorder=15)
    districts.boundary.plot(ax=ax, color="#46515a", linewidth=0.85, alpha=0.92, zorder=16)
    add_graticule(ax, bounds)
    ax.set_xlim(bounds.left, bounds.right)
    ax.set_ylim(bounds.bottom, bounds.top)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    style_frame(ax)
    add_panel_heading(ax, "a", "Screened road sections and modeled beneficiaries")
    add_north_arrow(ax)
    add_scale_bar(ax, bounds)

    ax.legend(
        handles=[
            Line2D([0], [0], color="#b57a7e", lw=1.2, label="Other screened candidates"),
            Line2D([0], [0], color=SECTION_COLORS[RECONNECTION_ID], lw=2.8, label="A · Pasang Lhamu Highway"),
            Line2D([0], [0], color=SECTION_COLORS[FINITE_IMPROVEMENT_ID], lw=2.8, label="B · Unnamed unclassified road"),
            Line2D([0], [0], marker="*", color="none", markerfacecolor=SECTION_COLORS[RECONNECTION_ID], markeredgecolor="white", markersize=9, label="Reconnected settlement"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor=SECTION_COLORS[FINITE_IMPROVEMENT_ID], markeredgecolor="white", markersize=6, label="Finite-delay improvement"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        labelspacing=0.45,
        handlelength=2.0,
    )


def style_benefit_axis(ax: plt.Axes) -> None:
    ax.grid(axis="x", color="#d7dde1", linewidth=0.55, alpha=0.78, zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#6c757d")
    ax.spines["bottom"].set_color("#6c757d")
    ax.tick_params(axis="both", labelsize=7.5)


def plot_single_section_benefits(ax: plt.Axes, critical: pd.DataFrame) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    style_frame(ax)
    add_panel_heading(ax, "b", "Single-section marginal benefits")

    ordered = critical.set_index("Road Repair Candidate ID").reindex(
        [RECONNECTION_ID, FINITE_IMPROVEMENT_ID]
    )
    if ordered["Critical Road Section"].isna().any():
        raise RuntimeError("Critical repair-section table is incomplete")
    y = np.arange(2)

    left = ax.inset_axes([0.08, 0.17, 0.39, 0.62])
    right = ax.inset_axes([0.56, 0.17, 0.39, 0.62])

    population = ordered["Population Reconnected"].to_numpy(dtype=float)
    left.barh(y, population, color="#2b8cbe", edgecolor="#34434d", linewidth=0.55, zorder=3)
    left.set_xlim(0, 3_000)
    left.set_xticks([0, 1_000, 2_000, 3_000], labels=["0", "1k", "2k", "3k"])
    left.set_yticks(
        y,
        labels=[
            f"A · {ordered.iloc[0]['Repair Section Length (m)'] / 1000:.2f} km",
            f"B · {ordered.iloc[1]['Repair Section Length (m)'] / 1000:.2f} km",
        ],
    )
    left.invert_yaxis()
    left.set_xlabel("Population reconnected (persons)", fontsize=8)
    left.text(0.5, 1.06, "Reconnection", transform=left.transAxes, ha="center", va="bottom", fontsize=8, fontweight="bold")
    for idx, value in enumerate(population):
        if value > 0:
            left.text(value - 65, idx, f"{value:,.0f}", ha="right", va="center", fontsize=8, color="white", fontweight="bold", zorder=5)
        else:
            left.text(35, idx, "0", ha="left", va="center", fontsize=8, color="#4e5962", zorder=5)
    style_benefit_axis(left)

    finite = (
        ordered["Population-Weighted Finite Travel-Time Improvement (person-minutes)"]
        .to_numpy(dtype=float)
        / 1_000
    )
    right.barh(y, finite, color="#f28e2b", edgecolor="#34434d", linewidth=0.55, zorder=3)
    right.set_xlim(0, 130)
    right.set_yticks(y, labels=[])
    right.invert_yaxis()
    right.set_xlabel("Finite improvement (thousand person-minutes)", fontsize=8)
    right.text(0.5, 1.06, "Finite-delay reduction", transform=right.transAxes, ha="center", va="bottom", fontsize=8, fontweight="bold")
    for idx, value in enumerate(finite):
        if value > 0:
            right.text(value - 2.5, idx, f"{value:,.1f}", ha="right", va="center", fontsize=8, color="white", fontweight="bold", zorder=5)
        else:
            right.text(1.8, idx, "0", ha="left", va="center", fontsize=8, color="#4e5962", zorder=5)
    style_benefit_axis(right)


def add_cumulative_labels(
    ax: plt.Axes,
    values: np.ndarray,
    increments: np.ndarray,
    maximum: float,
    decimals: int,
) -> None:
    for idx, (value, increment) in enumerate(zip(values, increments, strict=True)):
        if value > maximum * 0.35:
            x = value - maximum * 0.025
            color = "white"
            ha = "right"
        else:
            x = value + maximum * 0.025
            color = "#364049"
            ha = "left"
        value_text = f"{value:,.{decimals}f}"
        increment_text = f"+{increment:,.{decimals}f}" if increment > 0 else "+0"
        ax.text(
            x,
            idx,
            f"{value_text} ({increment_text})",
            ha=ha,
            va="center",
            fontsize=7,
            color=color,
            fontweight="bold" if increment > 0 else "normal",
            zorder=5,
        )


def plot_portfolio_benefits(ax: plt.Axes, portfolio: pd.DataFrame) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    style_frame(ax)
    add_panel_heading(ax, "c", "Count-constrained joint-rerouting portfolios")

    ordered = portfolio.sort_values("Repair Portfolio Size (sections)").copy()
    expected_sizes = [1, 2, 3, 5]
    if ordered["Repair Portfolio Size (sections)"].tolist() != expected_sizes:
        raise RuntimeError("Portfolio sizes must be K = 1, 2, 3, and 5")

    population = ordered["Primary Portfolio Population Reconnected"].to_numpy(dtype=float)
    finite = (
        ordered["Primary Portfolio-Weighted Finite Travel-Time Improvement (person-minutes)"]
        .to_numpy(dtype=float)
        / 1_000
    )
    retention = ordered["Portfolio Structural-Scenario Retention"].to_numpy(dtype=float) * 100
    population_increment = np.diff(np.r_[0, population])
    finite_increment = np.diff(np.r_[0, finite])
    y = np.arange(len(ordered))

    pop_ax = ax.inset_axes([0.055, 0.17, 0.285, 0.64])
    finite_ax = ax.inset_axes([0.385, 0.17, 0.285, 0.64])
    retention_ax = ax.inset_axes([0.715, 0.17, 0.245, 0.64])

    pop_ax.barh(y, population, color="#2b8cbe", edgecolor="#34434d", linewidth=0.55, zorder=3)
    pop_ax.set_xlim(0, 3_000)
    pop_ax.set_xticks([0, 1_000, 2_000, 3_000], labels=["0", "1k", "2k", "3k"])
    pop_ax.set_yticks(y, labels=[f"K = {value}" for value in expected_sizes])
    pop_ax.invert_yaxis()
    pop_ax.set_xlabel("Persons", fontsize=8)
    pop_ax.text(0.5, 1.06, "Population reconnected", transform=pop_ax.transAxes, ha="center", va="bottom", fontsize=8, fontweight="bold")
    add_cumulative_labels(pop_ax, population, population_increment, 3_000, 0)
    style_benefit_axis(pop_ax)

    finite_ax.barh(y, finite, color="#f28e2b", edgecolor="#34434d", linewidth=0.55, zorder=3)
    finite_ax.set_xlim(0, 130)
    finite_ax.set_yticks(y, labels=[])
    finite_ax.invert_yaxis()
    finite_ax.set_xlabel("Thousand person-minutes", fontsize=8)
    finite_ax.text(0.5, 1.06, "Finite improvement", transform=finite_ax.transAxes, ha="center", va="bottom", fontsize=8, fontweight="bold")
    add_cumulative_labels(finite_ax, finite, finite_increment, 130, 1)
    style_benefit_axis(finite_ax)

    retention_ax.barh(y, retention, color="#756bb1", edgecolor="#34434d", linewidth=0.55, zorder=3)
    retention_ax.set_xlim(0, 100)
    retention_ax.set_yticks(y, labels=[])
    retention_ax.invert_yaxis()
    retention_ax.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    retention_ax.set_xlabel("Structural scenarios", fontsize=8)
    retention_ax.text(0.5, 1.06, "Positive-benefit retention", transform=retention_ax.transAxes, ha="center", va="bottom", fontsize=8, fontweight="bold")
    for idx, value in enumerate(retention):
        retention_ax.text(value - 2, idx, f"{value:.0f}%", ha="right", va="center", fontsize=7.2, color="white", fontweight="bold", zorder=5)
    style_benefit_axis(retention_ax)

    for small_ax in [pop_ax, finite_ax, retention_ax]:
        for row in [2, 3]:
            small_ax.axhspan(row - 0.48, row + 0.48, facecolor="#e6e9ec", alpha=0.20, hatch="//", edgecolor="#aeb5bb", linewidth=0, zorder=4)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    candidate_table = pd.read_parquet(CANDIDATE_PATH)
    candidates = gpd.read_file(CANDIDATE_GPKG, layer="road_repair_candidates").to_crs(CRS)
    if len(candidate_table) != 194 or len(candidates) != 194:
        raise RuntimeError("The complete primary repair surface must contain 194 candidates")
    if int(candidate_table["Is Critical Road Section"].sum()) != 2:
        raise RuntimeError("Exactly two road sections must have positive primary marginal benefit")

    benefit = pd.read_parquet(SETTLEMENT_BENEFIT_PATH)
    benefit = benefit.loc[
        benefit["Road Repair Candidate ID"].isin([RECONNECTION_ID, FINITE_IMPROVEMENT_ID])
    ].copy()
    priority = pd.read_parquet(SETTLEMENT_PRIORITY_PATH)
    priority["OSM Settlement ID"] = priority["OSM Settlement ID"].astype(str)
    benefit["OSM Settlement ID"] = benefit["OSM Settlement ID"].astype(str)
    benefit = benefit.merge(
        priority[
            [
                "OSM Settlement ID",
                "Settlement Longitude",
                "Settlement Latitude",
            ]
        ],
        on="OSM Settlement ID",
        how="left",
        validate="many_to_one",
    )
    if benefit[["Settlement Longitude", "Settlement Latitude"]].isna().any().any():
        raise RuntimeError("Beneficiary settlement coordinates are incomplete")
    benefit_gdf = gpd.GeoDataFrame(
        benefit,
        geometry=gpd.points_from_xy(
            benefit["Settlement Longitude"], benefit["Settlement Latitude"]
        ),
        crs="EPSG:4326",
    ).to_crs(CRS)

    portfolio = pd.read_parquet(PORTFOLIO_PATH)
    if not np.allclose(
        portfolio["Portfolio Structural-Scenario Retention"].to_numpy(dtype=float),
        2 / 3,
    ):
        raise RuntimeError("Expected two-thirds structural-scenario retention")

    bounds = prepare_map_bounds(candidates)
    districts = gpd.read_file(ADMIN_PATH, layer="districts").to_crs(CRS)
    local_units = gpd.read_file(ADMIN_PATH, layer="local_units").to_crs(CRS)
    roads = gpd.read_file(OSM_PATH, layer="roads").to_crs(CRS)
    roads = roads.cx[bounds.left : bounds.right, bounds.bottom : bounds.top]
    major_classes = {"motorway", "trunk", "primary", "secondary", "tertiary"}
    local_classes = {"unclassified", "residential", "service", "living_street", "track"}
    major_roads = roads.loc[roads["highway"].isin(major_classes)]
    local_roads = roads.loc[roads["highway"].isin(local_classes)]

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "legend.frameon": True,
            "legend.framealpha": 0.94,
            "hatch.linewidth": 0.65,
        }
    )
    fig = plt.figure(figsize=(15.8, 9.2), constrained_layout=True)
    grid = fig.add_gridspec(2, 2, width_ratios=[0.98, 1.38], height_ratios=[0.86, 1.14])
    ax_a = fig.add_subplot(grid[:, 0])
    ax_b = fig.add_subplot(grid[0, 1])
    ax_c = fig.add_subplot(grid[1, 1])

    plot_map(
        ax_a,
        candidates,
        benefit_gdf,
        districts,
        local_units,
        local_roads,
        major_roads,
        bounds,
    )
    plot_single_section_benefits(
        ax_b,
        candidate_table.loc[candidate_table["Is Critical Road Section"]].copy(),
    )
    plot_portfolio_benefits(ax_c, portfolio)

    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight", pad_inches=0.14, facecolor="white")
    plt.close(fig)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
