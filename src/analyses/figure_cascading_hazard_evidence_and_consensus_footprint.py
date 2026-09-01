"""Generate the cascading-hazard evidence and consensus footprint figure.

The five panels separate event location, remotely sensed change, source agreement,
terrain and channel context, and the final evidence-confidence classes. The final classes
describe confidence in the assembled evidence, not physical hazard intensity.
"""

from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from matplotlib.colors import BoundaryNorm, ListedColormap, TwoSlopeNorm
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from pyproj import Transformer
from rasterio.enums import Resampling
from rasterio.vrt import WarpedVRT
from shapely.geometry import box


ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "data" / "processed" / "geospatial"
OUTPUT = (
    ROOT
    / "data"
    / "results"
    / "figures"
    / "Figure_cascading_hazard_evidence_and_consensus_footprint.png"
)

STACK_PATH = GEO / "hazard" / "hazard_evidence_stack_20m.tif"
CLASS_PATH = GEO / "hazard" / "hazard_evidence_class_20m.tif"
RADAR_PATH = (
    GEO / "satellite" / "sentinel1_rtc_change_2026-08-16_2026-08-28_vh_db_20m.tif"
)
SLOPE_PATH = GEO / "base" / "copernicus_glo30_slope_degrees_utm45n.tif"
ADMIN_PATH = GEO / "base" / "event_area_admin.gpkg"
NATIONAL_ADMIN0_PATH = (
    ROOT
    / "data"
    / "raw"
    / "geospatial"
    / "base"
    / "admin"
    / "npl_admin_boundaries_2024"
    / "npl_admin0.shp"
)
NATIONAL_ADMIN1_PATH = NATIONAL_ADMIN0_PATH.with_name("npl_admin1.shp")
WORLD_ADMIN0_PATH = (
    ROOT
    / "data"
    / "exp"
    / "figure-table-generation"
    / "context"
    / "natural_earth_10m_admin0"
    / "ne_10m_admin_0_countries.shp"
)
HYDRO_PATH = GEO / "context" / "hydrocryosphere_context.gpkg"
UNOSAT_PATH = GEO / "reference" / "unosat_event_reference.gpkg"
CEMS_PATH = GEO / "reference" / "copernicus_emsr927_damage_reference.gpkg"
MECHANISM_PATH = GEO / "reference" / "event_mechanism_reference.gpkg"

PLOT_HEIGHT = 950


def read_downsampled(
    dataset: rasterio.io.DatasetReader,
    band: int,
    height: int,
    width: int,
    resampling: Resampling,
) -> np.ndarray:
    return dataset.read(
        band,
        out_shape=(height, width),
        resampling=resampling,
        masked=True,
    )


def add_graticule(ax: plt.Axes, bounds: rasterio.coords.BoundingBox) -> None:
    """Add restrained longitude/latitude graticules to a UTM map."""
    to_lonlat = Transformer.from_crs("EPSG:32645", "EPSG:4326", always_xy=True)
    to_utm = Transformer.from_crs("EPSG:4326", "EPSG:32645", always_xy=True)
    lon_min, lat_min = to_lonlat.transform(bounds.left, bounds.bottom)
    lon_max, lat_max = to_lonlat.transform(bounds.right, bounds.top)

    lon_ticks = np.arange(np.floor(lon_min * 5) / 5, np.ceil(lon_max * 5) / 5 + 0.01, 0.2)
    lat_ticks = np.arange(np.floor(lat_min * 5) / 5, np.ceil(lat_max * 5) / 5 + 0.01, 0.2)
    lat_path = np.linspace(lat_min - 0.1, lat_max + 0.1, 120)
    lon_path = np.linspace(lon_min - 0.1, lon_max + 0.1, 120)

    for lon in lon_ticks:
        x, y = to_utm.transform(np.full_like(lat_path, lon), lat_path)
        ax.plot(x, y, color="#7d8894", linewidth=0.35, alpha=0.34, zorder=8)
        x_label, _ = to_utm.transform(lon, lat_min)
        if bounds.left <= x_label <= bounds.right:
            ax.text(
                x_label,
                bounds.bottom - 0.018 * (bounds.top - bounds.bottom),
                f"{lon:.1f}°E",
                fontsize=6.5,
                color="#56616c",
                ha="center",
                va="top",
                clip_on=False,
                zorder=20,
            )
    for lat in lat_ticks:
        x, y = to_utm.transform(lon_path, np.full_like(lon_path, lat))
        ax.plot(x, y, color="#7d8894", linewidth=0.35, alpha=0.34, zorder=8)
        _, y_label = to_utm.transform(lon_min, lat)
        if bounds.bottom <= y_label <= bounds.top:
            ax.text(
                bounds.left - 0.012 * (bounds.right - bounds.left),
                y_label,
                f"{lat:.1f}°N",
                fontsize=6.5,
                color="#56616c",
                ha="right",
                va="center",
                clip_on=False,
                zorder=20,
            )


def add_panel_heading(ax: plt.Axes, label: str, subtitle: str) -> None:
    ax.text(
        0.018,
        0.978,
        f"{label}: {subtitle}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=9.2,
        fontweight="bold",
        color="#20252b",
        bbox={
            "facecolor": "white",
            "edgecolor": "#d2d7dc",
            "linewidth": 0.5,
            "alpha": 0.90,
            "pad": 3.0,
        },
        zorder=50,
    )


def add_north_arrow(ax: plt.Axes) -> None:
    ax.annotate(
        "N",
        xy=(0.075, 0.92),
        xytext=(0.075, 0.80),
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


def add_location_panel(
    ax: plt.Axes,
    world: gpd.GeoDataFrame,
    country: gpd.GeoDataFrame,
    provinces: gpd.GeoDataFrame,
    event_source: gpd.GeoDataFrame,
    analysis_extent: gpd.GeoDataFrame,
) -> None:
    """Draw a standalone regional locator with countries and Nepal provinces."""
    world_name = "ADMIN" if "ADMIN" in world.columns else "name"
    regional_names = ["India", "China", "Bhutan", "Bangladesh", "Nepal"]
    regional = world.loc[world[world_name].isin(regional_names)].copy()
    country_colors = {
        "India": "#edf1f4",
        "China": "#e7ecef",
        "Bhutan": "#f1f3f4",
        "Bangladesh": "#f1f3f4",
        "Nepal": "#faf7f2",
    }
    regional["fill"] = regional[world_name].map(country_colors)
    regional.plot(
        ax=ax,
        color=regional["fill"],
        edgecolor="#59636c",
        linewidth=0.85,
        zorder=1,
    )
    country.plot(ax=ax, facecolor="#fbfaf7", edgecolor="#303a43", linewidth=1.3, zorder=3)
    provinces.boundary.plot(ax=ax, color="#89929a", linewidth=0.48, zorder=4)
    provinces.loc[provinces["adm1_name"] == "Bagmati"].plot(
        ax=ax,
        facecolor="#efb083",
        edgecolor="#a64c2a",
        linewidth=0.9,
        zorder=5,
    )
    analysis_extent.boundary.plot(
        ax=ax,
        color="#b30000",
        linewidth=1.25,
        linestyle="--",
        zorder=7,
    )
    event_source.plot(
        ax=ax,
        marker="*",
        color="#111111",
        edgecolor="white",
        linewidth=0.6,
        markersize=72,
        zorder=8,
    )

    country_labels = {
        "INDIA": (82.7, 26.02),
        "CHINA": (84.35, 30.72),
    }
    for label, (x, y) in country_labels.items():
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            fontsize=21.0,
            fontweight="bold",
            color="#65707a",
            zorder=9,
        )

    for _, row in provinces.iterrows():
        province_name = str(row["adm1_name"])
        province_y = float(row["center_lat"])
        if province_name == "Bagmati":
            province_y -= 0.14
        ax.text(
            float(row["center_lon"]),
            province_y,
            province_name,
            ha="center",
            va="center",
            fontsize=16.0,
            fontweight="bold" if province_name == "Bagmati" else "normal",
            color="#81391f" if province_name == "Bagmati" else "#535e67",
            zorder=9,
        )

    event_x = float(event_source.geometry.x.iloc[0])
    event_y = float(event_source.geometry.y.iloc[0])
    ax.annotate(
        "Event area",
        xy=(event_x, event_y),
        xytext=(86.6, 29.55),
        ha="left",
        va="center",
        fontsize=15.0,
        color="#252c32",
        arrowprops={"arrowstyle": "-", "color": "#4d565e", "lw": 0.75},
        zorder=10,
    )

    ax.set_xlim(79.65, 88.55)
    ax.set_ylim(25.8, 31.0)
    ax.set_aspect("equal")
    ax.set_anchor("W")
    lon_ticks = np.arange(80, 89, 1)
    lat_ticks = np.arange(26, 32, 1)
    ax.set_xticks(lon_ticks)
    ax.set_yticks(lat_ticks)
    ax.set_xticklabels([f"{value:.0f}°E" for value in lon_ticks], fontsize=7, color="#56616c")
    ax.set_yticklabels([f"{value:.0f}°N" for value in lat_ticks], fontsize=7, color="#56616c")
    ax.tick_params(axis="both", which="both", direction="out", length=2.5, width=0.7, pad=3)
    ax.grid(color="#7d8894", linewidth=0.4, alpha=0.28, zorder=0)
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_linewidth(1.25)
        spine.set_edgecolor("#535d66")
    add_panel_heading(ax, "a", "Nepal and immediate cross-border context")
    ax.legend(
        handles=[
            Patch(facecolor="#efb083", edgecolor="#a64c2a", label="Bagmati Province"),
            Line2D([0], [0], color="#b30000", lw=1.3, linestyle="--", label="Analysis extent"),
            Line2D([0], [0], marker="*", color="none", markerfacecolor="#111111", markeredgecolor="white", markersize=8, label="Reported source point"),
        ],
        loc="lower left",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.8,
    )


def style_map(
    ax: plt.Axes,
    bounds: rasterio.coords.BoundingBox,
    districts: gpd.GeoDataFrame,
    local_units: gpd.GeoDataFrame,
) -> None:
    local_units.boundary.plot(ax=ax, color="#87919a", linewidth=0.23, alpha=0.58, zorder=12)
    districts.boundary.plot(ax=ax, color="#3e4953", linewidth=0.75, alpha=0.85, zorder=13)
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


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with rasterio.open(STACK_PATH) as stack_ds, rasterio.open(CLASS_PATH) as class_ds:
        bounds = stack_ds.bounds
        crs = stack_ds.crs
        plot_width = round(PLOT_HEIGHT * stack_ds.width / stack_ds.height)
        extent = [bounds.left, bounds.right, bounds.bottom, bounds.top]

        scope = read_downsampled(
            stack_ds, 1, PLOT_HEIGHT, plot_width, Resampling.average
        ).filled(0) > 0
        mapped_unosat = read_downsampled(
            stack_ds, 2, PLOT_HEIGHT, plot_width, Resampling.average
        ).filled(0) > 0
        mapped_cems = read_downsampled(
            stack_ds, 3, PLOT_HEIGHT, plot_width, Resampling.average
        ).filled(0) > 0
        radar_evidence = read_downsampled(
            stack_ds, 4, PLOT_HEIGHT, plot_width, Resampling.average
        ).filled(0) > 0
        optical_evidence = read_downsampled(
            stack_ds, 5, PLOT_HEIGHT, plot_width, Resampling.average
        ).filled(0) > 0
        channel_context = read_downsampled(
            stack_ds, 6, PLOT_HEIGHT, plot_width, Resampling.average
        ).filled(0) > 0
        steep_context = read_downsampled(
            stack_ds, 7, PLOT_HEIGHT, plot_width, Resampling.average
        ).filled(0) > 0
        evidence_class = read_downsampled(
            class_ds, 1, PLOT_HEIGHT, plot_width, Resampling.nearest
        ).filled(0).astype(np.uint8)

        target_transform = stack_ds.transform
        target_width = stack_ds.width
        target_height = stack_ds.height

    with rasterio.open(RADAR_PATH) as radar_ds:
        radar_change = read_downsampled(
            radar_ds, 1, PLOT_HEIGHT, plot_width, Resampling.bilinear
        ).filled(np.nan)

    with rasterio.open(SLOPE_PATH) as slope_ds:
        with WarpedVRT(
            slope_ds,
            crs=crs,
            transform=target_transform,
            width=target_width,
            height=target_height,
            resampling=Resampling.bilinear,
        ) as slope_vrt:
            slope = read_downsampled(
                slope_vrt, 1, PLOT_HEIGHT, plot_width, Resampling.bilinear
            ).filled(np.nan)

    scope &= np.isfinite(radar_change)
    radar_change = np.ma.masked_where(~scope, radar_change)
    slope = np.ma.masked_where(~scope, slope)

    mapped_any = mapped_unosat | mapped_cems
    sensor_any = radar_evidence | optical_evidence
    source_combo = np.zeros(scope.shape, dtype=np.uint8)
    source_combo[sensor_any & ~mapped_any] = 1
    source_combo[mapped_any & ~sensor_any] = 2
    source_combo[mapped_any & sensor_any] = 3
    source_combo = np.ma.masked_where(~scope, source_combo)
    evidence_class = np.ma.masked_where(~scope, evidence_class)

    districts = gpd.read_file(ADMIN_PATH, layer="districts").to_crs(crs)
    local_units = gpd.read_file(ADMIN_PATH, layer="local_units").to_crs(crs)
    national_admin0 = gpd.read_file(NATIONAL_ADMIN0_PATH)
    national_admin1 = gpd.read_file(NATIONAL_ADMIN1_PATH)
    world_admin0 = gpd.read_file(WORLD_ADMIN0_PATH)
    rivers = gpd.read_file(HYDRO_PATH, layer="hydrorivers_context").to_crs(crs)
    rivers = rivers.cx[bounds.left : bounds.right, bounds.bottom : bounds.top]
    if "Strahler Order" in rivers.columns:
        rivers = rivers[rivers["Strahler Order"].fillna(0) >= 4]
    unosat = gpd.read_file(UNOSAT_PATH, layer="affected_extent").to_crs(crs)
    cems = gpd.read_file(CEMS_PATH, layer="observed_event").to_crs(crs)
    source_lonlat = gpd.read_file(MECHANISM_PATH, layer="reported_source_point").to_crs(4326)
    source = source_lonlat.to_crs(crs)
    analysis_extent_lonlat = gpd.GeoDataFrame(
        geometry=[box(bounds.left, bounds.bottom, bounds.right, bounds.top)],
        crs=crs,
    ).to_crs(4326)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "axes.linewidth": 0.65,
            "legend.frameon": True,
            "legend.framealpha": 0.93,
        }
    )
    fig = plt.figure(figsize=(13.1, 17.5), constrained_layout=True)
    grid = fig.add_gridspec(3, 2, height_ratios=[1.38, 1.0, 1.0])
    ax_a = fig.add_subplot(grid[0, :])
    ax_b = fig.add_subplot(grid[1, 0])
    ax_c = fig.add_subplot(grid[1, 1])
    ax_d = fig.add_subplot(grid[2, 0])
    ax_e = fig.add_subplot(grid[2, 1])

    add_location_panel(
        ax_a,
        world_admin0,
        national_admin0,
        national_admin1,
        source_lonlat,
        analysis_extent_lonlat,
    )

    radar_cmap = plt.get_cmap("RdBu_r").copy()
    radar_cmap.set_bad("white")
    radar_norm = TwoSlopeNorm(vmin=-5, vcenter=0, vmax=5)
    im_b = ax_b.imshow(
        radar_change,
        extent=extent,
        origin="upper",
        cmap=radar_cmap,
        norm=radar_norm,
        interpolation="bilinear",
        zorder=1,
    )
    unosat.boundary.plot(ax=ax_b, color="#d95f02", linewidth=1.05, zorder=16)
    cems.boundary.plot(ax=ax_b, color="#7b3294", linewidth=0.85, zorder=17)
    source.plot(ax=ax_b, marker="*", color="#111111", edgecolor="white", linewidth=0.55, markersize=68, zorder=18)
    style_map(ax_b, bounds, districts, local_units)
    add_panel_heading(ax_b, "b", "Sentinel-1 VH change, 16–28 Aug 2026")
    add_north_arrow(ax_b)
    add_scale_bar(ax_b, bounds)
    cbar_b = fig.colorbar(im_b, ax=ax_b, fraction=0.036, pad=0.016, shrink=0.76)
    cbar_b.set_label("Post-minus-pre VH change (dB)")
    ax_b.legend(
        handles=[
            Line2D([0], [0], color="#d95f02", lw=1.3, label="UNOSAT mapped extent"),
            Line2D([0], [0], color="#7b3294", lw=1.3, label="Copernicus observed event"),
            Line2D([0], [0], marker="*", color="none", markerfacecolor="#111111", markeredgecolor="white", markersize=8, label="Reported source point"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.8,
    )

    combo_colors = ["#eef1f3", "#4c78a8", "#f2a65a", "#8f4d78"]
    combo_cmap = ListedColormap(combo_colors)
    combo_cmap.set_bad("white")
    ax_c.imshow(
        source_combo,
        extent=extent,
        origin="upper",
        cmap=combo_cmap,
        norm=BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], combo_cmap.N),
        interpolation="nearest",
        zorder=1,
    )
    style_map(ax_c, bounds, districts, local_units)
    add_panel_heading(ax_c, "c", "Mapped and sensor evidence agreement")
    ax_c.legend(
        handles=[
            Patch(facecolor=combo_colors[0], edgecolor="#aeb5bc", label="No positive evidence"),
            Patch(facecolor=combo_colors[1], edgecolor="none", label="Sensor evidence only"),
            Patch(facecolor=combo_colors[2], edgecolor="none", label="Mapped evidence only"),
            Patch(facecolor=combo_colors[3], edgecolor="none", label="Mapped + sensor evidence"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.5,
    )

    slope_cmap = plt.get_cmap("YlOrBr").copy()
    slope_cmap.set_bad("white")
    im_d = ax_d.imshow(
        slope,
        extent=extent,
        origin="upper",
        cmap=slope_cmap,
        vmin=0,
        vmax=60,
        interpolation="bilinear",
        zorder=1,
    )
    steep_overlay = np.ma.masked_where(~(steep_context & scope), np.ones(scope.shape))
    channel_overlay = np.ma.masked_where(~(channel_context & scope), np.ones(scope.shape))
    ax_d.imshow(
        steep_overlay,
        extent=extent,
        origin="upper",
        cmap=ListedColormap(["#c44e52"]),
        alpha=0.16,
        interpolation="nearest",
        zorder=3,
    )
    ax_d.imshow(
        channel_overlay,
        extent=extent,
        origin="upper",
        cmap=ListedColormap(["#2a6fbb"]),
        alpha=0.42,
        interpolation="nearest",
        zorder=4,
    )
    if not rivers.empty:
        rivers.plot(ax=ax_d, color="#1f5f99", linewidth=0.42, alpha=0.78, zorder=6)
    style_map(ax_d, bounds, districts, local_units)
    add_panel_heading(ax_d, "d", "Terrain slope and channel context")
    cbar_d = fig.colorbar(im_d, ax=ax_d, fraction=0.036, pad=0.016, shrink=0.76)
    cbar_d.set_label("Terrain slope (degrees)")
    ax_d.legend(
        handles=[
            Patch(facecolor="#c44e52", alpha=0.35, edgecolor="none", label="Slope ≥ 30° context"),
            Line2D([0], [0], color="#1f5f99", lw=1.4, label="HydroRIVERS / 120 m context"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.8,
    )

    class_colors = ["#eef1f3", "#fdd49e", "#fc8d59", "#b30000"]
    class_cmap = ListedColormap(class_colors)
    class_cmap.set_bad("white")
    ax_e.imshow(
        evidence_class,
        extent=extent,
        origin="upper",
        cmap=class_cmap,
        norm=BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], class_cmap.N),
        interpolation="nearest",
        zorder=1,
    )
    unosat.boundary.plot(ax=ax_e, color="#d95f02", linewidth=0.72, alpha=0.82, zorder=16)
    cems.boundary.plot(ax=ax_e, color="#7b3294", linewidth=0.62, alpha=0.82, zorder=17)
    style_map(ax_e, bounds, districts, local_units)
    add_panel_heading(ax_e, "e", "Consensus evidence confidence class")
    ax_e.legend(
        handles=[
            Patch(facecolor=class_colors[0], edgecolor="#aeb5bc", label="Class 0: no positive evidence"),
            Patch(facecolor=class_colors[1], edgecolor="none", label="Class 1: sensor + context"),
            Patch(facecolor=class_colors[2], edgecolor="none", label="Class 2: mapped or multisensor"),
            Patch(facecolor=class_colors[3], edgecolor="none", label="Class 3: convergent evidence"),
        ],
        loc="lower right",
        fontsize=7,
        borderpad=0.5,
        handlelength=1.5,
    )

    # Freeze the automatically resolved layout, then make the spanning panel's
    # frame exactly match the outer edges of panels b and c without distorting it.
    fig.canvas.draw()
    a_position = ax_a.get_position()
    b_position = ax_b.get_position()
    c_position = ax_c.get_position()
    target_left = b_position.x0
    target_right = c_position.x1
    target_width = target_right - target_left
    data_aspect = abs(
        (ax_a.get_xlim()[1] - ax_a.get_xlim()[0])
        / (ax_a.get_ylim()[1] - ax_a.get_ylim()[0])
    )
    target_height = (
        target_width * fig.get_figwidth() / (data_aspect * fig.get_figheight())
    )
    target_bottom = a_position.y0 + (a_position.height - target_height) / 2
    fig.set_layout_engine("none")
    ax_a.set_position([target_left, target_bottom, target_width, target_height])
    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight", pad_inches=0.14, facecolor="white")
    plt.close(fig)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
