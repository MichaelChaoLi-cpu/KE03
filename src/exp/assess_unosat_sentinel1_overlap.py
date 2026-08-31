#!/usr/bin/env python3
"""Compare Sentinel-1 change screening values with the UNOSAT reference extent."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import os
from pathlib import Path

RASTERIO_SPEC = importlib.util.find_spec("rasterio")
if RASTERIO_SPEC is None or not RASTERIO_SPEC.submodule_search_locations:
    raise RuntimeError("rasterio is not installed in the active environment")
PROJ_DATA_DIR = Path(next(iter(RASTERIO_SPEC.submodule_search_locations))) / "proj_data"
os.environ["PROJ_DATA"] = str(PROJ_DATA_DIR)
os.environ["PROJ_LIB"] = str(PROJ_DATA_DIR)
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/ke03-matplotlib")

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter
from rasterio.enums import Resampling
from rasterio.features import rasterize
from rasterio.plot import plotting_extent


NODATA = -9999.0


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    reference_path = root / "data/processed/geospatial/reference/unosat_event_reference.gpkg"
    affected = gpd.read_file(reference_path, layer="affected_extent")
    analysis = gpd.read_file(reference_path, layer="analysis_extent")
    rows: list[dict[str, object]] = []
    vv_array = None
    vv_profile = None
    vv_extent = None

    for band in ("VV", "VH"):
        path = (
            root
            / "data/processed/geospatial/satellite"
            / f"sentinel1_rtc_change_2026-08-16_2026-08-28_{band.lower()}_db_20m.tif"
        )
        with rasterio.open(path) as source:
            array = source.read(1)
            profile = source.profile.copy()
            extent = plotting_extent(source)
        affected_grid = rasterize(
            ((geometry, 1) for geometry in affected.to_crs(profile["crs"]).geometry),
            out_shape=array.shape,
            transform=profile["transform"],
            fill=0,
            dtype="uint8",
        ).astype(bool)
        analysis_grid = rasterize(
            ((geometry, 1) for geometry in analysis.to_crs(profile["crs"]).geometry),
            out_shape=array.shape,
            transform=profile["transform"],
            fill=0,
            dtype="uint8",
        ).astype(bool)
        valid = (array != NODATA) & np.isfinite(array)
        zones = {
            "unosat_affected": affected_grid & valid,
            "analysis_extent_unmapped": analysis_grid & ~affected_grid & valid,
        }
        for zone, mask in zones.items():
            values = array[mask]
            q = np.percentile(values, [5, 25, 50, 75, 95])
            rows.append(
                {
                    "band": band,
                    "zone": zone,
                    "pixels": len(values),
                    "area_km2_at_20m": round(len(values) * 400 / 1_000_000, 4),
                    "mean_db": round(float(values.mean()), 4),
                    "p05_db": round(float(q[0]), 4),
                    "p25_db": round(float(q[1]), 4),
                    "median_db": round(float(q[2]), 4),
                    "p75_db": round(float(q[3]), 4),
                    "p95_db": round(float(q[4]), 4),
                    "share_decrease_le_minus2db": round(float((values <= -2).mean()), 6),
                    "share_increase_ge_2db": round(float((values >= 2).mean()), 6),
                    "interpretation": "descriptive discrimination check; not causal validation",
                }
            )
        if band == "VV":
            vv_array, vv_profile, vv_extent = array, profile, extent

    stats_path = root / "data/exp/data-briefing/tables/sentinel1_rtc_unosat_overlap.csv"
    write_rows(stats_path, rows)

    assert vv_array is not None and vv_profile is not None and vv_extent is not None
    dem_path = root / "data/processed/geospatial/base/copernicus_glo30_aoi_utm45n.tif"
    with rasterio.open(dem_path) as source:
        scale = 4
        dem = source.read(
            1,
            out_shape=(source.height // scale, source.width // scale),
            masked=True,
            resampling=Resampling.bilinear,
        )
        dem_extent = plotting_extent(source)

    osm_path = root / "data/processed/geospatial/base/osm_pre_event_aoi.gpkg"
    roads = gpd.read_file(osm_path, layer="roads").to_crs(vv_profile["crs"])
    waterways = gpd.read_file(osm_path, layer="waterways").to_crs(vv_profile["crs"])
    major_roads = roads.loc[roads["highway"].isin(["trunk", "primary", "secondary"])]
    rivers = waterways.loc[waterways["waterway"].isin(["river", "stream"])]
    affected = affected.to_crs(vv_profile["crs"])
    analysis = analysis.to_crs(vv_profile["crs"])
    bounds = analysis.total_bounds
    padding = 4_000

    vv_masked = np.ma.masked_where(vv_array == NODATA, vv_array)
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 7.2))
    fig.subplots_adjust(left=0.065, right=0.96, bottom=0.12, top=0.83, wspace=0.18)
    elevation_values = dem.compressed()
    elevation_range = np.percentile(elevation_values, [2, 98])
    terrain = axes[0].imshow(
        dem,
        extent=dem_extent,
        cmap="terrain",
        vmin=elevation_range[0],
        vmax=elevation_range[1],
        interpolation="bilinear",
    )
    affected.plot(ax=axes[0], facecolor="#d73027", edgecolor="#7f0000", alpha=0.55, linewidth=0.7)
    analysis.boundary.plot(ax=axes[0], color="#542788", linewidth=1.1, linestyle="--")
    rivers.plot(ax=axes[0], color="#2b83ba", linewidth=0.35, alpha=0.7)
    major_roads.plot(ax=axes[0], color="#fdae61", linewidth=0.65, alpha=0.9)
    axes[0].set_title("UNOSAT preliminary affected extent", loc="left", fontweight="bold")
    cb0 = fig.colorbar(terrain, ax=axes[0], shrink=0.75, pad=0.015)
    cb0.set_label("Elevation (m)")

    radar = axes[1].imshow(
        vv_masked,
        extent=vv_extent,
        cmap="RdBu_r",
        vmin=-5,
        vmax=5,
        interpolation="bilinear",
    )
    affected.boundary.plot(ax=axes[1], color="#ffff00", linewidth=1.0)
    analysis.boundary.plot(ax=axes[1], color="#222222", linewidth=0.9, linestyle="--")
    rivers.plot(ax=axes[1], color="#2b83ba", linewidth=0.25, alpha=0.55)
    axes[1].set_title("Sentinel-1 VV change with UNOSAT outline", loc="left", fontweight="bold")
    cb1 = fig.colorbar(radar, ax=axes[1], shrink=0.75, pad=0.015)
    cb1.set_label("Post − pre backscatter (dB)")

    for ax in axes:
        ax.set_xlim(bounds[0] - padding, bounds[2] + padding)
        ax.set_ylim(bounds[1] - padding, bounds[3] + padding)
        ax.set_aspect("equal")
        ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
        ax.set_xlabel("Easting (km), WGS 84 / UTM zone 45N")
    axes[0].set_ylabel("Northing (km)")
    legend = [
        Patch(facecolor="#d73027", edgecolor="#7f0000", alpha=0.55, label="UNOSAT affected extent"),
        Line2D([0], [0], color="#542788", linestyle="--", label="UNOSAT analysis extent"),
        Line2D([0], [0], color="#fdae61", label="Major pre-event road"),
        Line2D([0], [0], color="#2b83ba", label="River / stream"),
    ]
    fig.legend(handles=legend, loc="upper center", ncol=4, bbox_to_anchor=(0.5, 0.90))
    fig.suptitle(
        "Independent event reference and Sentinel-1 screening overlap",
        x=0.02,
        y=0.98,
        ha="left",
        fontsize=15,
        fontweight="bold",
    )
    fig.text(
        0.01,
        0.025,
        "UNOSAT extent derived from PlanetScope (26 Aug) and Sentinel-2 (27 Aug); preliminary and not field validated. "
        "Radar difference is relative orbit 85, 16–28 Aug 2026. Spatial overlap is screening evidence, not confirmed damage.",
        fontsize=7.5,
        color="#444444",
    )
    figure_path = (
        root
        / "data/exp/data-briefing/figures/geospatial/unosat_reference_sentinel1_overlap.png"
    )
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(figure_path, dpi=220, facecolor="white")
    plt.close(fig)
    print({"stats": str(stats_path), "figure": str(figure_path), "rows": len(rows)})


if __name__ == "__main__":
    main()
