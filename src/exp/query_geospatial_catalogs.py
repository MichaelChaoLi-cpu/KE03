#!/usr/bin/env python3
"""Inventory event-window Sentinel scenes from the Copernicus STAC catalogue."""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


STAC_SEARCH = "https://stac.dataspace.copernicus.eu/v1/search"
DEFAULT_BBOX = "84.5,27.55,85.95,28.60"
DEFAULT_START = "2026-08-01T00:00:00Z"
DEFAULT_END = "2026-08-31T23:59:59Z"
EVENT_TIME = datetime(2026, 8, 26, tzinfo=timezone.utc)


def fetch_collection(collection: str, bbox: str, start: str, end: str) -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "collections": collection,
            "bbox": bbox,
            "datetime": f"{start}/{end}",
            "limit": 100,
        }
    )
    request = urllib.request.Request(
        f"{STAC_SEARCH}?{params}",
        headers={"User-Agent": "KE03-geospatial-catalog-inventory/1.0"},
    )
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.load(response)
            return payload.get("features", [])
        except Exception as exc:  # catalog failures should be visible after retries
            last_error = exc
            if attempt < 2:
                time.sleep(2**attempt)
    raise RuntimeError(f"STAC query failed for {collection}: {last_error}")


def parse_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def scene_row(feature: dict) -> dict[str, object]:
    properties = feature.get("properties", {})
    acquired = properties.get("datetime") or properties.get("start_datetime")
    collection = feature.get("collection", "")
    is_pre_event = parse_datetime(acquired) < EVENT_TIME if acquired else ""
    return {
        "collection": collection,
        "scene_id": feature.get("id", ""),
        "acquired_utc": acquired or "",
        "event_period": "pre" if is_pre_event is True else "post" if is_pre_event is False else "",
        "relative_orbit": properties.get("sat:relative_orbit", ""),
        "orbit_state": properties.get("sat:orbit_state", ""),
        "polarizations": "+".join(properties.get("sar:polarizations", [])),
        "cloud_cover_percent": properties.get("eo:cloud_cover", ""),
        "grid_code": properties.get("grid:code", ""),
        "catalog_item_url": next(
            (link.get("href", "") for link in feature.get("links", []) if link.get("rel") == "self"),
            "",
        ),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "collection",
        "scene_id",
        "acquired_utc",
        "event_period",
        "relative_orbit",
        "orbit_state",
        "polarizations",
        "cloud_cover_percent",
        "grid_code",
        "catalog_item_url",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--bbox", default=DEFAULT_BBOX)
    parser.add_argument("--start", default=DEFAULT_START)
    parser.add_argument("--end", default=DEFAULT_END)
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    for collection in ("sentinel-1-grd", "sentinel-2-l2a"):
        rows.extend(
            scene_row(feature)
            for feature in fetch_collection(collection, args.bbox, args.start, args.end)
        )
    rows.sort(key=lambda row: (str(row["collection"]), str(row["acquired_utc"])))
    output = (
        args.root
        / "data/exp/data-briefing/tables/copernicus_event_window_scene_inventory.csv"
    )
    write_csv(output, rows)
    counts = {
        collection: sum(row["collection"] == collection for row in rows)
        for collection in ("sentinel-1-grd", "sentinel-2-l2a")
    }
    print(json.dumps({"output": str(output), "counts": counts}, indent=2))


if __name__ == "__main__":
    main()
