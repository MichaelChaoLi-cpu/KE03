"""Audit archived hazard-map provenance without changing research inputs.

Extract CEMS image-source DBF records, map-PDF interpretation statements and
activation/STAC metadata. Outputs support reviewer-2/comment-4, not a new
accuracy assessment. Network access is not required by this script.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from datetime import datetime, timezone
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import shutil
import subprocess
from zipfile import ZipFile


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_dbf(data: bytes) -> list[dict[str, str]]:
    """Read fixed-width source-table values and reject malformed records."""
    count = int.from_bytes(data[4:8], "little")
    header = int.from_bytes(data[8:10], "little")
    record_size = int.from_bytes(data[10:12], "little")
    fields = []
    offset = 32
    while offset < header and data[offset] != 13:
        field = data[offset : offset + 32]
        fields.append((field[:11].split(b"\0")[0].decode("ascii"), field[16]))
        offset += 32
    if sum(width for _, width in fields) + 1 != record_size:
        raise ValueError("Invalid DBF record width")
    rows = []
    for index in range(count):
        record = data[header + index * record_size : header + (index + 1) * record_size]
        if len(record) != record_size:
            raise ValueError("Truncated DBF source record")
        if record[:1] == b"*":
            continue
        cursor = 1
        row = {}
        for name, width in fields:
            row[name] = record[cursor : cursor + width].decode("utf-8").strip()
            cursor += width
        rows.append(row)
    return rows


def satellite_items(path: Path) -> list[dict[str, object]]:
    data = json.loads(path.read_text())
    rows = []
    for item in data["items"]:
        properties = item["properties"]
        rows.append({
            "id": item["id"],
            "datetime": properties.get("datetime"),
            "platform": properties.get("platform"),
            "relative_orbit": properties.get("sat:relative_orbit"),
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    output_dir = root / "Rev/docs/evidence"
    snapshot = output_dir / "unosat-catalog-metadata-20261023.json"
    archive_path = root / "data/raw/geospatial/reference/copernicus_emsr927/EMSR927_products.zip"
    activation_path = archive_path.with_name("EMSR927_activation.json")
    builder_path = root / "src/preprocessing/build_copernicus_emsr927_reference.py"
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("pdftotext is required to inspect archived map legends")

    # Parse the literal product inventory; do not import or execute preprocessing.
    tree = ast.parse(builder_path.read_text())
    product_specs = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "PRODUCTS" for target in node.targets
        ):
            product_specs = ast.literal_eval(node.value)
    if product_specs is None:
        raise RuntimeError("Builder PRODUCTS inventory not found")
    activation = json.loads(activation_path.read_text())["results"][0]
    records = []
    with ZipFile(archive_path) as outer:
        if outer.testzip() is not None:
            raise RuntimeError("Corrupt CEMS outer archive")
        name_counts = Counter(outer.namelist())
        for name, number in name_counts.items():
            if number > 1:
                digests = {sha256(outer.read(info)) for info in outer.infolist() if info.filename == name}
                if len(digests) != 1:
                    raise RuntimeError("Duplicate CEMS archive names have differing content")
        for spec in product_specs:
            archive_name = spec["archive"]
            with ZipFile(BytesIO(outer.read(archive_name))) as inner:
                source_name = next(name for name in inner.namelist() if "_source_" in name and name.endswith(".dbf"))
                pdf_name = next(name for name in inner.namelist() if name.endswith(".pdf"))
                source_rows = read_dbf(inner.read(source_name))
                post = [r for r in source_rows if r["eventphase"] == "Post-event"]
                pre = [r for r in source_rows if r["eventphase"] == "Pre-event" and r["src_id"] == "1"]
                result = subprocess.run(
                    [pdftotext, "-raw", "-", "-"], input=inner.read(pdf_name),
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
                )
                text = result.stdout.decode("utf-8")
                method = "The thematic layer has been derived from post-event satellite image by means of visual interpretation."
                normalized = " ".join(text.split())
                if method not in normalized:
                    raise RuntimeError(f"Map lacks the expected interpretation statement: {archive_name}")
                start = normalized.index("Data sources and analysis:")
                end = normalized.index(method, start) + len(method)
                aoi = next(a for a in activation["aois"] if a["number"] == spec["aoi_number"])
                products = [p for p in aoi["products"] if p["monitoringNumber"] == spec["monitoring_update"]]
                if len(products) != 1 or products[0]["version"]["number"] != spec["version"]:
                    raise RuntimeError(f"Activation and archive version disagree: {archive_name}")
                api_images = [{"sensor": i["sensorName"], "datetime": i["acquisitionTime"], "file_name": i["fileName"]} for i in products[0]["images"]]
                dbf_dates = {r["src_date"] for r in post}
                api_dates = {datetime.fromisoformat(i["datetime"]).strftime("%d/%m/%Y") for i in api_images}
                if dbf_dates != api_dates or len(post) != len(api_images):
                    raise RuntimeError(f"Source-table and activation acquisition dates disagree: {archive_name}")
                records.append({
                    **spec,
                    "source_dbf_member": source_name,
                    "pre_event_image_sources": pre,
                    "post_event_image_sources": post,
                    "all_source_rows": source_rows,
                    "activation_images": api_images,
                    "mapping_method": "visual interpretation of post-event satellite imagery",
                    "map_pdf_member": pdf_name,
                    "map_pdf_sha256": sha256(inner.read(pdf_name)),
                    "map_data_source_text": normalized[start:end],
                    "source_dbf_sha256": sha256(inner.read(source_name)),
                    "is_independent_field_truth": False,
                })

    if len(records) != 4 or sum(r["current"] for r in records) != 3:
        raise RuntimeError("Expected four archived versions and three selected current products")
    s1_path = root / "data/raw/geospatial/satellite/sentinel1_rtc/metadata/sentinel1_rtc_selected_items.json"
    s2_path = root / "data/raw/geospatial/satellite/sentinel2_l2a/metadata/sentinel2_l2a_selected_items.json"
    manifest_paths = [archive_path, activation_path, builder_path, s1_path, s2_path, snapshot]
    checks = {
        "outer_archive_integrity": "pass",
        "duplicate_product_content": "identical",
        "archive_versions_match_activation": "pass",
        "post_event_dates_match_source_dbf_and_activation": "pass",
        "all_archived_map_pdfs_declare_visual_interpretation": "pass",
        "current_product_count": 3,
        "archive_product_count": 4,
    }
    audit = {
        "schema": "ke03-hazard-provenance-audit/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "reviewer_comment": "reviewer-2/comment-4",
        "status": "pass",
        "checks": checks,
        "input_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()) for p in manifest_paths},
        "unosat_catalog": json.loads(snapshot.read_text()),
        "cems_products": records,
        "study_sentinel1_items": satellite_items(s1_path),
        "study_sentinel2_items": satellite_items(s2_path),
        "inference_limits": [
            "UNOSAT and study optical evidence share Sentinel-2 acquisition date and study region; exact scene/tile identity is unverified.",
            "CEMS current products document different post-event sensors from the study Sentinel inputs; this does not establish independent ground truth.",
            "CEMS and the routing graph both use mapped OSM baseline information.",
            "Reference products enter the consensus classifier; agreement with those same products is not a held-out accuracy test.",
            "The UNOSAT catalog supplies delineation provenance but no fully specified pixel-level classification procedure.",
            "AOI03 PRODUCT v1 is archived but superseded by MONIT01 v1 in processed inputs.",
            "The ESRI pre-image resolution differs between DBF (0.6) and map PDF (1.1 m); retain both records and do not silently choose a value.",
        ],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / "reviewer-2-comment-4-provenance-audit.json"
    output.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": audit["status"], "checks": checks, "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
