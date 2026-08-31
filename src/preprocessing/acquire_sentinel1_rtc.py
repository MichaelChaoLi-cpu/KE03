#!/usr/bin/env python3
"""Stream and mosaic event-window Sentinel-1 RTC COGs for the hazard corridor."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import urllib.parse
import urllib.request
from contextlib import ExitStack
from pathlib import Path

import numpy as np

# rasterio 1.5 requires the PROJ database shipped with its own wheel.  The
# workstation also exposes older Anaconda/Homebrew databases, so pin GDAL to
# rasterio's matching data directory before importing rasterio.
RASTERIO_SPEC = importlib.util.find_spec("rasterio")
if RASTERIO_SPEC is None or not RASTERIO_SPEC.submodule_search_locations:
    raise RuntimeError("rasterio is not installed in the active environment")
PROJ_DATA_DIR = Path(next(iter(RASTERIO_SPEC.submodule_search_locations))) / "proj_data"
os.environ["PROJ_DATA"] = str(PROJ_DATA_DIR)
os.environ["PROJ_LIB"] = str(PROJ_DATA_DIR)

import rasterio
from rasterio.enums import Resampling
from rasterio.merge import merge
from rasterio.warp import transform_bounds


STAC_API = "https://planetarycomputer.microsoft.com/api/stac/v1"
TOKEN_API = "https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel-1-rtc"
COLLECTION = "sentinel-1-rtc"
SEARCH_BBOX = (84.5, 27.55, 85.95, 28.60)
SATELLITE_BBOX = (84.75, 27.65, 85.75, 28.50)
TARGET_CRS = "EPSG:32645"
TARGET_RESOLUTION = 20
TARGET_ORBIT = 85
TARGET_DATES = ("2026-08-16", "2026-08-28")
TARGET_BANDS = ("vv", "vh")
NODATA = -9999.0


def read_json(url: str) -> dict:
    request = urllib.request.Request(
        url, headers={"User-Agent": "KE03-sentinel1-rtc-acquisition/1.0"}
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.load(response)


def search_items() -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "collections": COLLECTION,
            "bbox": ",".join(map(str, SEARCH_BBOX)),
            "datetime": "2026-08-01T00:00:00Z/2026-08-31T23:59:59Z",
            "limit": 100,
        }
    )
    features = read_json(f"{STAC_API}/search?{params}").get("features", [])
    selected = []
    for feature in features:
        properties = feature.get("properties", {})
        acquired = str(properties.get("datetime", ""))
        if properties.get("sat:relative_orbit") != TARGET_ORBIT:
            continue
        if not any(acquired.startswith(date) for date in TARGET_DATES):
            continue
        if not all(band in feature.get("assets", {}) for band in TARGET_BANDS):
            continue
        selected.append(feature)
    return sorted(selected, key=lambda item: item["id"])


def write_raster(path: Path, array: np.ndarray, transform, crs: str, tags: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    profile = {
        "driver": "GTiff",
        "height": array.shape[0],
        "width": array.shape[1],
        "count": 1,
        "dtype": "float32",
        "crs": crs,
        "transform": transform,
        "nodata": NODATA,
        "compress": "DEFLATE",
        "predictor": 3,
        "tiled": True,
        "blockxsize": 512,
        "blockysize": 512,
        "BIGTIFF": "IF_SAFER",
    }
    with rasterio.open(path, "w", **profile) as destination:
        destination.write(array.astype("float32"), 1)
        destination.update_tags(**tags)
        destination.build_overviews([2, 4, 8, 16], Resampling.average)
        destination.update_tags(ns="rio_overview", resampling="average")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    output_dir = root / "data/processed/geospatial/satellite"
    metadata_dir = root / "data/raw/geospatial/satellite/sentinel1_rtc/metadata"
    inventory_path = (
        root / "data/exp/data-briefing/tables/sentinel1_rtc_acquisition_inventory.csv"
    )

    items = search_items()
    by_date = {
        date: [item for item in items if item["properties"]["datetime"].startswith(date)]
        for date in TARGET_DATES
    }
    for date, date_items in by_date.items():
        if len(date_items) < 2:
            raise RuntimeError(f"Expected at least two orbit-85 frames for {date}, got {len(date_items)}")

    metadata_dir.mkdir(parents=True, exist_ok=True)
    unsigned_metadata = {
        "collection": COLLECTION,
        "search_bbox_wgs84": SEARCH_BBOX,
        "satellite_bbox_wgs84": SATELLITE_BBOX,
        "target_crs": TARGET_CRS,
        "target_resolution_m": TARGET_RESOLUTION,
        "relative_orbit": TARGET_ORBIT,
        "items": items,
        "note": "Unsigned STAC metadata only; temporary SAS tokens are never saved.",
    }
    metadata_path = metadata_dir / "sentinel1_rtc_selected_items.json"
    metadata_path.write_text(json.dumps(unsigned_metadata, indent=2), encoding="utf-8")

    token = read_json(TOKEN_API)["token"]
    target_bounds = transform_bounds(
        "EPSG:4326", TARGET_CRS, *SATELLITE_BBOX, densify_pts=21
    )
    gdal_options = {
        "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",
        "CPL_VSIL_CURL_ALLOWED_EXTENSIONS": ".tif,.tiff",
        "GDAL_HTTP_MULTIRANGE": "YES",
        "VSI_CACHE": "TRUE",
        "VSI_CACHE_SIZE": 50_000_000,
    }
    inventory_rows: list[dict[str, object]] = []

    for date in TARGET_DATES:
        for band in TARGET_BANDS:
            with rasterio.Env(**gdal_options), ExitStack() as stack:
                sources = []
                for item in by_date[date]:
                    unsigned_href = item["assets"][band]["href"]
                    signed_href = f"{unsigned_href}?{token}"
                    sources.append(stack.enter_context(rasterio.open(signed_href)))
                mosaic, transform = merge(
                    sources,
                    bounds=target_bounds,
                    res=TARGET_RESOLUTION,
                    nodata=NODATA,
                    dtype="float32",
                    resampling=Resampling.bilinear,
                    method="first",
                    target_aligned_pixels=True,
                )
            array = mosaic[0]
            output = output_dir / f"sentinel1_rtc_{date}_{band}_20m.tif"
            tags = {
                "collection": COLLECTION,
                "acquisition_date": date,
                "polarization": band.upper(),
                "relative_orbit": str(TARGET_ORBIT),
                "orbit_state": "ascending",
                "pixel_content": "linear gamma naught RTC",
                "source_item_ids": ",".join(item["id"] for item in by_date[date]),
            }
            write_raster(output, array, transform, TARGET_CRS, tags)

            valid = array[np.isfinite(array) & (array != NODATA) & (array >= 0)]
            sampled = valid[:: max(1, len(valid) // 1_000_000)]
            quantiles = np.percentile(sampled, [0, 1, 50, 99, 100])
            inventory_rows.append(
                {
                    "date": date,
                    "band": band.upper(),
                    "source_frames": len(by_date[date]),
                    "output": str(output.relative_to(root)),
                    "crs": TARGET_CRS,
                    "resolution_m": TARGET_RESOLUTION,
                    "width": array.shape[1],
                    "height": array.shape[0],
                    "valid_pixels": len(valid),
                    "coverage_fraction": round(len(valid) / array.size, 6),
                    "min": round(float(quantiles[0]), 6),
                    "p01": round(float(quantiles[1]), 6),
                    "median": round(float(quantiles[2]), 6),
                    "p99": round(float(quantiles[3]), 6),
                    "max": round(float(quantiles[4]), 6),
                }
            )
            print({"date": date, "band": band, "output": str(output), "shape": array.shape})

    inventory_path.parent.mkdir(parents=True, exist_ok=True)
    with inventory_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(inventory_rows[0]))
        writer.writeheader()
        writer.writerows(inventory_rows)
    print({"inventory": str(inventory_path), "rows": len(inventory_rows)})


if __name__ == "__main__":
    main()
