"""Generate the road disruption and service-access loss figure.

Plan: Map the primary modeled road closures, baseline service accessibility,
and post-disruption finite delay or complete modeled isolation.
Framework: AnaSOP Sections 5, 6.1, 6.6, and workflow step 4.  Results are
conditional model outputs, not field-confirmed road failure or observed travel.
"""

from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
from matplotlib.colors import Normalize
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from pyproj import Transformer
from rasterio.enums import Resampling


ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "data" / "processed" / "geospatial"
OUTPUT = (
    ROOT
    / "data"
    / "results"
    / "figures"
    / "Figure_road_disruption_and_service_access_loss.png"
)

HAZARD_CLASS_PATH = GEO / "hazard" / "hazard_evidence_class_20m.tif"
ADMIN_PATH = GEO / "base" / "event_area_admin.gpkg"
OSM_PATH = GEO / "base" / "osm_pre_event_aoi.gpkg"
DAMAGE_GEOMETRY_PATH = GEO / "network" / "road_damage_evidence_crosswalk.gpkg"
DAMAGE_TABLE_PATH = GEO / "exposure" / "road_damage_scenario_exposure_preprocessed.parquet"
ACCESS_PATH = GEO / "accessibility" / "settlement_disruption_accessibility_preprocessed.parquet"
POPULATION_PATH = GEO / "population" / "settlement_population_allocation_preprocessed.parquet"
FACILITY_CROSSWALK_PATH = GEO / "network" / "facility_road_crosswalk_preprocessed.parquet"

PRIMARY_SCENARIO_ID = "H3_destroyed_roads_only"
CRS = "EPSG:32645"


def add_graticule(ax: plt.Axes, bounds: rasterio.coords.BoundingBox) -> None:
    """Draw restrained geographic graticules with labels outside the map frame."""
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
        ax.plot(x, y, color="#7d8894", linewidth=0.35, alpha=0.30, zorder=12)
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
        ax.plot(x, y, color="#7d8894", linewidth=0.35, alpha=0.30, zorder=12)
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
            "alpha": 0.92,
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


def add_scale_bar(ax: plt.Axes, bounds: rasterio.coords.BoundingBox) -> None:
    length_m = 20_000
    x0 = bounds.left + 0.055 * (bounds.right - bounds.left)
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


def plot_road_background(
    ax: plt.Axes,
    local_roads: gpd.GeoDataFrame,
    major_roads: gpd.GeoDataFrame,
) -> None:
    if not local_roads.empty:
        local_roads.plot(ax=ax, color="#d5dade", linewidth=0.24, alpha=0.70, zorder=3)
    if not major_roads.empty:
        major_roads.plot(ax=ax, color="#9da6ad", linewidth=0.55, alpha=0.85, zorder=4)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with rasterio.open(HAZARD_CLASS_PATH) as hazard_ds:
        bounds = hazard_ds.bounds
        extent = [bounds.left, bounds.right, bounds.bottom, bounds.top]
        plot_height = 900
        plot_width = round(plot_height * hazard_ds.width / hazard_ds.height)
        hazard_class = hazard_ds.read(
            1,
            out_shape=(plot_height, plot_width),
            resampling=Resampling.nearest,
            masked=True,
        ).filled(0)
    primary_footprint = np.ma.masked_where(hazard_class < 3, np.ones(hazard_class.shape))

    districts = gpd.read_file(ADMIN_PATH, layer="districts").to_crs(CRS)
    local_units = gpd.read_file(ADMIN_PATH, layer="local_units").to_crs(CRS)

    roads = gpd.read_file(OSM_PATH, layer="roads").to_crs(CRS)
    roads = roads.cx[bounds.left : bounds.right, bounds.bottom : bounds.top]
    major_classes = {"motorway", "trunk", "primary", "secondary", "tertiary"}
    local_classes = {"unclassified", "residential", "service", "living_street", "track"}
    major_roads = roads.loc[roads["highway"].isin(major_classes)]
    local_roads = roads.loc[roads["highway"].isin(local_classes)]

    damage = pd.read_parquet(DAMAGE_TABLE_PATH)
    primary_closed_ids = damage.loc[
        damage["CEMS Damage Grade"].eq("Destroyed")
        & damage["Maximum Intersecting Evidence Class"].ge(3),
        "Edge ID",
    ].astype(int)
    damage_geometry = gpd.read_file(
        DAMAGE_GEOMETRY_PATH, layer="road_damage_crosswalk"
    ).to_crs(CRS)
    primary_closed = damage_geometry.loc[
        damage_geometry["Edge ID"].astype(int).isin(primary_closed_ids)
    ]

    access = pd.read_parquet(ACCESS_PATH)
    access = access.loc[access["Scenario ID"].eq(PRIMARY_SCENARIO_ID)].copy()
    population = pd.read_parquet(POPULATION_PATH)
    population = population.loc[population["Allocation Threshold (m)"].eq(3000)].copy()
    access["OSM Settlement ID"] = access["OSM Settlement ID"].astype(str)
    population["OSM Settlement ID"] = population["OSM Settlement ID"].astype(str)
    settlements = access.merge(
        population[
            [
                "OSM Settlement ID",
                "Settlement Longitude",
                "Settlement Latitude",
                "Estimated Settlement Population",
            ]
        ],
        on="OSM Settlement ID",
        how="left",
        validate="one_to_one",
    )
    if settlements[["Settlement Longitude", "Settlement Latitude"]].isna().any().any():
        raise RuntimeError("Settlement coordinates are incomplete after accessibility linkage")
    settlements = gpd.GeoDataFrame(
        settlements,
        geometry=gpd.points_from_xy(
            settlements["Settlement Longitude"], settlements["Settlement Latitude"]
        ),
        crs="EPSG:4326",
    ).to_crs(CRS)

    facility_crosswalk = pd.read_parquet(FACILITY_CROSSWALK_PATH)
    included_facilities = facility_crosswalk.loc[
        facility_crosswalk["Included health/emergency destination"]
    ].copy()
    included_facilities["OSM facility ID"] = included_facilities["OSM facility ID"].astype(str)
    facilities = gpd.read_file(OSM_PATH, layer="facilities")
    facilities["osm_id"] = facilities["osm_id"].astype(str)
    facilities = facilities.merge(
        included_facilities[["OSM facility ID", "Facility category"]],
        left_on="osm_id",
        right_on="OSM facility ID",
        how="inner",
        validate="one_to_one",
    ).to_crs(CRS)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "legend.frameon": True,
            "legend.framealpha": 0.94,
        }
    )
    fig, axes = plt.subplots(1, 3, figsize=(16.2, 6.2), constrained_layout=True)
    ax_a, ax_b, ax_c = axes

    footprint_cmap = plt.get_cmap("Oranges").copy()
    footprint_cmap.set_bad((1, 1, 1, 0))
    ax_a.imshow(
        primary_footprint,
        extent=extent,
        origin="upper",
        cmap=footprint_cmap,
        alpha=0.18,
        interpolation="nearest",
        zorder=1,
    )
    plot_road_background(ax_a, local_roads, major_roads)
    primary_closed.plot(ax=ax_a, color="#b2182b", linewidth=1.35, alpha=0.95, zorder=9)
    style_map(ax_a, bounds, districts, local_units)
    add_panel_heading(ax_a, "a", "Evidence-linked primary road closures")
    add_north_arrow(ax_a)
    add_scale_bar(ax_a, bounds)
    ax_a.legend(
        handles=[
            Patch(facecolor="#fdae6b", alpha=0.28, edgecolor="none", label="Class 3 evidence footprint"),
            Line2D([0], [0], color="#b2182b", lw=1.8, label="Modeled closed graph edges"),
            Line2D([0], [0], color="#9da6ad", lw=1.0, label="Pre-event major roads"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.8,
    )

    plot_road_background(ax_b, local_roads, major_roads)
    baseline_eligible = settlements.loc[settlements["Baseline Eligible"]].copy()
    baseline_ineligible = settlements.loc[~settlements["Baseline Eligible"]].copy()
    baseline_norm = Normalize(vmin=0, vmax=85)
    if not baseline_ineligible.empty:
        baseline_ineligible.plot(
            ax=ax_b,
            marker="o",
            facecolor="white",
            edgecolor="#9ca4ab",
            linewidth=0.45,
            markersize=7,
            alpha=0.80,
            zorder=7,
        )
    baseline_points = ax_b.scatter(
        baseline_eligible.geometry.x,
        baseline_eligible.geometry.y,
        c=baseline_eligible["Baseline Health/Emergency Accessibility (minutes)"],
        cmap="viridis_r",
        norm=baseline_norm,
        s=10,
        linewidths=0.15,
        edgecolors="white",
        alpha=0.92,
        zorder=8,
    )
    health = facilities.loc[facilities["Facility category"].eq("health")]
    emergency = facilities.loc[facilities["Facility category"].eq("emergency")]
    if not health.empty:
        health.plot(ax=ax_b, marker="P", color="#a50f15", edgecolor="white", linewidth=0.35, markersize=25, zorder=10)
    if not emergency.empty:
        emergency.plot(ax=ax_b, marker="^", color="#253746", edgecolor="white", linewidth=0.35, markersize=23, zorder=10)
    style_map(ax_b, bounds, districts, local_units)
    add_panel_heading(ax_b, "b", "Baseline health and emergency accessibility")
    cbar_b = fig.colorbar(baseline_points, ax=ax_b, fraction=0.038, pad=0.018, shrink=0.74)
    cbar_b.set_label("Baseline accessibility (minutes)")
    ax_b.legend(
        handles=[
            Line2D([0], [0], marker="P", color="none", markerfacecolor="#a50f15", markeredgecolor="white", markersize=7, label="Health destination"),
            Line2D([0], [0], marker="^", color="none", markerfacecolor="#253746", markeredgecolor="white", markersize=7, label="Emergency destination"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="white", markeredgecolor="#9ca4ab", markersize=5, label="Baseline ineligible"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.4,
    )

    plot_road_background(ax_c, local_roads, major_roads)
    primary_closed.plot(ax=ax_c, color="#b2182b", linewidth=0.70, alpha=0.62, zorder=6)
    limited = settlements.loc[
        settlements["Accessibility Status"].eq("reachable with limited change")
    ].copy()
    delayed = settlements.loc[
        settlements["Accessibility Status"].eq("delay over 5 minutes")
    ].copy()
    isolated = settlements.loc[settlements["Accessibility Status"].eq("newly isolated")].copy()
    if not limited.empty:
        limited.plot(
            ax=ax_c,
            marker="o",
            color="#c9d0d6",
            edgecolor="white",
            linewidth=0.12,
            markersize=7,
            alpha=0.78,
            zorder=7,
        )
    loss_norm = Normalize(vmin=5, vmax=max(10, float(delayed["Accessibility Loss (minutes)"].max())))
    delayed_points = ax_c.scatter(
        delayed.geometry.x,
        delayed.geometry.y,
        c=delayed["Accessibility Loss (minutes)"],
        cmap="YlOrRd",
        norm=loss_norm,
        s=18,
        linewidths=0.25,
        edgecolors="#5d2420",
        alpha=0.95,
        zorder=9,
    )
    if not isolated.empty:
        isolated.plot(
            ax=ax_c,
            marker="X",
            color="#54278f",
            edgecolor="white",
            linewidth=0.45,
            markersize=38,
            zorder=10,
        )
    style_map(ax_c, bounds, districts, local_units)
    add_panel_heading(ax_c, "c", "Post-disruption access loss and isolation")
    cbar_c = fig.colorbar(delayed_points, ax=ax_c, fraction=0.038, pad=0.018, shrink=0.74)
    cbar_c.set_label("Accessibility loss (minutes)")
    ax_c.legend(
        handles=[
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#c9d0d6", markeredgecolor="white", markersize=5, label="Reachable, ≤ 5 min delay"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#f16913", markeredgecolor="#5d2420", markersize=6, label="Finite delay > 5 min"),
            Line2D([0], [0], marker="X", color="none", markerfacecolor="#54278f", markeredgecolor="white", markersize=7, label="Newly isolated"),
            Line2D([0], [0], color="#b2182b", lw=1.2, alpha=0.70, label="Modeled closed edges"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.5,
    )

    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight", pad_inches=0.14, facecolor="white")
    plt.close(fig)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
