#!/usr/bin/env python3
"""Acquire the public Copernicus EMSR927 activation metadata and product bundle."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import urllib.request
import zipfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path


ACTIVATION_API = (
    "https://rapidmapping.emergency.copernicus.eu/backend/dashboard-api/"
    "public-activations/?code=EMSR927"
)
OUTPUT_DIR_RELATIVE = Path(
    "data/raw/geospatial/reference/copernicus_emsr927"
)
ARCHIVE_NAME = "EMSR927_products.zip"
METADATA_NAME = "EMSR927_activation.json"
INVENTORY_RELATIVE = Path(
    "data/exp/data-briefing/tables/copernicus_emsr927_acquisition_inventory.csv"
)


def read_json(url: str) -> dict:
    request = urllib.request.Request(
        url, headers={"User-Agent": "KE03-copernicus-emsr927-acquisition/1.0"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.stat().st_size > 0:
        print({"status": "already_present", "path": str(destination)}, flush=True)
        return
    partial = destination.with_suffix(destination.suffix + ".part")
    offset = partial.stat().st_size if partial.exists() else 0
    headers = {"User-Agent": "KE03-copernicus-emsr927-acquisition/1.0"}
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
                f"Incomplete download: expected {offset + int(expected_remaining)}, "
                f"got {partial.stat().st_size}"
            )
        partial.replace(destination)
    finally:
        if partial.exists() and destination.exists():
            partial.unlink()


def sha256(path: Path) -> str:
    checksum = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            checksum.update(block)
    return checksum.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    output_dir = root / OUTPUT_DIR_RELATIVE
    output_dir.mkdir(parents=True, exist_ok=True)

    response = read_json(ACTIVATION_API)
    if response.get("count") != 1:
        raise RuntimeError(f"Expected one EMSR927 activation, got {response.get('count')}")
    activation = response["results"][0]
    if activation.get("code") != "EMSR927":
        raise RuntimeError(f"Unexpected activation: {activation.get('code')}")
    products_path = activation.get("productsPath")
    if not products_path:
        raise RuntimeError("EMSR927 has no published product bundle")

    metadata_path = output_dir / METADATA_NAME
    metadata_path.write_text(json.dumps(response, indent=2), encoding="utf-8")
    archive_path = output_dir / ARCHIVE_NAME
    download(str(products_path), archive_path)

    with zipfile.ZipFile(archive_path) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"Corrupt archive member: {bad}")
        member_infos = [info for info in archive.infolist() if not info.is_dir()]
        members = [info.filename for info in member_infos]
        shapefiles = [name for name in members if name.casefold().endswith(".shp")]
        nested_archives = [
            info for info in member_infos if info.filename.casefold().endswith(".zip")
        ]
        seen_nested: set[tuple[str, int]] = set()
        nested_duplicates = 0
        for info in nested_archives:
            identity = (info.filename, info.CRC)
            if identity in seen_nested:
                nested_duplicates += 1
                continue
            seen_nested.add(identity)
            with zipfile.ZipFile(BytesIO(archive.read(info))) as nested:
                nested_bad = nested.testzip()
                if nested_bad is not None:
                    raise RuntimeError(
                        f"Corrupt member {nested_bad} in nested archive {info.filename}"
                    )
                shapefiles.extend(
                    f"{info.filename}!{name}"
                    for name in nested.namelist()
                    if name.casefold().endswith(".shp")
                )
    if not shapefiles:
        raise RuntimeError("No shapefiles found in EMSR927 product bundle")

    digest = sha256(archive_path)
    downloaded = datetime.now(timezone.utc).date().isoformat()
    ready_products = []
    inventory_rows: list[dict[str, object]] = []
    for aoi in activation.get("aois", []):
        for product in aoi.get("products", []):
            version = product.get("version") or {}
            ready = bool(product.get("downloadPath")) and version.get("statusCode") == "F"
            if ready:
                ready_products.append(product)
            inventory_rows.append(
                {
                    "activation": "EMSR927",
                    "aoi_number": aoi.get("number"),
                    "aoi_name": aoi.get("name"),
                    "product_type": product.get("type"),
                    "monitoring": product.get("monitoring"),
                    "monitoring_number": product.get("monitoringNumber"),
                    "version": version.get("number"),
                    "delivery_time": version.get("deliveryTime"),
                    "status_code": version.get("statusCode"),
                    "ready_for_download": ready,
                    "source_images": len(product.get("images") or []),
                    "archive_path": str(OUTPUT_DIR_RELATIVE / ARCHIVE_NAME),
                }
            )

    source_lines = [
        "# Copernicus Emergency Management Service activation EMSR927",
        "",
        "- Activation: Flood in Nepal (EMSR927)",
        "- Producer: European Union Copernicus Emergency Management Service Rapid Mapping",
        f"- Activation API: {ACTIVATION_API}",
        f"- Product bundle endpoint: {products_path}",
        f"- Downloaded: {downloaded}",
        f"- Local file: `{ARCHIVE_NAME}`",
        f"- Bytes: {archive_path.stat().st_size:,}",
        f"- SHA-256: `{digest}`",
        f"- ZIP members: {len(members)}",
        f"- Unique nested product archives: {len(seen_nested)}",
        f"- Duplicate nested archive entries: {nested_duplicates}",
        f"- Shapefiles: {len(shapefiles)}",
        f"- AOIs in activation metadata: {len(activation.get('aois', []))}",
        f"- Final-status products included at acquisition: {len(ready_products)}",
        "",
        "## Interpretation boundary",
        "",
        "These are rapid, satellite-image-based emergency mapping products. Damage grades are stronger validation evidence than geometry-only intersections, but they are not a substitute for field inspection. The activation was still open when acquired, so later product versions may supersede this bundle.",
        "",
    ]
    (output_dir / "SOURCE.md").write_text("\n".join(source_lines), encoding="utf-8")

    inventory = root / INVENTORY_RELATIVE
    inventory.parent.mkdir(parents=True, exist_ok=True)
    with inventory.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(inventory_rows[0]))
        writer.writeheader()
        writer.writerows(inventory_rows)

    print(
        {
            "archive": str(archive_path),
            "bytes": archive_path.stat().st_size,
            "sha256": digest,
            "members": len(members),
            "unique_nested_archives": len(seen_nested),
            "duplicate_nested_entries": nested_duplicates,
            "shapefiles": len(shapefiles),
            "ready_products": len(ready_products),
            "inventory": str(inventory),
        }
    )


if __name__ == "__main__":
    main()
