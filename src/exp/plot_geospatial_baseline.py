#!/usr/bin/env python3
"""Plot the event-area terrain and pre-event OSM baseline."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/ke03-matplotlib")

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter
from rasterio.enums import Resampling
from rasterio.plot import plotting_extent


CRS = "EPSG:32645"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    dem_path = root / "data/processed/geospatial/base/copernicus_glo30_aoi_utm45n.tif"
    admin_path = root / "data/processed/geospatial/base/event_area_admin.gpkg"
    osm_path = root / "data/processed/geospatial/base/osm_pre_event_aoi.gpkg"
    output = (
        root
        / "data/exp/data-briefing/figures/geospatial/study_area_pre_event_baseline.png"
    )
    facility_summary = (
        root
        / "data/exp/data-briefing/tables/osm_facility_category_summary.csv"
    )

    districts = gpd.read_file(admin_path, layer="districts").to_crs(CRS)
    local_units = gpd.read_file(admin_path, layer="local_units").to_crs(CRS)
    roads = gpd.read_file(osm_path, layer="roads").to_crs(CRS)
    waterways = gpd.read_file(osm_path, layer="waterways").to_crs(CRS)
    settlements = gpd.read_file(osm_path, layer="settlements").to_crs(CRS)
    facilities = gpd.read_file(osm_path, layer="facilities").to_crs(CRS)

    facility_summary.parent.mkdir(parents=True, exist_ok=True)
    (
        facilities.groupby("facility_category", dropna=False)
        .size()
        .rename("feature_count")
        .reset_index()
        .sort_values("feature_count", ascending=False)
        .to_csv(facility_summary, index=False)
    )

    with rasterio.open(dem_path) as src:
        scale = 4
        dem = src.read(
            1,
            out_shape=(1, src.height // scale, src.width // scale),
            masked=True,
            resampling=Resampling.bilinear,
        )
        extent = plotting_extent(src)

    major_order = [
        "trunk",
        "trunk_link",
        "primary",
        "primary_link",
        "secondary",
        "secondary_link",
        "tertiary",
        "tertiary_link",
    ]
    major_roads = roads.loc[roads["highway"].isin(major_order)].copy()
    rivers = waterways.loc[waterways["waterway"].isin(["river", "stream", "canal"])].copy()
    health = facilities.loc[facilities["facility_category"].eq("health")]
    emergency = facilities.loc[facilities["facility_category"].eq("emergency")]

    fig, ax = plt.subplots(figsize=(10.5, 10.5), constrained_layout=True)
    valid = dem.compressed()
    vmin, vmax = np.percentile(valid, [2, 98])
    image = ax.imshow(
        dem,
        extent=extent,
        cmap="terrain",
        vmin=vmin,
        vmax=vmax,
        interpolation="bilinear",
        zorder=0,
    )
    local_units.boundary.plot(ax=ax, color="white", linewidth=0.25, alpha=0.48, zorder=2)
    districts.boundary.plot(ax=ax, color="#202020", linewidth=1.25, zorder=4)
    rivers.plot(ax=ax, color="#2b83ba", linewidth=0.45, alpha=0.8, zorder=3)
    major_roads.plot(ax=ax, color="#d73027", linewidth=0.7, alpha=0.9, zorder=5)
    health.plot(ax=ax, color="#7b3294", marker="+", markersize=14, linewidth=0.8, zorder=7)
    emergency.plot(ax=ax, color="#fdae61", marker="^", markersize=8, zorder=7)

    named = settlements.loc[
        settlements["place"].isin(["town", "village"])
        & settlements["name"].notna()
        & settlements["name"].astype(str).str.strip().ne("")
        & settlements["name"].map(lambda value: str(value).isascii())
    ].copy()
    named["rank"] = named["place"].map({"town": 0, "village": 1})
    named = named.sort_values(["rank", "name"]).head(14)
    named.plot(ax=ax, color="#111111", markersize=10, zorder=8)
    for row in named.itertuples():
        ax.annotate(
            str(row.name),
            (row.geometry.x, row.geometry.y),
            xytext=(3, 3),
            textcoords="offset points",
            fontsize=6.5,
            color="#111111",
            zorder=9,
        )

    district_points = districts.copy()
    district_points["geometry"] = district_points.representative_point()
    for row in district_points.itertuples():
        ax.annotate(
            row.adm2_name.upper(),
            (row.geometry.x, row.geometry.y),
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color="white",
            path_effects=[],
            bbox={"boxstyle": "round,pad=0.2", "fc": "#202020", "ec": "none", "alpha": 0.65},
            zorder=10,
        )

    core_bounds = districts.total_bounds
    padding = 12_000
    ax.set_xlim(core_bounds[0] - padding, core_bounds[2] + padding)
    ax.set_ylim(core_bounds[1] - padding, core_bounds[3] + padding)
    ax.set_aspect("equal")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
    ax.set_xlabel("Easting (km), WGS 84 / UTM zone 45N")
    ax.set_ylabel("Northing (km), WGS 84 / UTM zone 45N")
    ax.set_title(
        "Rasuwa–Nuwakot–Dhading event corridor\nTopography and pre-event transport/service baseline",
        loc="left",
        fontsize=14,
        fontweight="bold",
    )

    x0 = core_bounds[0] - 4_000
    y0 = core_bounds[1] - 7_000
    ax.plot([x0, x0 + 20_000], [y0, y0], color="black", linewidth=3, zorder=12)
    ax.plot([x0, x0 + 10_000], [y0, y0], color="white", linewidth=1.2, zorder=13)
    ax.text(x0, y0 + 1_500, "0", fontsize=7, ha="center")
    ax.text(x0 + 10_000, y0 + 1_500, "10", fontsize=7, ha="center")
    ax.text(x0 + 20_000, y0 + 1_500, "20 km", fontsize=7, ha="center")
    ax.annotate(
        "N",
        xy=(0.96, 0.91),
        xytext=(0.96, 0.82),
        xycoords="axes fraction",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        arrowprops={"facecolor": "black", "width": 2.5, "headwidth": 8},
        zorder=12,
    )

    legend = [
        Line2D([0], [0], color="#d73027", lw=1.5, label="Major pre-event road"),
        Line2D([0], [0], color="#2b83ba", lw=1.2, label="River / stream"),
        Line2D([0], [0], marker="+", color="#7b3294", lw=0, label="Health facility"),
        Line2D([0], [0], marker="^", color="#fdae61", lw=0, label="Emergency facility"),
        Patch(facecolor="none", edgecolor="#202020", label="District boundary"),
    ]
    ax.legend(handles=legend, loc="lower right", frameon=True, framealpha=0.92, fontsize=8)
    colorbar = fig.colorbar(image, ax=ax, shrink=0.62, pad=0.02)
    colorbar.set_label("Elevation (m)")
    fig.text(
        0.01,
        0.005,
        "Sources: Copernicus DEM GLO-30; Nepal COD-AB; OpenStreetMap snapshot 25 Aug 2026. "
        "Map is a baseline coverage audit, not a validated hazard footprint.",
        fontsize=7,
        color="#444444",
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=220, facecolor="white")
    plt.close(fig)
    print({"output": str(output), "major_roads": len(major_roads), "labels": len(named)})


if __name__ == "__main__":
    main()
