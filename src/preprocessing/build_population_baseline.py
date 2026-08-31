#!/usr/bin/env python3
"""Calibrate the WorldPop spatial distribution to official 2021 district totals."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.enums import Resampling
from rasterio.features import geometry_mask
from rasterio.mask import mask
from shapely.geometry import mapping


WORLDPOP_RELATIVE = Path(
    "data/raw/geospatial/population/worldpop_2024_constrained_100m/"
    "npl_pop_2024_CN_100m_R2024A_v1.tif"
)
CENSUS_RELATIVE = Path(
    "data/raw/geospatial/population/census_2021/Indv05_SizeOfLocalities.csv"
)
ADMIN_RELATIVE = Path("data/processed/geospatial/base/event_area_admin.gpkg")
OUTPUT_RASTER_RELATIVE = Path(
    "data/processed/geospatial/population/"
    "worldpop_2024_distribution_calibrated_to_2021_census.tif"
)
DISTRICT_OUTPUT_RELATIVE = Path(
    "data/processed/geospatial/population/district_population_calibration.parquet"
)
LOCAL_UNIT_OUTPUT_RELATIVE = Path(
    "data/processed/geospatial/population/local_unit_population_estimates.parquet"
)
AUDIT_RELATIVE = Path(
    "data/exp/data-preprocessing/population_calibration_audit.csv"
)
NODATA = -99999.0


def normalized_name(value: object) -> str:
    return " ".join(str(value).strip().casefold().split())


def census_totals(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    totals = frame.loc[
        (frame["sizeclass"] == 0) & (frame["dist"] > 0),
        ["dname", "noHhld", "total", "male", "feml"],
    ].copy()
    totals["match_name"] = totals["dname"].map(normalized_name)
    if totals["match_name"].duplicated().any():
        duplicates = totals.loc[totals["match_name"].duplicated(), "dname"].tolist()
        raise RuntimeError(f"Duplicate census district names: {duplicates}")
    return totals


def pixel_sum(
    values: np.ndarray, transform, geometry, source_nodata: float | None
) -> float:
    inside = geometry_mask(
        [mapping(geometry)],
        out_shape=values.shape,
        transform=transform,
        invert=True,
        all_touched=False,
    )
    valid = inside & np.isfinite(values) & (values >= 0)
    if source_nodata is not None:
        valid &= values != source_nodata
    return float(values[valid].sum(dtype="float64"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    worldpop_path = root / WORLDPOP_RELATIVE
    census_path = root / CENSUS_RELATIVE
    admin_path = root / ADMIN_RELATIVE
    output_path = root / OUTPUT_RASTER_RELATIVE
    district_output = root / DISTRICT_OUTPUT_RELATIVE
    local_unit_output = root / LOCAL_UNIT_OUTPUT_RELATIVE
    audit_path = root / AUDIT_RELATIVE

    for required in (worldpop_path, census_path, admin_path):
        if not required.exists():
            raise FileNotFoundError(required)

    totals = census_totals(census_path)
    districts = gpd.read_file(admin_path, layer="districts")
    local_units = gpd.read_file(admin_path, layer="local_units")
    districts["match_name"] = districts["adm2_name"].map(normalized_name)
    districts = districts.merge(totals, on="match_name", how="left", validate="one_to_one")
    if districts["total"].isna().any():
        missing = districts.loc[districts["total"].isna(), "adm2_name"].tolist()
        raise RuntimeError(f"No census totals found for event-area districts: {missing}")

    with rasterio.open(worldpop_path) as source:
        districts_raster = districts.to_crs(source.crs)
        local_units_raster = local_units.to_crs(source.crs)
        source_nodata = source.nodata
        raw, output_transform = mask(
            source,
            [mapping(districts_raster.geometry.union_all())],
            crop=True,
            all_touched=False,
            filled=True,
            nodata=source_nodata,
        )
        raw = raw[0].astype("float64")
        profile = source.profile.copy()

    calibrated = np.full(raw.shape, NODATA, dtype="float32")
    calibration_rows: list[dict[str, object]] = []
    for _, district in districts_raster.iterrows():
        inside = geometry_mask(
            [mapping(district.geometry)],
            out_shape=raw.shape,
            transform=output_transform,
            invert=True,
            all_touched=False,
        )
        valid = inside & np.isfinite(raw) & (raw >= 0)
        if source_nodata is not None:
            valid &= raw != source_nodata
        modeled_total = float(raw[valid].sum(dtype="float64"))
        if modeled_total <= 0:
            raise RuntimeError(f"No modeled population in {district['adm2_name']}")
        official_total = float(district["total"])
        factor = official_total / modeled_total
        calibrated[valid] = (raw[valid] * factor).astype("float32")
        calibrated_total = float(calibrated[valid].sum(dtype="float64"))
        calibration_rows.append(
            {
                "District": district["adm2_name"],
                "District P-Code": district["adm2_pcode"],
                "Official 2021 Population": int(official_total),
                "Official 2021 Households": int(district["noHhld"]),
                "WorldPop 2024 Modeled Population": modeled_total,
                "Calibration Factor": factor,
                "Calibrated Population": calibrated_total,
                "Calibration Difference": calibrated_total - official_total,
            }
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    profile.update(
        driver="GTiff",
        height=calibrated.shape[0],
        width=calibrated.shape[1],
        count=1,
        dtype="float32",
        transform=output_transform,
        nodata=NODATA,
        compress="DEFLATE",
        predictor=3,
        tiled=True,
        blockxsize=512,
        blockysize=512,
        BIGTIFF="IF_SAFER",
    )
    with rasterio.open(output_path, "w", **profile) as destination:
        destination.write(calibrated, 1)
        destination.update_tags(
            variable="population count",
            spatial_distribution="WorldPop R2024A 2024 constrained 100 m",
            calibration="Nepal NSO 2021 district population totals",
            calibration_method="multiplicative factor within each district",
            interpretation=(
                "modeled pre-event population distribution calibrated to official "
                "district totals; not household locations"
            ),
        )
        # Overviews are for display only. This GDAL build does not expose
        # additive overviews, so preserve all analytical counts in the base
        # raster and use averages solely for pyramided visualization.
        destination.build_overviews([2, 4, 8, 16], Resampling.average)
        destination.update_tags(
            ns="rio_overview",
            resampling="average",
            analytical_counts="use_base_resolution_only",
        )

    district_frame = pd.DataFrame(calibration_rows)
    district_output.parent.mkdir(parents=True, exist_ok=True)
    district_frame.to_parquet(district_output, index=False)

    local_rows: list[dict[str, object]] = []
    for _, local_unit in local_units_raster.iterrows():
        estimated = pixel_sum(
            calibrated, output_transform, local_unit.geometry, NODATA
        )
        local_rows.append(
            {
                "Local Unit": local_unit["adm3_name"],
                "Local Unit P-Code": local_unit["adm3_pcode"],
                "District": local_unit["adm2_name"],
                "District P-Code": local_unit["adm2_pcode"],
                "Estimated Population": estimated,
                "Spatial Distribution Year": 2024,
                "Calibration Census Year": 2021,
            }
        )
    local_frame = pd.DataFrame(local_rows)
    local_unit_output.parent.mkdir(parents=True, exist_ok=True)
    local_frame.to_parquet(local_unit_output, index=False)

    audit_path.parent.mkdir(parents=True, exist_ok=True)
    with audit_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "district",
                "district_pcode",
                "official_2021_population",
                "worldpop_2024_modeled_population",
                "calibration_factor",
                "calibrated_population",
                "absolute_difference",
            ],
        )
        writer.writeheader()
        for row in calibration_rows:
            writer.writerow(
                {
                    "district": row["District"],
                    "district_pcode": row["District P-Code"],
                    "official_2021_population": row["Official 2021 Population"],
                    "worldpop_2024_modeled_population": round(
                        float(row["WorldPop 2024 Modeled Population"]), 6
                    ),
                    "calibration_factor": round(float(row["Calibration Factor"]), 9),
                    "calibrated_population": round(
                        float(row["Calibrated Population"]), 6
                    ),
                    "absolute_difference": round(
                        abs(float(row["Calibration Difference"])), 6
                    ),
                }
            )

    print(district_frame.to_string(index=False))
    print(
        {
            "raster": str(output_path),
            "district_table": str(district_output),
            "local_unit_table": str(local_unit_output),
            "local_units": len(local_frame),
            "audit": str(audit_path),
        }
    )


if __name__ == "__main__":
    main()
