#!/usr/bin/env python3
"""Acquire and validate public population inputs for the Nepal event analysis."""

from __future__ import annotations

import argparse
import csv
import hashlib
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import rasterio


WORLDPOP_URL = (
    "https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024A/2024/"
    "NPL/v1/100m/constrained/npl_pop_2024_CN_100m_R2024A_v1.tif"
)
CENSUS_URL = (
    "https://censusresults.nsonepal.gov.np/files/longform-dataset/"
    "Indv05_SizeOfLocalities.csv"
)
WORLDPOP_RELATIVE = Path(
    "data/raw/geospatial/population/worldpop_2024_constrained_100m/"
    "npl_pop_2024_CN_100m_R2024A_v1.tif"
)
CENSUS_RELATIVE = Path(
    "data/raw/geospatial/population/census_2021/Indv05_SizeOfLocalities.csv"
)
INVENTORY_RELATIVE = Path(
    "data/exp/data-briefing/tables/population_acquisition_inventory.csv"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.stat().st_size > 0:
        print({"status": "already_present", "path": str(destination)})
        return
    partial = destination.with_suffix(destination.suffix + ".part")
    offset = partial.stat().st_size if partial.exists() else 0
    headers = {"User-Agent": "KE03-population-acquisition/1.0"}
    if offset:
        headers["Range"] = f"bytes={offset}-"
    request = urllib.request.Request(
        url, headers=headers
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            if offset and response.status != 206:
                offset = 0
            expected_remaining = response.headers.get("Content-Length")
            mode = "ab" if offset else "wb"
            received = offset
            next_report = received + 4 * 1024 * 1024
            print(
                {
                    "status": "resuming" if offset else "downloading",
                    "path": str(destination),
                    "existing_bytes": offset,
                },
                flush=True,
            )
            with partial.open(mode) as handle:
                while block := response.read(1024 * 1024):
                    handle.write(block)
                    received += len(block)
                    if received >= next_report:
                        print({"path": str(destination), "bytes": received}, flush=True)
                        next_report = received + 4 * 1024 * 1024
        if (
            expected_remaining is not None
            and partial.stat().st_size != offset + int(expected_remaining)
        ):
            raise RuntimeError(
                f"Incomplete download for {url}: expected "
                f"{offset + int(expected_remaining)}, "
                f"received {partial.stat().st_size}"
            )
        partial.replace(destination)
    finally:
        if partial.exists():
            partial.unlink()


def write_source_notes(
    directory: Path,
    *,
    title: str,
    publisher: str,
    product: str,
    source_url: str,
    local_file: Path,
    digest: str,
    validation: list[str],
) -> None:
    downloaded = datetime.now(timezone.utc).date().isoformat()
    lines = [
        f"# {title}",
        "",
        f"- Publisher: {publisher}",
        f"- Product: {product}",
        f"- Source: {source_url}",
        f"- Downloaded: {downloaded}",
        f"- Local file: `{local_file.name}`",
        f"- SHA-256: `{digest}`",
        "",
        "## Validation",
        "",
        *[f"- {item}" for item in validation],
        "",
    ]
    (directory / "SOURCE.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    worldpop = root / WORLDPOP_RELATIVE
    census = root / CENSUS_RELATIVE

    download(WORLDPOP_URL, worldpop)
    download(CENSUS_URL, census)

    with rasterio.open(worldpop) as source:
        raster_metadata = {
            "driver": source.driver,
            "crs": str(source.crs),
            "width": source.width,
            "height": source.height,
            "band_count": source.count,
            "dtype": source.dtypes[0],
            "nodata": source.nodata,
            "bounds": ",".join(f"{value:.6f}" for value in source.bounds),
        }
    if raster_metadata["driver"] != "GTiff" or raster_metadata["band_count"] != 1:
        raise RuntimeError(f"Unexpected WorldPop raster structure: {raster_metadata}")

    census_frame = pd.read_csv(census)
    if census_frame.empty or len(census_frame.columns) < 2:
        raise RuntimeError("The census CSV has no usable tabular content")

    worldpop_hash = sha256(worldpop)
    census_hash = sha256(census)
    write_source_notes(
        worldpop.parent,
        title="WorldPop Nepal constrained population raster",
        publisher="WorldPop Research Programme, University of Southampton",
        product="R2024A 2024 constrained population count, 100 m",
        source_url=WORLDPOP_URL,
        local_file=worldpop,
        digest=worldpop_hash,
        validation=[
            f"Readable {raster_metadata['driver']} with one {raster_metadata['dtype']} band.",
            f"CRS: {raster_metadata['crs']}.",
            f"Dimensions: {raster_metadata['width']} x {raster_metadata['height']} pixels.",
            f"Bounds: {raster_metadata['bounds']}.",
            "This is a modeled 2024 pre-event population surface and must be calibrated "
            "against official 2021 census counts before exposure analysis.",
        ],
    )
    write_source_notes(
        census.parent,
        title="Nepal National Population and Housing Census 2021 table",
        publisher="National Statistics Office Nepal",
        product="Individual long-form dataset table 05: size of localities",
        source_url=CENSUS_URL,
        local_file=census,
        digest=census_hash,
        validation=[
            f"Readable CSV with {len(census_frame):,} rows and "
            f"{len(census_frame.columns):,} columns.",
            "Column names: " + ", ".join(map(str, census_frame.columns)),
            "Administrative identifiers and aggregation level will be audited before calibration.",
        ],
    )

    inventory_path = root / INVENTORY_RELATIVE
    inventory_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {
            "dataset": "WorldPop constrained population",
            "reference_year": 2024,
            "publisher": "WorldPop Research Programme",
            "local_path": str(WORLDPOP_RELATIVE),
            "bytes": worldpop.stat().st_size,
            "sha256": worldpop_hash,
            "status": "acquired_and_validated",
        },
        {
            "dataset": "Nepal Population and Housing Census",
            "reference_year": 2021,
            "publisher": "National Statistics Office Nepal",
            "local_path": str(CENSUS_RELATIVE),
            "bytes": census.stat().st_size,
            "sha256": census_hash,
            "status": "acquired_and_validated",
        },
    ]
    with inventory_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print({"worldpop": raster_metadata, "sha256": worldpop_hash})
    print(
        {
            "census_rows": len(census_frame),
            "census_columns": list(census_frame.columns),
            "sha256": census_hash,
        }
    )
    print({"inventory": str(inventory_path)})


if __name__ == "__main__":
    main()
