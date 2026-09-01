"""Generate the settlement exposure, isolation, and intervention-priority figure.

Plan: Integrate hazard evidence, modeled population, primary-scenario access
disruption, the three-component primary priority score, and the district-level
vulnerability sensitivity score. Population and accessibility are modeled;
district vulnerability is contextual sensitivity information and is not a
settlement-level observation.

Framework: AnaSOP Sections 5, 6.2--6.4, and workflow steps 7--8.
"""

from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
from matplotlib.colors import BoundaryNorm, ListedColormap, Normalize
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from pyproj import Transformer


ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "data" / "processed" / "geospatial"
DECISION = ROOT / "data" / "processed" / "decision"
OUTPUT = (
    ROOT
    / "data"
    / "results"
    / "figures"
    / "Figure_settlement_exposure_isolation_and_intervention_priority.png"
)

PRIORITY_PATH = DECISION / "settlement_intervention_priority_preprocessed.parquet"
HAZARD_CLASS_PATH = GEO / "hazard" / "hazard_evidence_class_20m.tif"
ADMIN_PATH = GEO / "base" / "event_area_admin.gpkg"
OSM_PATH = GEO / "base" / "osm_pre_event_aoi.gpkg"
CRS = "EPSG:32645"


def add_graticule(ax: plt.Axes, bounds: rasterio.coords.BoundingBox) -> None:
    """Draw geographic graticules and place coordinates outside the frame."""
    to_lonlat = Transformer.from_crs(CRS, "EPSG:4326", always_xy=True)
    to_utm = Transformer.from_crs("EPSG:4326", CRS, always_xy=True)
    lon_min, lat_min = to_lonlat.transform(bounds.left, bounds.bottom)
    lon_max, lat_max = to_lonlat.transform(bounds.right, bounds.top)

    lon_ticks = np.arange(np.floor(lon_min * 5) / 5, np.ceil(lon_max * 5) / 5 + 0.01, 0.2)
    lat_ticks = np.arange(np.floor(lat_min * 5) / 5, np.ceil(lat_max * 5) / 5 + 0.01, 0.2)
    lat_path = np.linspace(lat_min - 0.1, lat_max + 0.1, 120)
    lon_path = np.linspace(lon_min - 0.1, lon_max + 0.1, 120)

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
                bounds.left - 0.012 * (bounds.right - bounds.left),
                y_label,
                f"{lat:.1f}°N",
                fontsize=7,
                color="#56616c",
                ha="right",
                va="center",
                clip_on=False,
                zorder=30,
            )


def add_panel_heading(ax: plt.Axes, label: str, subtitle: str) -> None:
    ax.text(
        0.018,
        0.978,
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
            "alpha": 0.93,
            "pad": 3.0,
        },
        zorder=50,
    )


def add_north_arrow(ax: plt.Axes) -> None:
    ax.annotate(
        "N",
        xy=(0.068, 0.91),
        xytext=(0.068, 0.79),
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


def add_scale_bar(
    ax: plt.Axes,
    bounds: rasterio.coords.BoundingBox,
    x_fraction: float = 0.055,
) -> None:
    length_m = 20_000
    x0 = bounds.left + x_fraction * (bounds.right - bounds.left)
    y0 = bounds.bottom + 0.055 * (bounds.top - bounds.bottom)
    ax.plot([x0, x0 + length_m], [y0, y0], color="#20272e", linewidth=2.0, zorder=60)
    ax.plot([x0, x0], [y0 - 900, y0 + 900], color="#20272e", linewidth=1.0, zorder=60)
    ax.plot(
        [x0 + length_m, x0 + length_m],
        [y0 - 900, y0 + 900],
        color="#20272e",
        linewidth=1.0,
        zorder=60,
    )
    ax.text(
        x0 + length_m / 2,
        y0 + 1700,
        "20 km",
        ha="center",
        va="bottom",
        fontsize=7,
        color="#20272e",
        zorder=60,
    )


def plot_road_background(
    ax: plt.Axes,
    local_roads: gpd.GeoDataFrame,
    major_roads: gpd.GeoDataFrame,
) -> None:
    if not local_roads.empty:
        local_roads.plot(ax=ax, color="#d8dde1", linewidth=0.22, alpha=0.68, zorder=3)
    if not major_roads.empty:
        major_roads.plot(ax=ax, color="#9fa8af", linewidth=0.50, alpha=0.80, zorder=4)


def style_map(
    ax: plt.Axes,
    bounds: rasterio.coords.BoundingBox,
    districts: gpd.GeoDataFrame,
    local_units: gpd.GeoDataFrame,
) -> None:
    local_units.boundary.plot(ax=ax, color="#a7afb6", linewidth=0.25, alpha=0.58, zorder=13)
    districts.boundary.plot(ax=ax, color="#46515a", linewidth=0.80, alpha=0.90, zorder=14)
    add_graticule(ax, bounds)
    ax.set_xlim(bounds.left, bounds.right)
    ax.set_ylim(bounds.bottom, bounds.top)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_linewidth(1.25)
        spine.set_edgecolor("#535d66")


def population_sizes(values: pd.Series, maximum: float) -> np.ndarray:
    """Map modeled population to readable marker areas without implying precision."""
    clipped = np.clip(values.fillna(0).to_numpy(dtype=float), 0, maximum)
    return 7.0 + 48.0 * np.sqrt(clipped / maximum)


def add_population_legend(ax: plt.Axes, maximum: float) -> None:
    values = [100, 1_000, 3_000]
    handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor="#75808a",
            markeredgecolor="white",
            markeredgewidth=0.4,
            markersize=np.sqrt(population_sizes(pd.Series([value]), maximum)[0]),
            label=f"{value:,}",
        )
        for value in values
    ]
    legend = ax.legend(
        handles=handles,
        title="Modeled population",
        loc="lower right",
        fontsize=7,
        title_fontsize=7,
        borderpad=0.5,
        labelspacing=0.65,
        handletextpad=0.7,
    )
    ax.add_artist(legend)


def label_top_five(
    ax: plt.Axes,
    frame: gpd.GeoDataFrame,
    rank_column: str,
) -> None:
    """Label the five leading settlements with alternating leader offsets."""
    top = frame.nsmallest(5, rank_column).sort_values(rank_column)
    offsets = [(8, 8), (8, -12), (-8, 8), (-8, -12), (8, 15)]
    for (_, row), offset in zip(top.iterrows(), offsets, strict=True):
        name = str(row["Settlement Name (English Preferred)"])
        label = f"{int(row[rank_column])}  {name}"
        annotation = ax.annotate(
            label,
            xy=(row.geometry.x, row.geometry.y),
            xytext=offset,
            textcoords="offset points",
            ha="left" if offset[0] > 0 else "right",
            va="bottom" if offset[1] > 0 else "top",
            fontsize=7.2,
            fontweight="bold",
            color="#27313a",
            arrowprops={"arrowstyle": "-", "color": "#5f6870", "lw": 0.55},
            zorder=40,
        )
        annotation.set_path_effects(
            [path_effects.withStroke(linewidth=2.6, foreground="white")]
        )


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with rasterio.open(HAZARD_CLASS_PATH) as hazard_ds:
        bounds = hazard_ds.bounds

    districts = gpd.read_file(ADMIN_PATH, layer="districts").to_crs(CRS)
    local_units = gpd.read_file(ADMIN_PATH, layer="local_units").to_crs(CRS)
    roads = gpd.read_file(OSM_PATH, layer="roads").to_crs(CRS)
    roads = roads.cx[bounds.left : bounds.right, bounds.bottom : bounds.top]
    major_classes = {"motorway", "trunk", "primary", "secondary", "tertiary"}
    local_classes = {"unclassified", "residential", "service", "living_street", "track"}
    major_roads = roads.loc[roads["highway"].isin(major_classes)]
    local_roads = roads.loc[roads["highway"].isin(local_classes)]

    priority = pd.read_parquet(PRIORITY_PATH)
    if priority["Scenario ID"].nunique() != 1 or not priority["Primary Scenario"].all():
        raise RuntimeError("Priority table must contain exactly the primary scenario")
    if priority[["Settlement Longitude", "Settlement Latitude"]].isna().any().any():
        raise RuntimeError("Settlement coordinates are incomplete")
    settlements = gpd.GeoDataFrame(
        priority,
        geometry=gpd.points_from_xy(
            priority["Settlement Longitude"], priority["Settlement Latitude"]
        ),
        crs="EPSG:4326",
    ).to_crs(CRS)
    eligible = settlements.loc[settlements["Included in Priority Ranking"].fillna(False)].copy()
    if eligible.empty:
        raise RuntimeError("No settlements are included in the intervention-priority ranking")

    maximum_population = max(3_000.0, float(settlements["Estimated Settlement Population"].max()))
    all_sizes = population_sizes(settlements["Estimated Settlement Population"], maximum_population)
    eligible_sizes = population_sizes(eligible["Estimated Settlement Population"], maximum_population)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "legend.frameon": True,
            "legend.framealpha": 0.94,
        }
    )
    fig, axes = plt.subplots(2, 2, figsize=(13.2, 11.1), constrained_layout=True)
    ax_a, ax_b, ax_c, ax_d = axes.flat

    # a: Hazard evidence class and modeled settlement population.
    plot_road_background(ax_a, local_roads, major_roads)
    evidence_colors = ["#bfc5ca", "#fee08b", "#fdae61", "#d73027"]
    evidence_cmap = ListedColormap(evidence_colors)
    evidence_norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], evidence_cmap.N)
    ax_a.scatter(
        settlements.geometry.x,
        settlements.geometry.y,
        c=settlements["Maximum Evidence Class within 500 m"],
        cmap=evidence_cmap,
        norm=evidence_norm,
        s=all_sizes,
        linewidths=0.32,
        edgecolors="white",
        alpha=0.92,
        zorder=8,
    )
    style_map(ax_a, bounds, districts, local_units)
    add_panel_heading(ax_a, "a", "Hazard evidence and modeled population")
    add_north_arrow(ax_a)
    add_scale_bar(ax_a, bounds, x_fraction=0.36)
    evidence_legend = ax_a.legend(
        handles=[
            Line2D(
                [0],
                [0],
                marker="o",
                color="none",
                markerfacecolor=color,
                markeredgecolor="white",
                markersize=6,
                label=f"Evidence class {level}",
            )
            for level, color in enumerate(evidence_colors)
        ],
        loc="lower left",
        fontsize=7,
        borderpad=0.5,
        labelspacing=0.45,
        handletextpad=0.5,
    )
    ax_a.add_artist(evidence_legend)
    add_population_legend(ax_a, maximum_population)

    # b: Primary-scenario accessibility loss and modeled isolation.
    plot_road_background(ax_b, local_roads, major_roads)
    status = settlements["Accessibility Status"]
    ineligible = settlements.loc[status.eq("baseline ineligible")]
    limited = settlements.loc[status.eq("reachable with limited change")]
    delayed = settlements.loc[status.eq("delay over 5 minutes")]
    isolated = settlements.loc[status.eq("newly isolated")]
    if not ineligible.empty:
        ineligible.plot(
            ax=ax_b,
            marker="o",
            facecolor="white",
            edgecolor="#a1a8ae",
            linewidth=0.45,
            markersize=8,
            alpha=0.85,
            zorder=6,
        )
    if not limited.empty:
        limited.plot(
            ax=ax_b,
            marker="o",
            color="#cbd2d8",
            edgecolor="white",
            linewidth=0.15,
            markersize=8,
            alpha=0.85,
            zorder=7,
        )
    loss_norm = Normalize(vmin=5, vmax=max(10, float(delayed["Accessibility Loss (minutes)"].max())))
    delayed_points = ax_b.scatter(
        delayed.geometry.x,
        delayed.geometry.y,
        c=delayed["Accessibility Loss (minutes)"],
        cmap="YlOrRd",
        norm=loss_norm,
        s=24,
        linewidths=0.30,
        edgecolors="#6b2c25",
        alpha=0.96,
        zorder=9,
    )
    if not isolated.empty:
        isolated.plot(
            ax=ax_b,
            marker="X",
            color="#54278f",
            edgecolor="white",
            linewidth=0.50,
            markersize=42,
            zorder=10,
        )
    style_map(ax_b, bounds, districts, local_units)
    add_panel_heading(ax_b, "b", "Primary-scenario access loss")
    cbar_b = fig.colorbar(delayed_points, ax=ax_b, fraction=0.035, pad=0.018, shrink=0.68)
    cbar_b.set_label("Accessibility loss (minutes)")
    ax_b.legend(
        handles=[
            Line2D([0], [0], marker="o", color="none", markerfacecolor="white", markeredgecolor="#a1a8ae", markersize=5, label="Baseline ineligible"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#cbd2d8", markeredgecolor="white", markersize=5, label="Reachable, ≤ 5 min delay"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#f16913", markeredgecolor="#6b2c25", markersize=6, label="Finite delay > 5 min"),
            Line2D([0], [0], marker="X", color="none", markerfacecolor="#54278f", markeredgecolor="white", markersize=7, label="Newly isolated"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        labelspacing=0.45,
        handletextpad=0.5,
    )

    # c: Equal-weight hazard, exposure, and accessibility ranking.
    plot_road_background(ax_c, local_roads, major_roads)
    priority_norm = Normalize(vmin=0, vmax=1)
    primary_points = ax_c.scatter(
        eligible.geometry.x,
        eligible.geometry.y,
        c=eligible["Intervention Priority"],
        cmap="YlOrRd",
        norm=priority_norm,
        s=eligible_sizes,
        linewidths=0.38,
        edgecolors="#6f251e",
        alpha=0.96,
        zorder=9,
    )
    primary_top = eligible.nsmallest(10, "Priority Rank")
    ax_c.scatter(
        primary_top.geometry.x,
        primary_top.geometry.y,
        facecolors="none",
        edgecolors="#17202a",
        s=population_sizes(primary_top["Estimated Settlement Population"], maximum_population) + 18,
        linewidths=1.05,
        zorder=11,
    )
    style_map(ax_c, bounds, districts, local_units)
    add_panel_heading(ax_c, "c", "Primary three-component priority")
    cax_c = ax_c.inset_axes([0.055, 0.835, 0.32, 0.025])
    cbar_c = fig.colorbar(primary_points, cax=cax_c, orientation="horizontal")
    cbar_c.set_ticks([0, 0.5, 1])
    cbar_c.ax.tick_params(labelsize=6.5, length=2, pad=1)
    cbar_c.set_label("Primary intervention priority", fontsize=7, labelpad=1.5)
    label_top_five(ax_c, eligible, "Priority Rank")
    ax_c.legend(
        handles=[
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#d7301f", markeredgecolor="#6f251e", markersize=6, label="Ranking-eligible settlement"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="none", markeredgecolor="#17202a", markeredgewidth=1.1, markersize=8, label="Primary top 10"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        labelspacing=0.45,
        handletextpad=0.6,
    )

    # d: District vulnerability is a sensitivity component, not settlement data.
    plot_road_background(ax_d, local_roads, major_roads)
    sensitivity_points = ax_d.scatter(
        eligible.geometry.x,
        eligible.geometry.y,
        c=eligible["Sensitivity Intervention Priority"],
        cmap="YlOrRd",
        norm=priority_norm,
        s=eligible_sizes,
        linewidths=0.38,
        edgecolors="#6f251e",
        alpha=0.96,
        zorder=9,
    )
    sensitivity_top = eligible.nsmallest(10, "Sensitivity Priority Rank")
    ax_d.scatter(
        sensitivity_top.geometry.x,
        sensitivity_top.geometry.y,
        facecolors="none",
        edgecolors="#17202a",
        s=population_sizes(sensitivity_top["Estimated Settlement Population"], maximum_population) + 18,
        linewidths=1.05,
        zorder=11,
    )
    style_map(ax_d, bounds, districts, local_units)
    add_panel_heading(ax_d, "d", "District vulnerability sensitivity")
    cax_d = ax_d.inset_axes([0.055, 0.835, 0.32, 0.025])
    cbar_d = fig.colorbar(sensitivity_points, cax=cax_d, orientation="horizontal")
    cbar_d.set_ticks([0, 0.5, 1])
    cbar_d.ax.tick_params(labelsize=6.5, length=2, pad=1)
    cbar_d.set_label("Sensitivity intervention priority", fontsize=7, labelpad=1.5)
    label_top_five(ax_d, eligible, "Sensitivity Priority Rank")
    ax_d.legend(
        handles=[
            Patch(facecolor="#fdae61", edgecolor="#6f251e", label="District-context sensitivity score"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="none", markeredgecolor="#17202a", markeredgewidth=1.1, markersize=8, label="Sensitivity top 10"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        labelspacing=0.45,
        handletextpad=0.6,
    )

    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight", pad_inches=0.14, facecolor="white")
    plt.close(fig)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
