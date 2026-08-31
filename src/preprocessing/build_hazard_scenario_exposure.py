#!/usr/bin/env python3
"""Build scenario-based population and infrastructure exposure tables."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.enums import Resampling
from rasterio.features import rasterize
from rasterio.transform import rowcol
from rasterio.warp import reproject
from rasterio.windows import Window, from_bounds, transform as window_transform
from shapely.geometry import GeometryCollection, LineString, MultiLineString
from shapely.ops import unary_union


HAZARD = Path(
    "data/processed/geospatial/hazard/hazard_evidence_class_20m.tif"
)
POPULATION = Path(
    "data/processed/geospatial/population/"
    "worldpop_2024_distribution_calibrated_to_2021_census.tif"
)
OSM = Path("data/processed/geospatial/base/osm_pre_event_aoi.gpkg")
UNOSAT = Path(
    "data/processed/geospatial/reference/unosat_event_reference.gpkg"
)
CEMS = Path(
    "data/processed/geospatial/reference/copernicus_emsr927_damage_reference.gpkg"
)
ROAD_DAMAGE_TABLE = Path(
    "data/processed/geospatial/network/road_damage_evidence_crosswalk.parquet"
)
ROAD_DAMAGE_GEOMETRY = Path(
    "data/processed/geospatial/network/road_damage_evidence_crosswalk.gpkg"
)
OUTPUT_DIR = Path("data/processed/geospatial/exposure")
AUDIT = Path(
    "data/exp/data-preprocessing/hazard_scenario_exposure_audit.csv"
)

SCENARIOS = (
    ("Primary conservative", 3),
    ("Alternative mapped or multisensor", 2),
    ("Sensitivity screening", 1),
)
OUTSIDE_ANALYSIS = 255
ROAD_SAMPLE_STEP_M = 20.0
SETTLEMENT_CONTEXT_M = 500.0
FACILITY_CONTEXT_M = 250.0


def clamp_window(window: Window, height: int, width: int) -> Window | None:
    col_start = max(0, int(math.floor(window.col_off)))
    row_start = max(0, int(math.floor(window.row_off)))
    col_end = min(width, int(math.ceil(window.col_off + window.width)))
    row_end = min(height, int(math.ceil(window.row_off + window.height)))
    if col_end <= col_start or row_end <= row_start:
        return None
    return Window(col_start, row_start, col_end - col_start, row_end - row_start)


def max_class_for_geometry(
    classes: np.ndarray,
    transform: rasterio.Affine,
    geometry: object,
) -> int:
    if geometry is None or geometry.is_empty:
        return OUTSIDE_ANALYSIS
    window = clamp_window(
        from_bounds(*geometry.bounds, transform=transform),
        classes.shape[0],
        classes.shape[1],
    )
    if window is None:
        return OUTSIDE_ANALYSIS
    row_start = int(window.row_off)
    col_start = int(window.col_off)
    row_end = row_start + int(window.height)
    col_end = col_start + int(window.width)
    local = classes[row_start:row_end, col_start:col_end]
    mask = rasterize(
        [(geometry, 1)],
        out_shape=local.shape,
        transform=window_transform(window, transform),
        fill=0,
        all_touched=True,
        dtype="uint8",
    ).astype(bool)
    values = local[mask & (local != OUTSIDE_ANALYSIS)]
    return int(values.max()) if values.size else OUTSIDE_ANALYSIS


def class_at_point(
    classes: np.ndarray,
    transform: rasterio.Affine,
    x: float,
    y: float,
) -> int:
    row, col = rowcol(transform, x, y)
    if row < 0 or col < 0 or row >= classes.shape[0] or col >= classes.shape[1]:
        return OUTSIDE_ANALYSIS
    return int(classes[row, col])


def max_class_near_point(
    classes: np.ndarray,
    transform: rasterio.Affine,
    x: float,
    y: float,
    radius_m: float,
) -> int:
    row, col = rowcol(transform, x, y)
    pixel_m = abs(transform.a)
    radius_cells = int(math.ceil(radius_m / pixel_m))
    row_start = max(0, row - radius_cells)
    row_end = min(classes.shape[0], row + radius_cells + 1)
    col_start = max(0, col - radius_cells)
    col_end = min(classes.shape[1], col + radius_cells + 1)
    if row_start >= row_end or col_start >= col_end:
        return OUTSIDE_ANALYSIS
    local = classes[row_start:row_end, col_start:col_end]
    rows = np.arange(row_start, row_end) - row
    cols = np.arange(col_start, col_end) - col
    circle = (
        rows[:, None].astype("float64") ** 2
        + cols[None, :].astype("float64") ** 2
    ) <= (radius_m / pixel_m) ** 2
    values = local[circle & (local != OUTSIDE_ANALYSIS)]
    return int(values.max()) if values.size else OUTSIDE_ANALYSIS


def line_parts(geometry: object) -> list[LineString]:
    if geometry is None or geometry.is_empty:
        return []
    if isinstance(geometry, LineString):
        return [geometry]
    if isinstance(geometry, MultiLineString):
        return list(geometry.geoms)
    if isinstance(geometry, GeometryCollection):
        parts: list[LineString] = []
        for part in geometry.geoms:
            parts.extend(line_parts(part))
        return parts
    return []


def sampled_line_exposure(
    classes: np.ndarray,
    transform: rasterio.Affine,
    geometry: object,
) -> tuple[float, int, dict[int, float]]:
    xs: list[float] = []
    ys: list[float] = []
    weights: list[float] = []
    total_length = 0.0
    for part in line_parts(geometry):
        length = float(part.length)
        if length <= 0:
            continue
        total_length += length
        samples = max(1, int(math.ceil(length / ROAD_SAMPLE_STEP_M)))
        segment_weight = length / samples
        for index in range(samples):
            point = part.interpolate((index + 0.5) * segment_weight)
            xs.append(point.x)
            ys.append(point.y)
            weights.append(segment_weight)
    if not xs:
        return total_length, OUTSIDE_ANALYSIS, {1: 0.0, 2: 0.0, 3: 0.0}
    rows, cols = rowcol(transform, xs, ys)
    rows_array = np.asarray(rows)
    cols_array = np.asarray(cols)
    valid = (
        (rows_array >= 0)
        & (cols_array >= 0)
        & (rows_array < classes.shape[0])
        & (cols_array < classes.shape[1])
    )
    values = np.full(len(xs), OUTSIDE_ANALYSIS, dtype="uint8")
    values[valid] = classes[rows_array[valid], cols_array[valid]]
    weights_array = np.asarray(weights)
    in_scope = values != OUTSIDE_ANALYSIS
    maximum = int(values[in_scope].max()) if in_scope.any() else OUTSIDE_ANALYSIS
    exposed = {
        threshold: float(weights_array[(values >= threshold) & in_scope].sum())
        for threshold in (1, 2, 3)
    }
    return total_length, maximum, exposed


def load_osm_layer(root: Path, layer: str, crs: object, scope: object) -> gpd.GeoDataFrame:
    frame = gpd.read_file(root / OSM, layer=layer).to_crs(crs)
    return frame.loc[
        frame.geometry.notna()
        & frame.geometry.is_valid
        & ~frame.geometry.is_empty
        & frame.geometry.intersects(scope)
    ].copy()


def point_exposure_table(
    frame: gpd.GeoDataFrame,
    classes: np.ndarray,
    transform: rasterio.Affine,
    id_column: str,
    name_column: str,
    context_m: float,
    extra_columns: list[str],
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, source in frame.iterrows():
        point = source.geometry
        record: dict[str, object] = {
            id_column: source[id_column],
            name_column: source.get(name_column),
            "Direct Evidence Class": class_at_point(
                classes, transform, point.x, point.y
            ),
            f"Maximum Evidence Class within {int(context_m)} m": max_class_near_point(
                classes, transform, point.x, point.y, context_m
            ),
        }
        for column in extra_columns:
            record[column] = source.get(column)
        rows.append(record)
    return pd.DataFrame(rows)


def geometry_exposure_table(
    frame: gpd.GeoDataFrame,
    classes: np.ndarray,
    transform: rasterio.Affine,
    id_column: str,
    name_column: str,
    extra_columns: list[str],
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, source in frame.iterrows():
        record: dict[str, object] = {
            id_column: source[id_column],
            name_column: source.get(name_column),
            "Maximum Intersecting Evidence Class": max_class_for_geometry(
                classes, transform, source.geometry
            ),
        }
        for column in extra_columns:
            record[column] = source.get(column)
        rows.append(record)
    return pd.DataFrame(rows)


def normalize_class_columns(frame: pd.DataFrame) -> pd.DataFrame:
    for column in frame.columns:
        if "Evidence Class" in column:
            frame[column] = frame[column].replace(OUTSIDE_ANALYSIS, pd.NA).astype("Int64")
    return frame


def at_least(series: pd.Series, threshold: int) -> pd.Series:
    return series.ge(threshold).fillna(False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    required = [
        root / HAZARD,
        root / POPULATION,
        root / OSM,
        root / UNOSAT,
        root / CEMS,
        root / ROAD_DAMAGE_TABLE,
        root / ROAD_DAMAGE_GEOMETRY,
    ]
    for path in required:
        if not path.exists():
            raise FileNotFoundError(path)

    with rasterio.open(root / HAZARD) as hazard_source:
        classes = hazard_source.read(1)
        transform = hazard_source.transform
        crs = hazard_source.crs
        profile = hazard_source.profile
    if crs is None:
        raise RuntimeError("Hazard evidence raster has no CRS")
    pixel_area_km2 = abs(transform.a * transform.e) / 1_000_000

    unosat_scope = gpd.read_file(root / UNOSAT, layer="analysis_extent").to_crs(crs)
    cems_scope = gpd.read_file(root / CEMS, layer="area_of_interest").to_crs(crs)
    scope = unary_union([unosat_scope.geometry.union_all(), cems_scope.geometry.union_all()])

    population_20m = np.zeros(classes.shape, dtype="float32")
    with rasterio.open(root / POPULATION) as population_source:
        source_population = population_source.read(1)
        source_valid = (
            source_population != population_source.nodata
            if population_source.nodata is not None
            else np.isfinite(source_population)
        )
        calibrated_population_total = float(source_population[source_valid].sum())
        reproject(
            source=source_population,
            destination=population_20m,
            src_transform=population_source.transform,
            src_crs=population_source.crs,
            src_nodata=population_source.nodata,
            dst_transform=transform,
            dst_crs=crs,
            dst_nodata=0,
            resampling=Resampling.sum,
        )
    analysis_scope = classes != OUTSIDE_ANALYSIS
    population_in_analysis_scope = float(population_20m[analysis_scope].sum())

    settlements = load_osm_layer(root, "settlements", crs, scope)
    facilities = load_osm_layer(root, "facilities", crs, scope)
    buildings = load_osm_layer(root, "buildings", crs, scope)
    bridges = load_osm_layer(root, "bridges", crs, scope)
    roads = load_osm_layer(root, "roads", crs, scope)

    settlement_table = point_exposure_table(
        settlements,
        classes,
        transform,
        "osm_id",
        "name",
        SETTLEMENT_CONTEXT_M,
        ["place"],
    ).rename(columns={"osm_id": "OSM Settlement ID", "name": "Settlement Name", "place": "Place Type"})
    facility_table = point_exposure_table(
        facilities,
        classes,
        transform,
        "osm_id",
        "name",
        FACILITY_CONTEXT_M,
        ["facility_category"],
    ).rename(columns={"osm_id": "OSM Facility ID", "name": "Facility Name", "facility_category": "Facility Category"})
    building_table = geometry_exposure_table(
        buildings,
        classes,
        transform,
        "osm_id",
        "name",
        ["building"],
    ).rename(columns={"osm_id": "OSM Building ID", "name": "Building Name", "building": "Building Type"})
    bridge_table = geometry_exposure_table(
        bridges,
        classes,
        transform,
        "osm_id",
        "name",
        ["highway", "length_m"],
    ).rename(columns={"osm_id": "OSM Bridge ID", "name": "Bridge Name", "highway": "Road Class", "length_m": "Bridge Length (m)"})

    road_rows: list[dict[str, object]] = []
    for _, source in roads.iterrows():
        clipped = source.geometry.intersection(scope)
        total_m, maximum, exposed = sampled_line_exposure(classes, transform, clipped)
        road_rows.append(
            {
                "OSM Road ID": source["osm_id"],
                "Road Name": source.get("name"),
                "Road Class": source.get("highway"),
                "Road Length in Analysis Scope (km)": total_m / 1000,
                "Maximum Intersecting Evidence Class": maximum,
                "Primary Exposed Road Length (km)": exposed[3] / 1000,
                "Alternative Exposed Road Length (km)": exposed[2] / 1000,
                "Sensitivity Exposed Road Length (km)": exposed[1] / 1000,
                "Sampling Step (m)": ROAD_SAMPLE_STEP_M,
            }
        )
    road_table = pd.DataFrame(road_rows)

    damage_attributes = pd.read_parquet(root / ROAD_DAMAGE_TABLE)
    damage_geometry = gpd.read_file(
        root / ROAD_DAMAGE_GEOMETRY, layer="road_damage_crosswalk"
    ).to_crs(crs)
    damage = damage_attributes.merge(
        damage_geometry[["Edge ID", "geometry"]], on="Edge ID", how="left", validate="one_to_one"
    )
    damage["Maximum Intersecting Evidence Class"] = [
        max_class_for_geometry(classes, transform, geometry)
        for geometry in damage.geometry
    ]
    damage_table = pd.DataFrame(damage.drop(columns="geometry"))

    settlement_table = normalize_class_columns(settlement_table)
    facility_table = normalize_class_columns(facility_table)
    building_table = normalize_class_columns(building_table)
    bridge_table = normalize_class_columns(bridge_table)
    road_table = normalize_class_columns(road_table)
    damage_table = normalize_class_columns(damage_table)

    output_dir = root / OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "settlements": output_dir / "settlement_hazard_exposure_preprocessed.parquet",
        "facilities": output_dir / "facility_hazard_exposure_preprocessed.parquet",
        "buildings": output_dir / "building_hazard_exposure_preprocessed.parquet",
        "bridges": output_dir / "bridge_hazard_exposure_preprocessed.parquet",
        "roads": output_dir / "road_hazard_exposure_preprocessed.parquet",
        "damage_edges": output_dir / "road_damage_scenario_exposure_preprocessed.parquet",
    }
    settlement_table.to_parquet(outputs["settlements"], index=False)
    facility_table.to_parquet(outputs["facilities"], index=False)
    building_table.to_parquet(outputs["buildings"], index=False)
    bridge_table.to_parquet(outputs["bridges"], index=False)
    road_table.to_parquet(outputs["roads"], index=False)
    damage_table.to_parquet(outputs["damage_edges"], index=False)

    summary_rows: list[dict[str, object]] = []
    for scenario, threshold in SCENARIOS:
        footprint = analysis_scope & (classes >= threshold)
        exposed_population = float(population_20m[footprint].sum())
        road_length_column = {
            3: "Primary Exposed Road Length (km)",
            2: "Alternative Exposed Road Length (km)",
            1: "Sensitivity Exposed Road Length (km)",
        }[threshold]
        summary_rows.append(
            {
                "Scenario": scenario,
                "Minimum Evidence Class": threshold,
                "Footprint Area (sq km)": float(footprint.sum() * pixel_area_km2),
                "Exposed Population": exposed_population,
                "Population Share of Analysis Scope (%)": (
                    100 * exposed_population / population_in_analysis_scope
                    if population_in_analysis_scope > 0
                    else np.nan
                ),
                "Road Features Intersecting Footprint": int(
                    (road_table[road_length_column] > 0).sum()
                ),
                "Exposed Road Length (km)": float(road_table[road_length_column].sum()),
                "Bridges Intersecting Footprint": int(
                    at_least(bridge_table["Maximum Intersecting Evidence Class"], threshold).sum()
                ),
                "Buildings Intersecting Footprint": int(
                    at_least(building_table["Maximum Intersecting Evidence Class"], threshold).sum()
                ),
                "Facilities Directly Exposed": int(
                    at_least(facility_table["Direct Evidence Class"], threshold).sum()
                ),
                "Facilities within 250 m": int(
                    at_least(facility_table["Maximum Evidence Class within 250 m"], threshold).sum()
                ),
                "Settlements Directly Exposed": int(
                    at_least(settlement_table["Direct Evidence Class"], threshold).sum()
                ),
                "Settlements within 500 m": int(
                    at_least(settlement_table["Maximum Evidence Class within 500 m"], threshold).sum()
                ),
                "CEMS Disruption Candidate Edges Intersecting Footprint": int(
                    (
                        damage_table["Is Disruption Candidate"]
                        & at_least(
                            damage_table["Maximum Intersecting Evidence Class"],
                            threshold,
                        )
                    ).sum()
                ),
                "Interpretation": "scenario exposure; not confirmed damage or casualties",
            }
        )
    summary = pd.DataFrame(summary_rows)
    summary_path = output_dir / "hazard_scenario_exposure_summary.parquet"
    summary.to_parquet(summary_path, index=False)
    outputs["summary"] = summary_path
    summary_csv_path = root / "data/exp/data-preprocessing/hazard_scenario_exposure_summary.csv"
    summary_csv_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(summary_csv_path, index=False)
    outputs["summary_csv"] = summary_csv_path

    audit_rows = [
        {
            "measure": "Calibrated population raster total",
            "value": round(calibrated_population_total, 6),
            "unit": "people",
            "status": "reference total across three calibrated districts",
        },
        {
            "measure": "Population covered by hazard reference grid",
            "value": round(float(population_20m.sum()), 6),
            "unit": "people",
            "status": "grid overlap check; less than district total because reference grid is smaller",
        },
        {
            "measure": "Population inside analysis scope",
            "value": round(population_in_analysis_scope, 6),
            "unit": "people",
            "status": "denominator for scenario exposure share",
        },
        {"measure": "Candidate settlements", "value": len(settlement_table), "unit": "features", "status": "inside analysis scope geometry"},
        {"measure": "Candidate facilities", "value": len(facility_table), "unit": "features", "status": "inside analysis scope geometry"},
        {"measure": "Candidate buildings", "value": len(building_table), "unit": "features", "status": "inside analysis scope geometry"},
        {"measure": "Candidate bridges", "value": len(bridge_table), "unit": "features", "status": "inside analysis scope geometry"},
        {"measure": "Candidate road features", "value": len(road_table), "unit": "features", "status": "intersects analysis scope geometry"},
        {"measure": "Road sampling step", "value": ROAD_SAMPLE_STEP_M, "unit": "m", "status": "approximate exposed length"},
    ]
    audit_path = root / AUDIT
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    with audit_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    print(summary.to_string(index=False))
    print(pd.DataFrame(audit_rows).to_string(index=False))
    print({name: str(path) for name, path in outputs.items()})
    print({"audit": str(audit_path), "hazard_grid": profile})


if __name__ == "__main__":
    main()
