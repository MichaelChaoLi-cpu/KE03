#!/usr/bin/env python3
"""Build a transparent multi-source hazard-evidence consensus raster.

The output is an evidence-confidence classification, not a physical intensity
estimate and not a field-validated event footprint.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import geopandas as gpd
import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.features import rasterize
from rasterio.warp import reproject


S1_VH_CHANGE = Path(
    "data/processed/geospatial/satellite/"
    "sentinel1_rtc_change_2026-08-16_2026-08-28_vh_db_20m.tif"
)
S2_DIR = Path("data/processed/geospatial/satellite")
SLOPE = Path(
    "data/processed/geospatial/base/copernicus_glo30_slope_degrees_utm45n.tif"
)
UNOSAT = Path(
    "data/processed/geospatial/reference/unosat_event_reference.gpkg"
)
CEMS = Path(
    "data/processed/geospatial/reference/copernicus_emsr927_damage_reference.gpkg"
)
HYDRO = Path(
    "data/processed/geospatial/context/hydrocryosphere_context.gpkg"
)
OUTPUT_STACK = Path(
    "data/processed/geospatial/hazard/hazard_evidence_stack_20m.tif"
)
OUTPUT_CLASS = Path(
    "data/processed/geospatial/hazard/hazard_evidence_class_20m.tif"
)
AUDIT = Path(
    "data/exp/data-preprocessing/hazard_evidence_consensus_audit.csv"
)
LEGEND = Path(
    "data/exp/data-preprocessing/hazard_evidence_class_legend.csv"
)
CONSTRUCTION = Path(
    "data/exp/data-preprocessing/hazard_evidence_construction.json"
)

TARGET_CRS = "EPSG:32645"
RADAR_VH_DECREASE_DB = -2.0
OPTICAL_MNDWI_INCREASE = 0.15
CHANNEL_BUFFER_M = 120.0
STEEP_SLOPE_DEGREES = 30.0
OUTSIDE_ANALYSIS = 255


def rasterize_layer(
    path: Path,
    layer: str,
    shape: tuple[int, int],
    transform: rasterio.Affine,
    crs: rasterio.crs.CRS,
    *,
    buffer_m: float = 0.0,
    all_touched: bool = False,
) -> np.ndarray:
    frame = gpd.read_file(path, layer=layer).to_crs(crs)
    frame = frame.loc[
        frame.geometry.notna() & frame.geometry.is_valid & ~frame.geometry.is_empty
    ].copy()
    geometry = frame.geometry
    if buffer_m:
        geometry = geometry.buffer(buffer_m)
    return rasterize(
        ((geom, 1) for geom in geometry),
        out_shape=shape,
        transform=transform,
        fill=0,
        all_touched=all_touched,
        dtype="uint8",
    ).astype(bool)


def read_s2(name: str) -> tuple[np.ndarray, dict[str, object]]:
    path = S2_DIR / name
    with rasterio.open(path) as dataset:
        return dataset.read(1), {
            "transform": dataset.transform,
            "crs": dataset.crs,
            "shape": dataset.shape,
        }


def mndwi(date: str) -> tuple[np.ndarray, dict[str, object]]:
    green, profile = read_s2(f"sentinel2_l2a_{date}_b03_20m.tif")
    swir, other = read_s2(f"sentinel2_l2a_{date}_b11_20m.tif")
    if profile != other:
        raise RuntimeError(f"Sentinel-2 grid mismatch for {date}")
    green = green.astype("float32")
    swir = swir.astype("float32")
    denominator = green + swir
    result = np.full(green.shape, np.nan, dtype="float32")
    np.divide(green - swir, denominator, out=result, where=denominator > 0)
    return result, profile


def optical_change_on_s1(
    target_shape: tuple[int, int],
    target_transform: rasterio.Affine,
    target_crs: rasterio.crs.CRS,
) -> tuple[np.ndarray, int, int]:
    pre, profile = mndwi("2026-08-12")
    post, post_profile = mndwi("2026-08-27")
    if profile != post_profile:
        raise RuntimeError("Pre/post Sentinel-2 grid mismatch")
    pre_valid, valid_profile = read_s2(
        "sentinel2_l2a_2026-08-12_valid_mask_20m.tif"
    )
    post_valid, post_valid_profile = read_s2(
        "sentinel2_l2a_2026-08-27_valid_mask_20m.tif"
    )
    if profile != valid_profile or profile != post_valid_profile:
        raise RuntimeError("Sentinel-2 valid-mask grid mismatch")
    joint_valid = (pre_valid == 1) & (post_valid == 1)
    evidence_source = (
        joint_valid
        & np.isfinite(pre)
        & np.isfinite(post)
        & ((post - pre) >= OPTICAL_MNDWI_INCREASE)
    ).astype("uint8")
    valid_source = joint_valid.astype("uint8")
    evidence_target = np.zeros(target_shape, dtype="uint8")
    valid_target = np.zeros(target_shape, dtype="uint8")
    for source, destination in (
        (evidence_source, evidence_target),
        (valid_source, valid_target),
    ):
        reproject(
            source=source,
            destination=destination,
            src_transform=profile["transform"],
            src_crs=profile["crs"],
            dst_transform=target_transform,
            dst_crs=target_crs,
            resampling=Resampling.nearest,
            src_nodata=0,
            dst_nodata=0,
        )
    return evidence_target.astype(bool), int(joint_valid.sum()), int(
        evidence_source.sum()
    )


def slope_context_on_s1(
    path: Path,
    target_shape: tuple[int, int],
    target_transform: rasterio.Affine,
    target_crs: rasterio.crs.CRS,
) -> np.ndarray:
    with rasterio.open(path) as source:
        slope = source.read(1)
        valid = slope != source.nodata if source.nodata is not None else np.isfinite(slope)
        steep = (valid & (slope >= STEEP_SLOPE_DEGREES)).astype("uint8")
        target = np.zeros(target_shape, dtype="uint8")
        reproject(
            source=steep,
            destination=target,
            src_transform=source.transform,
            src_crs=source.crs,
            dst_transform=target_transform,
            dst_crs=target_crs,
            resampling=Resampling.nearest,
            src_nodata=0,
            dst_nodata=0,
        )
    return target.astype(bool)


def write_single_band(
    path: Path,
    values: np.ndarray,
    profile: dict[str, object],
    description: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    output_profile = profile.copy()
    output_profile.update(
        count=1,
        dtype="uint8",
        nodata=OUTSIDE_ANALYSIS,
        compress="deflate",
        predictor=2,
        tiled=True,
        blockxsize=512,
        blockysize=512,
    )
    with rasterio.open(path, "w", **output_profile) as destination:
        destination.write(values.astype("uint8"), 1)
        destination.set_band_description(1, description)
        destination.update_tags(
            ANALYTICAL_STATUS="screening evidence; not field validated",
            CLASS_TYPE="evidence confidence; not physical hazard intensity",
        )


def write_stack(
    path: Path,
    layers: list[tuple[str, np.ndarray]],
    profile: dict[str, object],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    output_profile = profile.copy()
    output_profile.update(
        count=len(layers),
        dtype="uint8",
        nodata=0,
        compress="deflate",
        predictor=2,
        tiled=True,
        blockxsize=512,
        blockysize=512,
    )
    with rasterio.open(path, "w", **output_profile) as destination:
        for index, (description, values) in enumerate(layers, start=1):
            destination.write(values.astype("uint8"), index)
            destination.set_band_description(index, description)
        destination.update_tags(
            RADAR_RULE=f"Sentinel-1 VH post-minus-pre <= {RADAR_VH_DECREASE_DB} dB",
            OPTICAL_RULE=(
                "Sentinel-2 joint-valid post-minus-pre MNDWI >= "
                f"{OPTICAL_MNDWI_INCREASE}"
            ),
            CHANNEL_RULE=f"within {CHANNEL_BUFFER_M} m of HydroRIVERS",
            SLOPE_RULE=f"slope >= {STEEP_SLOPE_DEGREES} degrees",
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    global S2_DIR
    S2_DIR = root / S2_DIR
    inputs = [root / S1_VH_CHANGE, root / SLOPE, root / UNOSAT, root / CEMS, root / HYDRO]
    for required in inputs:
        if not required.exists():
            raise FileNotFoundError(required)

    with rasterio.open(root / S1_VH_CHANGE) as radar_source:
        profile = radar_source.profile.copy()
        transform = radar_source.transform
        crs = radar_source.crs
        shape = radar_source.shape
        radar_change = radar_source.read(1)
        radar_valid = (
            radar_change != radar_source.nodata
            if radar_source.nodata is not None
            else np.isfinite(radar_change)
        )
    if crs is None:
        raise RuntimeError("Sentinel-1 reference raster has no CRS")

    unosat_mapped = rasterize_layer(
        root / UNOSAT, "affected_extent", shape, transform, crs
    )
    unosat_analysis = rasterize_layer(
        root / UNOSAT, "analysis_extent", shape, transform, crs
    )
    cems_mapped = rasterize_layer(
        root / CEMS, "observed_event", shape, transform, crs
    )
    cems_analysis = rasterize_layer(
        root / CEMS, "area_of_interest", shape, transform, crs
    )
    analysis_scope = unosat_analysis | cems_analysis
    radar_evidence = (
        analysis_scope & radar_valid & (radar_change <= RADAR_VH_DECREASE_DB)
    )
    optical_evidence, optical_valid_source, optical_evidence_source = (
        optical_change_on_s1(shape, transform, crs)
    )
    optical_evidence &= analysis_scope
    channel_context = rasterize_layer(
        root / HYDRO,
        "hydrorivers_context",
        shape,
        transform,
        crs,
        buffer_m=CHANNEL_BUFFER_M,
        all_touched=True,
    ) & analysis_scope
    steep_context = slope_context_on_s1(
        root / SLOPE, shape, transform, crs
    ) & analysis_scope

    mapped_count = unosat_mapped.astype("uint8") + cems_mapped.astype("uint8")
    sensor_count = radar_evidence.astype("uint8") + optical_evidence.astype("uint8")
    context = channel_context | steep_context

    evidence_class = np.full(shape, OUTSIDE_ANALYSIS, dtype="uint8")
    evidence_class[analysis_scope] = 0
    screening = analysis_scope & (sensor_count >= 1) & context
    reference_or_multisensor = analysis_scope & (
        (mapped_count >= 1) | ((sensor_count >= 2) & context)
    )
    convergent = analysis_scope & (
        (mapped_count >= 2) | ((mapped_count >= 1) & (sensor_count >= 1))
    )
    evidence_class[screening] = 1
    evidence_class[reference_or_multisensor] = 2
    evidence_class[convergent] = 3

    stack_layers = [
        ("Analysis Scope", analysis_scope),
        ("UNOSAT Mapped Evidence", unosat_mapped & analysis_scope),
        ("Copernicus Mapped Evidence", cems_mapped & analysis_scope),
        ("Sentinel-1 VH Decrease Evidence", radar_evidence),
        ("Sentinel-2 MNDWI Increase Evidence", optical_evidence),
        ("HydroRIVERS 120 m Channel Context", channel_context),
        ("Slope 30 Degree Context", steep_context),
    ]
    write_stack(root / OUTPUT_STACK, stack_layers, profile)
    write_single_band(
        root / OUTPUT_CLASS,
        evidence_class,
        profile,
        "Hazard Evidence Confidence Class",
    )

    pixel_area_km2 = abs(transform.a * transform.e) / 1_000_000
    audit_rows: list[dict[str, object]] = []
    for name, values in stack_layers:
        pixels = int(values.sum())
        audit_rows.append(
            {
                "measure": name,
                "pixels": pixels,
                "area_sq_km": round(pixels * pixel_area_km2, 4),
                "interpretation": "binary evidence or context layer",
            }
        )
    for code, label in (
        (0, "analysed, no positive evidence"),
        (1, "sensor screening evidence with terrain or channel context"),
        (2, "one mapped reference or multi-sensor contextual evidence"),
        (3, "convergent mapped and sensor evidence"),
    ):
        pixels = int((evidence_class == code).sum())
        audit_rows.append(
            {
                "measure": f"Evidence class {code}",
                "pixels": pixels,
                "area_sq_km": round(pixels * pixel_area_km2, 4),
                "interpretation": label,
            }
        )
    overlap_layers = [
        ("Any mapped reference evidence", (unosat_mapped | cems_mapped) & analysis_scope),
        ("UNOSAT and Copernicus overlap", unosat_mapped & cems_mapped & analysis_scope),
        ("Any mapped evidence and Sentinel-1", (unosat_mapped | cems_mapped) & radar_evidence),
        ("Any mapped evidence and Sentinel-2", (unosat_mapped | cems_mapped) & optical_evidence),
        ("Any mapped evidence and any sensor", (unosat_mapped | cems_mapped) & (radar_evidence | optical_evidence)),
        ("Sentinel-1 and Sentinel-2 overlap", radar_evidence & optical_evidence),
        ("Primary conservative footprint", evidence_class == 3),
        ("Alternative mapped-or-multisensor footprint", (evidence_class >= 2) & (evidence_class != OUTSIDE_ANALYSIS)),
        ("Sensitivity screening footprint", (evidence_class >= 1) & (evidence_class != OUTSIDE_ANALYSIS)),
    ]
    for name, values in overlap_layers:
        pixels = int(values.sum())
        audit_rows.append(
            {
                "measure": name,
                "pixels": pixels,
                "area_sq_km": round(pixels * pixel_area_km2, 4),
                "interpretation": "overlap or scenario footprint",
            }
        )
    audit_rows.extend(
        [
            {
                "measure": "Sentinel-2 joint-valid source pixels",
                "pixels": optical_valid_source,
                "area_sq_km": round(optical_valid_source * pixel_area_km2, 4),
                "interpretation": "before reprojection to the Sentinel-1 grid",
            },
            {
                "measure": "Sentinel-2 source evidence pixels",
                "pixels": optical_evidence_source,
                "area_sq_km": round(optical_evidence_source * pixel_area_km2, 4),
                "interpretation": "joint-valid MNDWI increase before scope masking",
            },
        ]
    )
    audit_path = root / AUDIT
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    with audit_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    legend_rows = [
        {
            "class_code": 0,
            "class_name": "Analysed - no positive evidence",
            "rule": "Inside analysis scope but no evidence rule is met",
            "analytical_use": "comparison area; not evidence of absence",
        },
        {
            "class_code": 1,
            "class_name": "Sensor screening evidence",
            "rule": "At least one sensor signal plus channel or steep-slope context",
            "analytical_use": "sensitivity expansion only",
        },
        {
            "class_code": 2,
            "class_name": "Mapped or multi-sensor evidence",
            "rule": "At least one mapped reference, or both sensors plus context",
            "analytical_use": "alternative footprint",
        },
        {
            "class_code": 3,
            "class_name": "Convergent evidence",
            "rule": "Both mapped sources, or mapped reference plus sensor signal",
            "analytical_use": "primary conservative footprint",
        },
        {
            "class_code": OUTSIDE_ANALYSIS,
            "class_name": "Outside analysis scope",
            "rule": "Outside UNOSAT analysis extent and Copernicus AOIs",
            "analytical_use": "nodata",
        },
    ]
    legend_path = root / LEGEND
    with legend_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(legend_rows[0]))
        writer.writeheader()
        writer.writerows(legend_rows)

    construction_path = root / CONSTRUCTION
    construction_path.write_text(
        json.dumps(
            {
                "status": "proposed_screening_construction_pending_human_confirmation",
                "output_type": "evidence confidence, not physical hazard intensity",
                "reference_grid": {
                    "crs": str(crs),
                    "resolution_m": abs(transform.a),
                    "rows": shape[0],
                    "columns": shape[1],
                },
                "analysis_scope": (
                    "union of UNOSAT analysis extent and current Copernicus EMSR927 AOIs"
                ),
                "thresholds": {
                    "sentinel1_vh_post_minus_pre_db_max": RADAR_VH_DECREASE_DB,
                    "sentinel2_mndwi_post_minus_pre_min": OPTICAL_MNDWI_INCREASE,
                    "hydrorivers_buffer_m": CHANNEL_BUFFER_M,
                    "steep_slope_degrees_min": STEEP_SLOPE_DEGREES,
                },
                "class_rules": {
                    "0": "inside scope with no positive evidence rule",
                    "1": "at least one sensor signal plus channel or steep-slope context",
                    "2": "at least one mapped reference, or both sensors plus context",
                    "3": "both mapped sources, or mapped reference plus sensor signal",
                    "255": "outside analysis scope",
                },
                "interpretation_limits": [
                    "not field validated",
                    "does not establish event-specific climate attribution",
                    "class is evidence confidence rather than physical intensity",
                    "Sentinel-2 is used only where both dates pass the valid-pixel mask",
                ],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print(
        {
            "stack": str(root / OUTPUT_STACK),
            "class": str(root / OUTPUT_CLASS),
            "audit": str(audit_path),
            "legend": str(legend_path),
            "construction": str(construction_path),
        }
    )
    for row in audit_rows:
        print(row)


if __name__ == "__main__":
    main()
