#!/usr/bin/env python3
"""Stream event-corridor Sentinel-2 L2A bands and scene classifications."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import urllib.parse
import urllib.request
from contextlib import ExitStack
from datetime import datetime, timezone
from pathlib import Path

import geopandas as gpd
import numpy as np

# Keep rasterio aligned with the PROJ database shipped in its wheel.
RASTERIO_SPEC = importlib.util.find_spec("rasterio")
if RASTERIO_SPEC is None or not RASTERIO_SPEC.submodule_search_locations:
    raise RuntimeError("rasterio is not installed in the active environment")
PROJ_DATA_DIR = Path(next(iter(RASTERIO_SPEC.submodule_search_locations))) / "proj_data"
os.environ["PROJ_DATA"] = str(PROJ_DATA_DIR)
os.environ["PROJ_LIB"] = str(PROJ_DATA_DIR)

import rasterio
from rasterio.enums import Resampling
from rasterio.merge import merge


STAC_API = "https://planetarycomputer.microsoft.com/api/stac/v1"
TOKEN_API = "https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel-2-l2a"
COLLECTION = "sentinel-2-l2a"
REFERENCE_RELATIVE = Path(
    "data/processed/geospatial/reference/unosat_event_reference.gpkg"
)
METADATA_RELATIVE = Path(
    "data/raw/geospatial/satellite/sentinel2_l2a/metadata/"
    "sentinel2_l2a_selected_items.json"
)
SOURCE_NOTE_RELATIVE = Path(
    "data/raw/geospatial/satellite/sentinel2_l2a/SOURCE.md"
)
INVENTORY_RELATIVE = Path(
    "data/exp/data-briefing/tables/sentinel2_l2a_acquisition_inventory.csv"
)
OUTPUT_DIR_RELATIVE = Path("data/processed/geospatial/satellite")
TARGET_CRS = "EPSG:32645"
TARGET_RESOLUTION = 20
REFERENCE_BUFFER_M = 2_000
TARGET_DATES = ("2026-08-12", "2026-08-27")
TARGET_ORBIT = 119
TARGET_TILES = {"45RUM", "45RUL", "45RTM", "45RTL"}
REFLECTANCE_BANDS = ("B02", "B03", "B04", "B08", "B11")
SCL_BAND = "SCL"
INVALID_SCL_CLASSES = {0, 1, 3, 8, 9, 10, 11}


def read_json(url: str) -> dict:
    request = urllib.request.Request(
        url, headers={"User-Agent": "KE03-sentinel2-l2a-acquisition/1.0"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


def search_items(search_bbox: tuple[float, float, float, float]) -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "collections": COLLECTION,
            "bbox": ",".join(map(str, search_bbox)),
            "datetime": "2026-08-12T00:00:00Z/2026-08-27T23:59:59Z",
            "limit": 100,
        }
    )
    features = read_json(f"{STAC_API}/search?{params}").get("features", [])
    selected = []
    required_assets = set(REFLECTANCE_BANDS) | {SCL_BAND}
    for feature in features:
        properties = feature.get("properties", {})
        acquired = str(properties.get("datetime", ""))
        if not any(acquired.startswith(date) for date in TARGET_DATES):
            continue
        if properties.get("sat:relative_orbit") != TARGET_ORBIT:
            continue
        if properties.get("s2:mgrs_tile") not in TARGET_TILES:
            continue
        if not required_assets.issubset(feature.get("assets", {})):
            continue
        selected.append(feature)
    return sorted(selected, key=lambda item: item["id"])


def signed_href(item: dict, band: str, token: str) -> str:
    href = item["assets"][band]["href"]
    separator = "&" if "?" in href else "?"
    return f"{href}{separator}{token}"


def write_raster(
    path: Path,
    array: np.ndarray,
    transform,
    *,
    dtype: str,
    nodata: int,
    resampling: Resampling,
    tags: dict[str, str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    profile = {
        "driver": "GTiff",
        "height": array.shape[0],
        "width": array.shape[1],
        "count": 1,
        "dtype": dtype,
        "crs": TARGET_CRS,
        "transform": transform,
        "nodata": nodata,
        "compress": "DEFLATE",
        "predictor": 2 if dtype != "uint8" else 1,
        "tiled": True,
        "blockxsize": 512,
        "blockysize": 512,
        "BIGTIFF": "IF_SAFER",
    }
    with rasterio.open(path, "w", **profile) as destination:
        destination.write(array.astype(dtype), 1)
        destination.update_tags(**tags)
        destination.build_overviews([2, 4, 8, 16], resampling)
        destination.update_tags(ns="rio_overview", resampling=resampling.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    reference_path = root / REFERENCE_RELATIVE
    if not reference_path.exists():
        raise FileNotFoundError(reference_path)

    reference = gpd.read_file(reference_path, layer="analysis_extent")
    reference_metric = reference.to_crs(TARGET_CRS)
    target_geometry = reference_metric.geometry.union_all().buffer(REFERENCE_BUFFER_M)
    target_bounds = tuple(target_geometry.bounds)
    search_bbox = tuple(
        gpd.GeoSeries([target_geometry], crs=TARGET_CRS)
        .to_crs("EPSG:4326")
        .total_bounds
    )

    items = search_items(search_bbox)
    by_date = {
        date: [
            item
            for item in items
            if str(item["properties"]["datetime"]).startswith(date)
        ]
        for date in TARGET_DATES
    }
    for date, date_items in by_date.items():
        tiles = {item["properties"]["s2:mgrs_tile"] for item in date_items}
        if tiles != TARGET_TILES:
            raise RuntimeError(
                f"Expected {sorted(TARGET_TILES)} for {date}, got {sorted(tiles)}"
            )

    metadata = {
        "collection": COLLECTION,
        "search_bbox_wgs84": search_bbox,
        "target_bounds_utm45n": target_bounds,
        "target_crs": TARGET_CRS,
        "target_resolution_m": TARGET_RESOLUTION,
        "reference_buffer_m": REFERENCE_BUFFER_M,
        "relative_orbit": TARGET_ORBIT,
        "dates": TARGET_DATES,
        "bands": (*REFLECTANCE_BANDS, SCL_BAND),
        "items": items,
        "note": "Unsigned STAC metadata only; temporary SAS tokens are never saved.",
    }
    metadata_path = root / METADATA_RELATIVE
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    token = read_json(TOKEN_API)["token"]
    gdal_options = {
        "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",
        "CPL_VSIL_CURL_ALLOWED_EXTENSIONS": ".tif,.tiff",
        "GDAL_HTTP_MULTIRANGE": "YES",
        "VSI_CACHE": "TRUE",
        "VSI_CACHE_SIZE": 50_000_000,
    }
    output_dir = root / OUTPUT_DIR_RELATIVE
    inventory_rows: list[dict[str, object]] = []

    for date in TARGET_DATES:
        date_items = by_date[date]
        transforms = []
        for band in (*REFLECTANCE_BANDS, SCL_BAND):
            is_scl = band == SCL_BAND
            with rasterio.Env(**gdal_options), ExitStack() as stack:
                sources = [
                    stack.enter_context(
                        rasterio.open(signed_href(item, band, token))
                    )
                    for item in date_items
                ]
                mosaic, transform = merge(
                    sources,
                    bounds=target_bounds,
                    res=TARGET_RESOLUTION,
                    nodata=0,
                    dtype="uint8" if is_scl else "uint16",
                    resampling=Resampling.nearest if is_scl else Resampling.bilinear,
                    method="first",
                    target_aligned_pixels=True,
                )
            array = mosaic[0]
            transforms.append(transform)
            output = output_dir / f"sentinel2_l2a_{date}_{band.lower()}_20m.tif"
            tags = {
                "collection": COLLECTION,
                "acquisition_date": date,
                "band": band,
                "relative_orbit": str(TARGET_ORBIT),
                "source_item_ids": ",".join(item["id"] for item in date_items),
                "processing_baseline": ",".join(
                    sorted(
                        {
                            str(item["properties"].get("s2:processing_baseline", ""))
                            for item in date_items
                        }
                    )
                ),
                "interpretation": (
                    "scene classification code"
                    if is_scl
                    else "Sentinel-2 L2A bottom-of-atmosphere reflectance digital number"
                ),
            }
            write_raster(
                output,
                array,
                transform,
                dtype="uint8" if is_scl else "uint16",
                nodata=0,
                resampling=Resampling.nearest if is_scl else Resampling.average,
                tags=tags,
            )
            print(
                {
                    "date": date,
                    "band": band,
                    "output": str(output),
                    "shape": array.shape,
                },
                flush=True,
            )
            if is_scl:
                scl = array

        if len(set(transforms)) != 1:
            raise RuntimeError(f"Band grids are not aligned for {date}")
        valid = np.isin(scl, list(set(range(1, 12)) - INVALID_SCL_CLASSES))
        valid_output = output_dir / f"sentinel2_l2a_{date}_valid_mask_20m.tif"
        write_raster(
            valid_output,
            valid.astype("uint8"),
            transforms[0],
            dtype="uint8",
            nodata=255,
            resampling=Resampling.nearest,
            tags={
                "collection": COLLECTION,
                "acquisition_date": date,
                "variable": "valid optical observation mask",
                "valid_value": "1",
                "invalid_value": "0",
                "excluded_scl_classes": ",".join(map(str, sorted(INVALID_SCL_CLASSES))),
            },
        )
        classified = scl > 0
        class_counts = {code: int((scl == code).sum()) for code in range(1, 12)}
        inventory_rows.append(
            {
                "date": date,
                "source_items": len(date_items),
                "mgrs_tiles": ";".join(
                    sorted(item["properties"]["s2:mgrs_tile"] for item in date_items)
                ),
                "catalog_cloud_min_percent": min(
                    float(item["properties"]["eo:cloud_cover"]) for item in date_items
                ),
                "catalog_cloud_max_percent": max(
                    float(item["properties"]["eo:cloud_cover"]) for item in date_items
                ),
                "classified_pixels": int(classified.sum()),
                "valid_optical_pixels": int(valid.sum()),
                "valid_optical_fraction": (
                    float(valid.sum() / classified.sum()) if classified.any() else 0.0
                ),
                "cloud_shadow_pixels_scl3": class_counts[3],
                "cloud_pixels_scl8_9_10": (
                    class_counts[8] + class_counts[9] + class_counts[10]
                ),
                "snow_ice_pixels_scl11": class_counts[11],
                "output_grid": f"{scl.shape[1]}x{scl.shape[0]}",
                "status": "acquired_and_processed",
            }
        )

    inventory_path = root / INVENTORY_RELATIVE
    inventory_path.parent.mkdir(parents=True, exist_ok=True)
    with inventory_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(inventory_rows[0]))
        writer.writeheader()
        writer.writerows(inventory_rows)

    source_note = root / SOURCE_NOTE_RELATIVE
    source_note.parent.mkdir(parents=True, exist_ok=True)
    downloaded = datetime.now(timezone.utc).date().isoformat()
    source_note.write_text(
        "\n".join(
            [
                "# Sentinel-2 Level-2A event-corridor subset",
                "",
                "- Producer: European Union Copernicus Sentinel-2 mission",
                "- Distribution: Microsoft Planetary Computer STAC and cloud-optimized GeoTIFF assets",
                f"- Collection: {STAC_API}/collections/{COLLECTION}",
                f"- Downloaded / streamed: {downloaded}",
                f"- Dates: {', '.join(TARGET_DATES)}",
                f"- Relative orbit: {TARGET_ORBIT}",
                f"- MGRS tiles: {', '.join(sorted(TARGET_TILES))}",
                f"- Bands: {', '.join((*REFLECTANCE_BANDS, SCL_BAND))}",
                f"- Output resolution: {TARGET_RESOLUTION} m in {TARGET_CRS}",
                "- Spatial subset: UNOSAT analysis extent plus a 2 km buffer",
                "- Raw-data handling: source COG windows were streamed; unsigned STAC item metadata is retained locally and temporary SAS tokens are not saved.",
                "",
                "## Interpretation boundary",
                "",
                "The post-event acquisition is heavily cloud affected. Optical bands are retained for masked visual and spectral validation only; they do not independently define the hazard footprint.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(inventory_rows)
    print({"inventory": str(inventory_path), "metadata": str(metadata_path)})


if __name__ == "__main__":
    main()
