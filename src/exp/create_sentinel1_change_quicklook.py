#!/usr/bin/env python3
"""Validate aligned Sentinel-1 RTC pairs and create screening change products."""

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
from matplotlib.ticker import FuncFormatter
from rasterio.enums import Resampling
from rasterio.plot import plotting_extent


PRE_DATE = "2026-08-16"
POST_DATE = "2026-08-28"
NODATA = -9999.0


def read_band(path: Path) -> tuple[np.ndarray, dict, tuple[float, float, float, float]]:
    with rasterio.open(path) as source:
        array = source.read(1)
        profile = source.profile.copy()
        extent = plotting_extent(source)
    return array, profile, extent


def write_change(path: Path, array: np.ndarray, profile: dict, band: str) -> None:
    output_profile = profile.copy()
    output_profile.update(
        dtype="float32",
        nodata=NODATA,
        compress="DEFLATE",
        predictor=3,
        tiled=True,
        blockxsize=512,
        blockysize=512,
        BIGTIFF="IF_SAFER",
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(path, "w", **output_profile) as destination:
        destination.write(array.astype("float32"), 1)
        destination.update_tags(
            metric="post-event minus pre-event backscatter",
            units="dB",
            pre_event_date=PRE_DATE,
            post_event_date=POST_DATE,
            polarization=band,
            interpretation="screening layer; not a validated hazard footprint",
        )
        destination.build_overviews([2, 4, 8, 16], Resampling.average)
        destination.update_tags(ns="rio_overview", resampling="average")


def aggregate_mean(array: np.ndarray, factor: int = 5) -> np.ma.MaskedArray:
    height = array.shape[0] // factor * factor
    width = array.shape[1] // factor * factor
    cropped = array[:height, :width]
    masked = np.ma.masked_where(cropped == NODATA, cropped)
    return masked.reshape(height // factor, factor, width // factor, factor).mean(axis=(1, 3))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    satellite_dir = root / "data/processed/geospatial/satellite"
    inputs = {
        (date, band): satellite_dir / f"sentinel1_rtc_{date}_{band.lower()}_20m.tif"
        for date in (PRE_DATE, POST_DATE)
        for band in ("VV", "VH")
    }
    arrays: dict[tuple[str, str], np.ndarray] = {}
    reference_profile = None
    reference_extent = None
    for key, path in inputs.items():
        array, profile, extent = read_band(path)
        signature = (profile["crs"], profile["transform"], profile["width"], profile["height"])
        if reference_profile is None:
            reference_profile = profile
            reference_extent = extent
            reference_signature = signature
        elif signature != reference_signature:
            raise RuntimeError(f"Raster grid mismatch: {path}")
        arrays[key] = array

    assert reference_profile is not None and reference_extent is not None
    changes: dict[str, np.ndarray] = {}
    rows: list[dict[str, object]] = []
    for band in ("VV", "VH"):
        pre = arrays[(PRE_DATE, band)]
        post = arrays[(POST_DATE, band)]
        valid = (pre > 0) & (post > 0) & np.isfinite(pre) & np.isfinite(post)
        change = np.full(pre.shape, NODATA, dtype="float32")
        change[valid] = 10 * np.log10(post[valid]) - 10 * np.log10(pre[valid])
        changes[band] = change
        path = satellite_dir / f"sentinel1_rtc_change_{PRE_DATE}_{POST_DATE}_{band.lower()}_db_20m.tif"
        write_change(path, change, reference_profile, band)
        values = change[change != NODATA]
        sampled = values[:: max(1, len(values) // 1_000_000)]
        q = np.percentile(sampled, [0, 1, 5, 50, 95, 99, 100])
        rows.append(
            {
                "band": band,
                "pre_date": PRE_DATE,
                "post_date": POST_DATE,
                "valid_pixels": len(values),
                "coverage_fraction": round(len(values) / change.size, 6),
                "min_db": round(float(q[0]), 4),
                "p01_db": round(float(q[1]), 4),
                "p05_db": round(float(q[2]), 4),
                "median_db": round(float(q[3]), 4),
                "p95_db": round(float(q[4]), 4),
                "p99_db": round(float(q[5]), 4),
                "max_db": round(float(q[6]), 4),
                "output": str(path.relative_to(root)),
            }
        )

    stats_path = root / "data/exp/data-briefing/tables/sentinel1_rtc_change_screening.csv"
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    with stats_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    admin_path = root / "data/processed/geospatial/base/event_area_admin.gpkg"
    osm_path = root / "data/processed/geospatial/base/osm_pre_event_aoi.gpkg"
    districts = gpd.read_file(admin_path, layer="districts").to_crs(reference_profile["crs"])
    roads = gpd.read_file(osm_path, layer="roads").to_crs(reference_profile["crs"])
    waterways = gpd.read_file(osm_path, layer="waterways").to_crs(reference_profile["crs"])
    major_roads = roads.loc[roads["highway"].isin(["trunk", "primary", "secondary"])]
    rivers = waterways.loc[waterways["waterway"].isin(["river", "stream"])]

    pre_vv_db = np.full(arrays[(PRE_DATE, "VV")].shape, NODATA, dtype="float32")
    post_vv_db = np.full(arrays[(POST_DATE, "VV")].shape, NODATA, dtype="float32")
    pre_valid = arrays[(PRE_DATE, "VV")] > 0
    post_valid = arrays[(POST_DATE, "VV")] > 0
    pre_vv_db[pre_valid] = 10 * np.log10(arrays[(PRE_DATE, "VV")][pre_valid])
    post_vv_db[post_valid] = 10 * np.log10(arrays[(POST_DATE, "VV")][post_valid])

    panels = [
        (aggregate_mean(pre_vv_db), f"Pre-event VV | {PRE_DATE}", "gray", -20, 2),
        (aggregate_mean(post_vv_db), f"Post-event VV | {POST_DATE}", "gray", -20, 2),
        (aggregate_mean(changes["VV"]), "VV change (post − pre)", "RdBu_r", -5, 5),
        (aggregate_mean(changes["VH"]), "VH change (post − pre)", "RdBu_r", -5, 5),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 11.5))
    fig.subplots_adjust(left=0.06, right=0.96, bottom=0.085, top=0.90, hspace=0.18, wspace=0.18)
    for ax, (image, title, cmap, vmin, vmax) in zip(axes.flat, panels):
        rendered = ax.imshow(
            image,
            extent=reference_extent,
            origin="upper",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            interpolation="bilinear",
        )
        rivers.plot(ax=ax, color="#2b83ba", linewidth=0.25, alpha=0.65)
        major_roads.plot(ax=ax, color="#fdae61", linewidth=0.4, alpha=0.8)
        districts.boundary.plot(ax=ax, color="black", linewidth=0.75)
        ax.set_title(title, loc="left", fontsize=11, fontweight="bold")
        ax.set_xlim(reference_extent[0], reference_extent[1])
        ax.set_ylim(reference_extent[2], reference_extent[3])
        ax.set_aspect("equal")
        ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:.0f}"))
        colorbar = fig.colorbar(rendered, ax=ax, shrink=0.72, pad=0.015)
        colorbar.set_label("Backscatter (dB)" if "event VV" in title else "Change (dB)")

    axes[1, 0].set_xlabel("Easting (km), WGS 84 / UTM zone 45N")
    axes[1, 1].set_xlabel("Easting (km), WGS 84 / UTM zone 45N")
    axes[0, 0].set_ylabel("Northing (km)")
    axes[1, 0].set_ylabel("Northing (km)")
    legend = [
        Line2D([0], [0], color="#fdae61", lw=1.3, label="Major pre-event road"),
        Line2D([0], [0], color="#2b83ba", lw=1.1, label="River / stream"),
        Line2D([0], [0], color="black", lw=1.1, label="District boundary"),
    ]
    fig.legend(handles=legend, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 0.947))
    fig.suptitle(
        "Rasuwa event corridor: Sentinel-1 RTC change screening",
        x=0.02,
        ha="left",
        fontsize=15,
        fontweight="bold",
    )
    fig.text(
        0.01,
        0.025,
        "Source: Microsoft Planetary Computer Sentinel-1 RTC (relative orbit 85, ascending). "
        "Display aggregated to 100 m. Backscatter change alone is not a validated hazard footprint.",
        fontsize=7.5,
        color="#444444",
    )
    figure_path = (
        root
        / "data/exp/data-briefing/figures/geospatial/sentinel1_rtc_change_screening.png"
    )
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(figure_path, dpi=220, facecolor="white")
    plt.close(fig)
    print({"figure": str(figure_path), "stats": str(stats_path), "grid_aligned": True})


if __name__ == "__main__":
    main()
