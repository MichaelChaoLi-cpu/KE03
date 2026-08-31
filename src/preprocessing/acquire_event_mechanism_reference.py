#!/usr/bin/env python3
"""Acquire and checksum the Hi-RISK rapid hazard assessment for the 2026 event."""

from __future__ import annotations

import argparse
import hashlib
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


REPORT_URL = "https://hirisk.org/wp-content/uploads/2026/08/RHA_NP3_RasuwaFlood-1.pdf"
LANDING_URL = "https://hirisk.org/"
REPORT_RELATIVE = Path(
    "data/raw/geospatial/reference/hirisk_2026_rasuwa/"
    "RHA_NP3_RasuwaFlood-1.pdf"
)


def sha256(path: Path) -> str:
    checksum = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            checksum.update(block)
    return checksum.hexdigest()


def download(destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.stat().st_size > 0:
        return
    partial = destination.with_suffix(".pdf.part")
    request = urllib.request.Request(
        REPORT_URL,
        headers={"User-Agent": "KE03-event-reference-acquisition/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            content_type = response.headers.get("Content-Type", "")
            if "pdf" not in content_type.casefold():
                raise RuntimeError(f"Unexpected content type: {content_type}")
            with partial.open("wb") as handle:
                while block := response.read(1024 * 1024):
                    handle.write(block)
        if partial.stat().st_size < 10_000:
            raise RuntimeError("Downloaded report is unexpectedly small")
        partial.replace(destination)
    finally:
        if partial.exists() and destination.exists():
            partial.unlink()


def validate_pdf(path: Path) -> None:
    with path.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise RuntimeError(f"Not a PDF: {path}")
        handle.seek(-32, 2)
        if b"%%EOF" not in handle.read():
            raise RuntimeError(f"PDF has no EOF marker: {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    path = root / REPORT_RELATIVE
    download(path)
    validate_pdf(path)
    checksum = sha256(path)
    downloaded = datetime.now(timezone.utc).date().isoformat()
    source = path.parent / "SOURCE.md"
    source.write_text(
        "\n".join(
            [
                "# Hi-RISK rapid hazard assessment: Rasuwa flood",
                "",
                "- Publisher: Hi-RISK",
                "- Report date: 2026-08-28",
                f"- Report: {REPORT_URL}",
                f"- Landing page: {LANDING_URL}",
                f"- Downloaded: {downloaded}",
                f"- Local file: `{path.name}`",
                f"- Bytes: {path.stat().st_size:,}",
                f"- SHA-256: `{checksum}`",
                "",
                "## Interpretation boundary",
                "",
                "This is a rapid remote-sensing hazard assessment, not field validation. "
                "Its mapped source location and proposed event sequence may be used for "
                "triangulation, but not as definitive event-specific climate attribution.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(
        {
            "status": "acquired_and_validated",
            "path": str(path),
            "bytes": path.stat().st_size,
            "sha256": checksum,
        }
    )


if __name__ == "__main__":
    main()
