#!/usr/bin/env python3
"""Render a diagnostic PNG of the multi-source hazard-evidence consensus."""

from __future__ import annotations

import argparse
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from rasterio.enums import Resampling
from rasterio.windows import Window, bounds, get_data_window
from shapely.geometry import box


CLASS_RASTER = Path(
    "data/processed/geospatial/hazard/hazard_evidence_class_20m.tif"
)
ADMIN = Path("data/processed/geospatial/base/event_area_admin.gpkg")
OSM = Path("data/processed/geospatial/base/osm_pre_event_aoi.gpkg")
HYDRO = Path("data/processed/geospatial/context/hydrocryosphere_context.gpkg")
UNOSAT = Path(
    "data/processed/geospatial/reference/unosat_event_reference.gpkg"
)
CEMS = Path(
    "data/processed/geospatial/reference/copernicus_emsr927_damage_reference.gpkg"
)
EVENT_SOURCE = Path(
    "data/processed/geospatial/reference/event_mechanism_reference.gpkg"
)
OUTPUT = Path(
    "data/exp/data-preprocessing/figures/hazard_evidence_consensus_preview.png"
)
TARGET_CRS = "EPSG:32645"
MAX_RENDER_DIMENSION = 2200


def padded_window(window: Window, height: int, width: int, padding: int) -> Window:
    row_off = max(0, int(window.row_off) - padding)
    col_off = max(0, int(window.col_off) - padding)
    row_end = min(height, int(window.row_off + window.height) + padding)
    col_end = min(width, int(window.col_off + window.width) + padding)
    return Window(col_off, row_off, col_end - col_off, row_end - row_off)


def plot_outline(frame: gpd.GeoDataFrame, ax: plt.Axes, **kwargs: object) -> None:
    if not frame.empty:
        frame.boundary.plot(ax=ax, **kwargs)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output

    with rasterio.open(root / CLASS_RASTER) as source:
        full = source.read(1, masked=True)
        data_window = get_data_window(full)
        window = padded_window(data_window, source.height, source.width, 75)
        scale = max(window.height, window.width) / MAX_RENDER_DIMENSION
        out_height = max(1, int(round(window.height / max(scale, 1))))
        out_width = max(1, int(round(window.width / max(scale, 1))))
        image = source.read(
            1,
            window=window,
            out_shape=(out_height, out_width),
            resampling=Resampling.nearest,
            masked=True,
        )
        left, bottom, right, top = bounds(window, source.transform)
        crs = source.crs
    if crs is None:
        raise RuntimeError("Hazard evidence raster has no CRS")

    extent_polygon = box(left, bottom, right, top)
    districts = gpd.read_file(root / ADMIN, layer="districts").to_crs(crs)
    districts = districts.loc[districts.geometry.intersects(extent_polygon)].copy()
    roads = gpd.read_file(root / OSM, layer="roads").to_crs(crs)
    roads = roads.loc[
        roads.geometry.intersects(extent_polygon)
        & roads["highway"].isin(
            ["trunk", "trunk_link", "primary", "primary_link", "secondary"]
        )
    ].copy()
    rivers = gpd.read_file(root / HYDRO, layer="hydrorivers_context").to_crs(crs)
    rivers = rivers.loc[
        rivers.geometry.intersects(extent_polygon) & (rivers["Strahler Order"] >= 3)
    ].copy()
    unosat = gpd.read_file(root / UNOSAT, layer="affected_extent").to_crs(crs)
    cems = gpd.read_file(root / CEMS, layer="observed_event").to_crs(crs)
    aois = gpd.read_file(root / CEMS, layer="area_of_interest").to_crs(crs)
    event_source = gpd.read_file(
        root / EVENT_SOURCE, layer="reported_source_point"
    ).to_crs(crs)

    plt.rcParams.update(
        {
            "font.family": ["Heiti SC", "Arial Unicode MS", "DejaVu Sans"],
            "axes.unicode_minus": False,
        }
    )
    fig, ax = plt.subplots(figsize=(13.5, 13.0), dpi=180)
    ax.set_facecolor("#F4F6F5")

    display = np.ma.masked_where(image == 255, image)
    cmap = ListedColormap(["#E8ECEF", "#F4D35E", "#F28E2B", "#C92A2A"])
    ax.imshow(
        display,
        extent=(left, right, bottom, top),
        origin="upper",
        cmap=cmap,
        vmin=-0.5,
        vmax=3.5,
        interpolation="nearest",
        alpha=0.88,
        zorder=1,
    )
    districts.boundary.plot(ax=ax, color="#4E5961", linewidth=1.1, zorder=2)
    if not rivers.empty:
        rivers.plot(ax=ax, color="#2878B5", linewidth=0.7, alpha=0.80, zorder=3)
    if not roads.empty:
        roads.plot(ax=ax, color="#30343B", linewidth=0.65, alpha=0.72, zorder=4)
    plot_outline(
        unosat,
        ax,
        color="#7B2CBF",
        linewidth=1.3,
        linestyle=(0, (4, 3)),
        zorder=5,
    )
    plot_outline(
        cems,
        ax,
        color="#006D77",
        linewidth=1.0,
        linestyle=(0, (2, 2)),
        zorder=5,
    )
    event_source.plot(
        ax=ax,
        marker="*",
        color="#111111",
        edgecolor="#FFFFFF",
        linewidth=0.8,
        markersize=170,
        zorder=7,
    )

    for _, row in aois.iterrows():
        point = row.geometry.representative_point()
        ax.annotate(
            str(row["AOI"]),
            (point.x, point.y),
            xytext=(4, 4),
            textcoords="offset points",
            fontsize=8.5,
            color="#202428",
            weight="medium",
            zorder=8,
            path_effects=[],
        )
    source_point = event_source.geometry.iloc[0]
    ax.annotate(
        "Reported source",
        (source_point.x, source_point.y),
        xytext=(7, 5),
        textcoords="offset points",
        fontsize=9,
        color="#111111",
        zorder=8,
    )

    x_padding = (right - left) * 0.01
    y_padding = (top - bottom) * 0.01
    ax.set_xlim(left - x_padding, right + x_padding)
    ax.set_ylim(bottom - y_padding, top + y_padding)
    ax.set_aspect("equal")
    ax.set_xlabel("UTM Easting (m), Zone 45N")
    ax.set_ylabel("UTM Northing (m), Zone 45N")
    ax.set_title(
        "2026 Rasuwa–Trishuli Multi-source Hazard Evidence Footprint (Diagnostic)",
        fontsize=16,
        weight="medium",
        pad=18,
    )
    ax.text(
        0.5,
        1.005,
        "Classes represent evidence confidence, not physical hazard intensity; rapid mapping is not field validated",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10.5,
        color="#4E5961",
    )

    scale_length = 10_000
    scale_x = left + (right - left) * 0.065
    scale_y = bottom + (top - bottom) * 0.055
    ax.plot(
        [scale_x, scale_x + scale_length],
        [scale_y, scale_y],
        color="#111111",
        linewidth=3,
        solid_capstyle="butt",
        zorder=9,
    )
    ax.plot(
        [scale_x, scale_x],
        [scale_y - 250, scale_y + 250],
        color="#111111",
        linewidth=1.2,
        zorder=9,
    )
    ax.plot(
        [scale_x + scale_length, scale_x + scale_length],
        [scale_y - 250, scale_y + 250],
        color="#111111",
        linewidth=1.2,
        zorder=9,
    )
    ax.text(
        scale_x + scale_length / 2,
        scale_y + 650,
        "10 km",
        ha="center",
        va="bottom",
        fontsize=9,
        color="#111111",
        zorder=9,
    )
    north_x = right - (right - left) * 0.055
    north_y = top - (top - bottom) * 0.08
    ax.annotate(
        "N",
        xy=(north_x, north_y + 3500),
        xytext=(north_x, north_y),
        ha="center",
        va="center",
        fontsize=12,
        weight="medium",
        arrowprops={"arrowstyle": "-|>", "color": "#111111", "lw": 1.5},
        zorder=9,
    )

    handles = [
        Patch(facecolor="#C92A2A", label="Class 3: convergent evidence (primary)"),
        Patch(facecolor="#F28E2B", label="Class 2: mapped or dual-sensor evidence (alternative)"),
        Patch(facecolor="#F4D35E", label="Class 1: sensor screening evidence (sensitivity)"),
        Patch(facecolor="#E8ECEF", label="Class 0: analysed, no positive evidence rule"),
        Line2D([0], [0], color="#7B2CBF", lw=1.5, ls="--", label="UNOSAT boundary"),
        Line2D([0], [0], color="#006D77", lw=1.3, ls=":", label="Copernicus boundary"),
        Line2D([0], [0], color="#2878B5", lw=1.2, label="Major river"),
        Line2D([0], [0], color="#30343B", lw=1.0, label="Major road"),
        Line2D(
            [0],
            [0],
            marker="*",
            color="none",
            markerfacecolor="#111111",
            markersize=11,
            label="Reported source",
        ),
    ]
    ax.legend(
        handles=handles,
        loc="lower right",
        frameon=True,
        framealpha=0.94,
        facecolor="#FFFFFF",
        edgecolor="#B8C0C5",
        fontsize=9,
        title="Legend",
        title_fontsize=10,
    )
    ax.grid(color="#AAB2B8", linewidth=0.35, alpha=0.35)
    ax.tick_params(labelsize=8.5)
    fig.text(
        0.5,
        0.018,
        "Data: UNOSAT, Copernicus EMSR927, Sentinel-1/2, HydroRIVERS, and OSM; 20 m analysis grid",
        ha="center",
        fontsize=8.5,
        color="#4E5961",
    )
    fig.tight_layout(rect=(0.02, 0.035, 0.98, 0.965))
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=180, bbox_inches="tight", facecolor="#FFFFFF")
    plt.close(fig)
    print({"output": str(output), "bytes": output.stat().st_size})


if __name__ == "__main__":
    main()
