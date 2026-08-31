# Geospatial and Satellite Data Plan

## Event definition

- Event date: 26 August 2026.
- Preliminary mechanism: an upstream ice-rock avalanche and temporary blockage released a debris-rich flood into the Lhende-Bhote Koshi-Trishuli river system.
- Preliminary area of interest: longitude 84.5-85.95 E and latitude 27.55-28.60 N. This covers all three core districts, a 10 km network buffer, and the likely upstream source area. It is an acquisition envelope, not the final hazard footprint.
- Interpretation rule: event cause, death toll, missing-person count, and damage counts remain provisional while official situation reporting is active.

## Acquisition sequence

1. Establish authoritative administrative boundaries and P-code crosswalks.
2. Freeze a pre-event road, bridge, settlement, and service baseline using the 25 August 2026 OpenStreetMap snapshot.
3. Acquire terrain, hydrography, population, and official census calibration layers.
4. Acquire Sentinel-1 same-orbit pre/post imagery; begin with 16 and 28 August 2026, relative orbit 85, ascending, VV/VH.
5. Acquire Sentinel-2 Level-2A observations for visual and spectral validation, using scene classification and cloud-probability masks.
6. Compile official and independently mapped damage, road closure, bridge loss, and settlement impact points for validation.
7. Create clipped, projected, analysis-ready layers only after source checksums and licenses are recorded.

## Analytical use

- Sentinel-1: calibrated and terrain-corrected VV/VH change, log-ratio change, and candidate disturbed-area segmentation.
- Sentinel-2: true colour, NDWI/MNDWI, NDVI/NBR-style surface-change diagnostics, conditioned on cloud and snow masks.
- DEM and hydrography: slope, relative elevation, flow paths, channel distance, and terrain-based plausibility constraints.
- Roads and facilities: routable baseline network, damaged-link scenarios, shortest travel times, isolation, and population reconnected by candidate repairs.
- Population and survey evidence: exposed population and contextual vulnerability at supported administrative domains. Survey households will not be assigned to pixels or settlements without validated geocodes.

## Immediate gate

The first analysis gate was passed on 31 August 2026: administrative boundaries, the pre-event road snapshot, six DEM tiles, same-orbit Sentinel-1 metadata, and four clipped RTC rasters are reproducibly available. Large source rasters were window-streamed by AOI rather than downloaded as unrestricted national archives.

The next gate is independent event validation and exposure screening. A preliminary UNOSAT mudflow/rockflow extent and its explicit analysis footprint are now available and have been intersected with radar change, terrain, roads, bridges, settlements, facilities, buildings, and administrative units. Before any final hazard or damage claim, the project still requires optical cloud/snow masking, field or official damage observations, and sensitivity checks for radar thresholds and terrain geometry.

An initial road-access pilot has also been completed. It demonstrates a plausible north-south isolation corridor and stable direction across 0.5-3 km settlement snap thresholds, but it also reveals baseline topology gaps. The road-network gate will be passed only after endpoint/intersection repair is documented, baseline unreachable settlements are audited, alternative road-speed and facility-availability assumptions are run, and the resulting isolation candidates are checked against independent closure or field observations.
