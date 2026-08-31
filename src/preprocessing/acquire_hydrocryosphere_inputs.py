#!/usr/bin/env python3
"""Acquire and validate HydroRIVERS Asia and RGI 7 South Asia East archives."""

from __future__ import annotations

import argparse
import csv
import hashlib
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path


SOURCES = (
    {
        "dataset": "HydroRIVERS Asia",
        "version": "1.0",
        "publisher": "HydroSHEDS",
        "url": "https://data.hydrosheds.org/file/HydroRIVERS/HydroRIVERS_v10_as_shp.zip",
        "relative": Path(
            "data/raw/geospatial/hydrography/hydrorivers_v10_asia/"
            "HydroRIVERS_v10_as_shp.zip"
        ),
        "expected_sha1": "71a92a2defcee8cf8294544a7dfc93c2c1281c3c",
        "interpretation": (
            "Regional reference river network; cross-check against DEM-derived flow "
            "paths and do not treat reach attributes as event observations."
        ),
    },
    {
        "dataset": "Randolph Glacier Inventory South Asia East",
        "version": "7.0",
        "publisher": "RGI Consortium / NSIDC, distributed by UNESCO IHP-WINS",
        "url": (
            "https://data.dev-wins.com/dataset/33a5017a-e6e9-43cc-82d6-62da7fbb74d8/"
            "resource/070f3115-9792-4173-926c-600af1cf97f6/download/"
            "rgi2000-v7.0-g-15_south_asia_east.zip"
        ),
        "relative": Path(
            "data/raw/geospatial/cryosphere/rgi7_south_asia_east/"
            "rgi2000-v7.0-g-15_south_asia_east.zip"
        ),
        "expected_sha1": None,
        "interpretation": (
            "Approximate year-2000 glacier inventory for source-area context only; "
            "not evidence of the 2026 trigger or current glacier extent."
        ),
    },
)
INVENTORY_RELATIVE = Path(
    "data/exp/data-briefing/tables/hydrocryosphere_acquisition_inventory.csv"
)


def digest(path: Path, algorithm: str) -> str:
    checksum = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            checksum.update(block)
    return checksum.hexdigest()


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.stat().st_size > 0:
        print({"status": "already_present", "path": str(destination)}, flush=True)
        return
    partial = destination.with_suffix(destination.suffix + ".part")
    offset = partial.stat().st_size if partial.exists() else 0
    headers = {"User-Agent": "KE03-hydrocryosphere-acquisition/1.0"}
    if offset:
        headers["Range"] = f"bytes={offset}-"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            if offset and response.status != 206:
                offset = 0
            expected_remaining = response.headers.get("Content-Length")
            mode = "ab" if offset else "wb"
            received = offset
            next_report = received + 8 * 1024 * 1024
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
                        next_report = received + 8 * 1024 * 1024
        if (
            expected_remaining is not None
            and partial.stat().st_size != offset + int(expected_remaining)
        ):
            raise RuntimeError(
                f"Incomplete download for {url}: expected "
                f"{offset + int(expected_remaining)}, got {partial.stat().st_size}"
            )
        partial.replace(destination)
    finally:
        if partial.exists() and destination.exists():
            partial.unlink()


def validate_zip(path: Path) -> tuple[int, list[str]]:
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"Corrupt member in {path}: {bad}")
        names = [name for name in archive.namelist() if not name.endswith("/")]
    if not any(name.casefold().endswith(".shp") for name in names):
        raise RuntimeError(f"No shapefile found in {path}")
    return len(names), names


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    inventory_rows: list[dict[str, object]] = []
    downloaded = datetime.now(timezone.utc).date().isoformat()

    for source in SOURCES:
        path = root / source["relative"]
        download(str(source["url"]), path)
        member_count, members = validate_zip(path)
        sha1 = digest(path, "sha1")
        sha256 = digest(path, "sha256")
        expected_sha1 = source["expected_sha1"]
        if expected_sha1 is not None and sha1 != expected_sha1:
            raise RuntimeError(
                f"SHA-1 mismatch for {path}: expected {expected_sha1}, got {sha1}"
            )
        shapefiles = [name for name in members if name.casefold().endswith(".shp")]
        source_lines = [
            f"# {source['dataset']}",
            "",
            f"- Publisher: {source['publisher']}",
            f"- Version: {source['version']}",
            f"- Source: {source['url']}",
            f"- Downloaded: {downloaded}",
            f"- Local file: `{path.name}`",
            f"- Bytes: {path.stat().st_size:,}",
            f"- SHA-1: `{sha1}`",
            f"- SHA-256: `{sha256}`",
            f"- ZIP members: {member_count}",
            f"- Shapefiles: {', '.join(shapefiles)}",
            "",
            "## Interpretation boundary",
            "",
            str(source["interpretation"]),
            "",
        ]
        (path.parent / "SOURCE.md").write_text(
            "\n".join(source_lines), encoding="utf-8"
        )
        inventory_rows.append(
            {
                "dataset": source["dataset"],
                "version": source["version"],
                "publisher": source["publisher"],
                "local_path": source["relative"],
                "bytes": path.stat().st_size,
                "sha256": sha256,
                "zip_members": member_count,
                "status": "acquired_and_validated",
            }
        )
        print(
            {
                "dataset": source["dataset"],
                "bytes": path.stat().st_size,
                "members": member_count,
                "shapefiles": shapefiles,
                "sha256": sha256,
            },
            flush=True,
        )

    inventory = root / INVENTORY_RELATIVE
    inventory.parent.mkdir(parents=True, exist_ok=True)
    with inventory.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(inventory_rows[0]))
        writer.writeheader()
        writer.writerows(inventory_rows)
    print({"inventory": str(inventory)}, flush=True)


if __name__ == "__main__":
    main()
