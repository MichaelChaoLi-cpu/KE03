#!/usr/bin/env python3
"""Allocate calibrated population cells to nearby settlements within local units."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from pyproj import Transformer
from rasterio.features import rasterize
from shapely import points
from shapely.strtree import STRtree


POPULATION_RASTER = Path(
    "data/processed/geospatial/population/"
    "worldpop_2024_distribution_calibrated_to_2021_census.tif"
)
ADMIN_SOURCE = Path("data/processed/geospatial/base/event_area_admin.gpkg")
OSM_SOURCE = Path("data/processed/geospatial/base/osm_pre_event_aoi.gpkg")
OUTPUT_DIR = Path("data/processed/geospatial/population")
EXP_DIR = Path("data/exp/data-preprocessing")
PRIMARY_THRESHOLD_M = 3000
THRESHOLDS_M = (500, 1000, 2000, 3000)
METRIC_CRS = "EPSG:32645"


def text_or_missing(value: object) -> object:
    if pd.isna(value):
        return pd.NA
    text = " ".join(str(value).strip().split())
    return text if text else pd.NA


def tag_value(tags: object, key: str) -> str | None:
    if pd.isna(tags):
        return None
    match = re.search(rf'"{re.escape(key)}"=>"([^"]+)"', str(tags))
    return " ".join(match.group(1).strip().split()) if match else None


def ascii_transliteration(value: str) -> str:
    text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return " ".join(text.strip().split())


def preferred_english_name(row: pd.Series) -> str:
    english = tag_value(row.get("other_tags"), "name:en")
    if english:
        transliterated = ascii_transliteration(english)
        if transliterated:
            return transliterated
    source_name = text_or_missing(row.get("name"))
    if source_name is not pd.NA and str(source_name).isascii():
        return str(source_name)
    alternative = tag_value(row.get("other_tags"), "alt_name")
    if alternative and alternative.isascii():
        return alternative.split(";")[0].strip()
    return f"OSM Settlement {row['osm_id']}"


def assign_settlement_admin(
    settlements: gpd.GeoDataFrame,
    local_units: gpd.GeoDataFrame,
    districts: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    settlement_frame = settlements.reset_index(drop=True).copy()
    settlement_frame["_settlement_index"] = np.arange(len(settlement_frame))
    admin_columns = [
        "adm3_name",
        "adm3_pcode",
        "geometry",
    ]
    joined = gpd.sjoin(
        settlement_frame,
        local_units[admin_columns],
        how="left",
        predicate="intersects",
    )
    joined = joined.sort_values(
        ["_settlement_index", "adm3_pcode"], na_position="last"
    ).drop_duplicates("_settlement_index", keep="first")
    joined = joined.sort_values("_settlement_index").reset_index(drop=True)
    if len(joined) != len(settlements):
        raise RuntimeError("Settlement-to-local-unit join changed the settlement count.")
    joined = joined.drop(columns="index_right")
    district_columns = ["adm2_name", "adm2_pcode", "geometry"]
    joined = gpd.sjoin(
        joined,
        districts[district_columns],
        how="left",
        predicate="intersects",
    )
    joined = joined.sort_values(
        ["_settlement_index", "adm2_pcode"], na_position="last"
    ).drop_duplicates("_settlement_index", keep="first")
    joined = joined.sort_values("_settlement_index").reset_index(drop=True)
    if len(joined) != len(settlements) or joined["adm2_pcode"].isna().any():
        raise RuntimeError("Settlement-to-district spatial join is incomplete.")
    return gpd.GeoDataFrame(joined, geometry="geometry", crs=settlements.crs)


def aggregate_for_threshold(
    population: np.ndarray,
    nearest_settlement: np.ndarray,
    nearest_distance_m: np.ndarray,
    settlement_count: int,
    threshold_m: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    allocated = (nearest_settlement >= 0) & (nearest_distance_m <= threshold_m)
    assigned_index = nearest_settlement[allocated]
    assigned_population = population[allocated]
    assigned_distance = nearest_distance_m[allocated]

    population_sum = np.bincount(
        assigned_index,
        weights=assigned_population,
        minlength=settlement_count,
    ).astype("float64")
    cell_count = np.bincount(
        assigned_index, minlength=settlement_count
    ).astype("int64")
    weighted_distance_sum = np.bincount(
        assigned_index,
        weights=assigned_population * assigned_distance,
        minlength=settlement_count,
    ).astype("float64")
    mean_distance = np.full(settlement_count, np.nan, dtype="float64")
    positive_population = population_sum > 0
    mean_distance[positive_population] = (
        weighted_distance_sum[positive_population]
        / population_sum[positive_population]
    )
    max_distance = np.full(settlement_count, np.nan, dtype="float64")
    if assigned_index.size:
        max_distance_work = np.full(settlement_count, -np.inf, dtype="float64")
        np.maximum.at(max_distance_work, assigned_index, assigned_distance)
        max_distance[cell_count > 0] = max_distance_work[cell_count > 0]
    return population_sum, cell_count, mean_distance, max_distance


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    population_path = root / POPULATION_RASTER
    admin_path = root / ADMIN_SOURCE
    osm_path = root / OSM_SOURCE
    for required in (population_path, admin_path, osm_path):
        if not required.exists():
            raise FileNotFoundError(required)

    local_units = gpd.read_file(admin_path, layer="local_units")
    districts = gpd.read_file(admin_path, layer="districts")
    settlements = gpd.read_file(osm_path, layer="settlements")
    if settlements["osm_id"].astype("string").duplicated().any():
        raise RuntimeError("OSM settlement identifiers are not unique.")

    settlements = assign_settlement_admin(settlements, local_units, districts)
    settlements["Settlement Name"] = settlements.apply(
        preferred_english_name, axis=1
    )
    settlements["OSM settlement ID"] = settlements["osm_id"].astype("string")
    settlements["Place Type"] = settlements["place"].map(text_or_missing).astype(
        "string"
    )
    settlements["Original OSM Name"] = settlements["name"].map(
        text_or_missing
    ).astype("string")

    with rasterio.open(population_path) as source:
        raster_crs = source.crs
        transform = source.transform
        values = source.read(1)
        valid = np.isfinite(values) & (values >= 0)
        if source.nodata is not None:
            valid &= values != source.nodata
        positive = valid & (values > 0)
        rows, columns = np.nonzero(positive)
        population = values[rows, columns].astype("float64")
        local_units_raster = local_units.to_crs(raster_crs).reset_index(drop=True)
        districts_raster = districts.to_crs(raster_crs).reset_index(drop=True)
        admin_index_raster = rasterize(
            (
                (geometry, index)
                for index, geometry in enumerate(local_units_raster.geometry)
            ),
            out_shape=values.shape,
            transform=transform,
            fill=-1,
            dtype="int16",
            all_touched=False,
        )
        district_index_raster = rasterize(
            (
                (geometry, index)
                for index, geometry in enumerate(districts_raster.geometry)
            ),
            out_shape=values.shape,
            transform=transform,
            fill=-1,
            dtype="int16",
            all_touched=False,
        )

    pixel_admin_index = admin_index_raster[rows, columns].astype("int64")
    pixel_district_index = district_index_raster[rows, columns].astype("int64")
    longitude = (
        transform.c
        + (columns + 0.5) * transform.a
        + (rows + 0.5) * transform.b
    )
    latitude = (
        transform.f
        + (columns + 0.5) * transform.d
        + (rows + 0.5) * transform.e
    )
    transformer = Transformer.from_crs(raster_crs, METRIC_CRS, always_xy=True)
    pixel_x, pixel_y = transformer.transform(longitude, latitude)

    settlements_metric = settlements.to_crs(METRIC_CRS).reset_index(drop=True)
    settlement_admin_lookup = {
        code: index
        for index, code in enumerate(local_units_raster["adm3_pcode"].tolist())
    }
    settlements_metric["_admin_index"] = settlements_metric["adm3_pcode"].map(
        settlement_admin_lookup
    )

    nearest_settlement = np.full(len(population), -1, dtype="int64")
    nearest_distance_m = np.full(len(population), np.inf, dtype="float64")
    for admin_index in range(len(local_units_raster)):
        pixel_positions = np.flatnonzero(pixel_admin_index == admin_index)
        settlement_positions = np.flatnonzero(
            settlements_metric["_admin_index"].to_numpy() == admin_index
        )
        if pixel_positions.size == 0 or settlement_positions.size == 0:
            continue
        tree = STRtree(
            settlements_metric.geometry.iloc[settlement_positions].to_numpy()
        )
        pixel_geometries = points(
            np.column_stack((pixel_x[pixel_positions], pixel_y[pixel_positions]))
        )
        pair_indices, distances = tree.query_nearest(
            pixel_geometries,
            all_matches=False,
            return_distance=True,
        )
        input_positions = pair_indices[0]
        tree_positions = pair_indices[1]
        global_pixels = pixel_positions[input_positions]
        nearest_settlement[global_pixels] = settlement_positions[tree_positions]
        nearest_distance_m[global_pixels] = distances

    total_population = float(population.sum(dtype="float64"))
    population_inside_admin = float(
        population[pixel_admin_index >= 0].sum(dtype="float64")
    )
    population_outside_admin = total_population - population_inside_admin
    settlement_count = len(settlements_metric)

    base_columns = {
        "OSM Settlement ID": settlements_metric["OSM settlement ID"].astype(
            "string"
        ),
        "Settlement Name": settlements_metric["Settlement Name"].astype("string"),
        "Original OSM Name": settlements_metric["Original OSM Name"].astype(
            "string"
        ),
        "Place Type": settlements_metric["Place Type"].astype("string"),
        "Local Unit": settlements_metric["adm3_name"].astype("string"),
        "Local Unit P-Code": settlements_metric["adm3_pcode"].astype("string"),
        "District": settlements_metric["adm2_name"].astype("string"),
        "District P-Code": settlements_metric["adm2_pcode"].astype("string"),
        "Settlement Longitude": settlements.geometry.x.astype("float64"),
        "Settlement Latitude": settlements.geometry.y.astype("float64"),
    }

    sensitivity_frames: list[pd.DataFrame] = []
    threshold_rows: list[dict[str, object]] = []
    local_audit_rows: list[dict[str, object]] = []
    previous_allocated = -np.inf
    for threshold_m in THRESHOLDS_M:
        population_sum, cell_count, mean_distance, max_distance = (
            aggregate_for_threshold(
                population,
                nearest_settlement,
                nearest_distance_m,
                settlement_count,
                threshold_m,
            )
        )
        frame = pd.DataFrame(base_columns)
        frame["Allocation Threshold (m)"] = threshold_m
        frame["Estimated Settlement Population"] = population_sum
        frame["Allocated Population Cell Count"] = cell_count
        frame["Population-Weighted Mean Allocation Distance (m)"] = mean_distance
        frame["Maximum Allocation Distance (m)"] = max_distance
        frame["Has Assigned Population"] = population_sum > 0
        sensitivity_frames.append(frame)

        allocated_population = float(population_sum.sum(dtype="float64"))
        if allocated_population + 1e-8 < previous_allocated:
            raise RuntimeError("Allocated population is not monotonic by threshold.")
        previous_allocated = allocated_population
        unallocated_population = total_population - allocated_population
        threshold_rows.append(
            {
                "Allocation Threshold (m)": threshold_m,
                "Calibrated Raster Population": total_population,
                "Population inside Local Units": population_inside_admin,
                "Population outside Local Units": population_outside_admin,
                "Allocated Settlement Population": allocated_population,
                "Unallocated Population": unallocated_population,
                "Allocated Population Share (%)": (
                    100 * allocated_population / total_population
                ),
                "Unallocated Population Share (%)": (
                    100 * unallocated_population / total_population
                ),
                "Settlements with Assigned Population": int(
                    (population_sum > 0).sum()
                ),
                "Total Settlements": settlement_count,
                "Positive Population Cells Allocated": int(cell_count.sum()),
                "Total Positive Population Cells": len(population),
            }
        )

        for admin_index, local_unit in local_units_raster.iterrows():
            unit_pixels = pixel_admin_index == admin_index
            unit_population = float(population[unit_pixels].sum(dtype="float64"))
            unit_settlements = np.flatnonzero(
                settlements_metric["_admin_index"].to_numpy() == admin_index
            )
            unit_allocated = float(population_sum[unit_settlements].sum())
            local_audit_rows.append(
                {
                    "Allocation Threshold (m)": threshold_m,
                    "Local Unit": local_unit["adm3_name"],
                    "Local Unit P-Code": local_unit["adm3_pcode"],
                    "District": local_unit["adm2_name"],
                    "District P-Code": local_unit["adm2_pcode"],
                    "Settlement Count": len(unit_settlements),
                    "Input Population": unit_population,
                    "Allocated Population": unit_allocated,
                    "Unallocated Population": unit_population - unit_allocated,
                    "Conservation Difference": (
                        unit_population
                        - unit_allocated
                        - (unit_population - unit_allocated)
                    ),
                }
            )

    sensitivity = pd.concat(sensitivity_frames, ignore_index=True)
    primary = sensitivity.loc[
        sensitivity["Allocation Threshold (m)"] == PRIMARY_THRESHOLD_M
    ].copy()
    threshold_summary = pd.DataFrame(threshold_rows)
    local_audit = pd.DataFrame(local_audit_rows)

    admin_names = np.full(len(population), None, dtype=object)
    admin_codes = np.full(len(population), None, dtype=object)
    district_names = np.full(len(population), None, dtype=object)
    district_codes = np.full(len(population), None, dtype=object)
    inside_admin = pixel_admin_index >= 0
    admin_names[inside_admin] = local_units_raster["adm3_name"].to_numpy()[
        pixel_admin_index[inside_admin]
    ]
    admin_codes[inside_admin] = local_units_raster["adm3_pcode"].to_numpy()[
        pixel_admin_index[inside_admin]
    ]
    inside_district = pixel_district_index >= 0
    district_names[inside_district] = districts_raster["adm2_name"].to_numpy()[
        pixel_district_index[inside_district]
    ]
    district_codes[inside_district] = districts_raster["adm2_pcode"].to_numpy()[
        pixel_district_index[inside_district]
    ]
    nearest_ids = np.full(len(population), None, dtype=object)
    has_nearest = nearest_settlement >= 0
    nearest_ids[has_nearest] = settlements_metric["OSM settlement ID"].to_numpy()[
        nearest_settlement[has_nearest]
    ]
    cell_crosswalk = pd.DataFrame(
        {
            "Population Cell ID": rows.astype("int64") * values.shape[1]
            + columns.astype("int64"),
            "Raster Row": rows.astype("int32"),
            "Raster Column": columns.astype("int32"),
            "Cell Longitude": longitude,
            "Cell Latitude": latitude,
            "Calibrated Population": population,
            "Local Unit": pd.array(admin_names, dtype="string"),
            "Local Unit P-Code": pd.array(admin_codes, dtype="string"),
            "District": pd.array(district_names, dtype="string"),
            "District P-Code": pd.array(district_codes, dtype="string"),
            "Nearest OSM Settlement ID": pd.array(nearest_ids, dtype="string"),
            "Nearest Settlement Distance (m)": np.where(
                has_nearest, nearest_distance_m, np.nan
            ),
            "Allocated within 3000 m": has_nearest
            & (nearest_distance_m <= PRIMARY_THRESHOLD_M),
        }
    )

    if len(primary) != settlement_count:
        raise RuntimeError("Primary output does not contain one row per settlement.")
    if primary["OSM Settlement ID"].duplicated().any():
        raise RuntimeError("Primary output contains duplicate settlements.")
    if not np.allclose(
        threshold_summary["Allocated Settlement Population"]
        + threshold_summary["Unallocated Population"],
        total_population,
        rtol=0,
        atol=1e-6,
    ):
        raise RuntimeError("Population is not conserved in threshold summaries.")
    if (local_audit["Conservation Difference"].abs() > 1e-8).any():
        raise RuntimeError("Population is not conserved in local-unit audits.")
    if any(not str(column).isascii() for column in sensitivity.columns):
        raise RuntimeError("Non-English output column detected.")

    output_dir = root / OUTPUT_DIR
    exp_dir = root / EXP_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    exp_dir.mkdir(parents=True, exist_ok=True)
    primary_path = output_dir / "settlement_population_allocation_preprocessed.parquet"
    sensitivity_path = (
        output_dir / "settlement_population_allocation_sensitivity_preprocessed.parquet"
    )
    threshold_path = (
        output_dir / "population_allocation_threshold_summary_preprocessed.parquet"
    )
    cell_path = output_dir / "population_cell_settlement_crosswalk_preprocessed.parquet"
    local_audit_path = exp_dir / "settlement_population_allocation_audit.csv"
    threshold_csv_path = exp_dir / "population_allocation_threshold_summary.csv"
    metadata_path = exp_dir / "settlement_population_allocation_run.json"

    primary.to_parquet(primary_path, index=False)
    sensitivity.to_parquet(sensitivity_path, index=False)
    threshold_summary.to_parquet(threshold_path, index=False)
    cell_crosswalk.to_parquet(cell_path, index=False)
    local_audit.to_csv(local_audit_path, index=False)
    threshold_summary.to_csv(threshold_csv_path, index=False)
    metadata_path.write_text(
        json.dumps(
            {
                "status": "complete",
                "primary_threshold_m": PRIMARY_THRESHOLD_M,
                "sensitivity_thresholds_m": list(THRESHOLDS_M),
                "metric_crs": METRIC_CRS,
                "settlements": settlement_count,
                "local_units": len(local_units_raster),
                "positive_population_cells": len(population),
                "calibrated_population": total_population,
                "outputs": {
                    "primary": str(primary_path.relative_to(root)),
                    "sensitivity": str(sensitivity_path.relative_to(root)),
                    "threshold_summary": str(threshold_path.relative_to(root)),
                    "cell_crosswalk": str(cell_path.relative_to(root)),
                    "local_unit_audit": str(local_audit_path.relative_to(root)),
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(threshold_summary.to_string(index=False))
    print(
        {
            "primary": str(primary_path),
            "sensitivity": str(sensitivity_path),
            "threshold_summary": str(threshold_path),
            "cell_crosswalk": str(cell_path),
            "local_unit_audit": str(local_audit_path),
        }
    )


if __name__ == "__main__":
    main()
