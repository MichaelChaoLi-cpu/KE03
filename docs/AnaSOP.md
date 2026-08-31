# AnaSOP
Analysis Standard Operating Procedure

## 1. Research Objective

### Central Research Question

- Research question: Which settlements in the Rasuwa-Bhote Koshi-Trishuli mountain corridor face the highest intervention priority because of the joint effects of the 2026 cascading-hazard footprint, population and infrastructure exposure, road-network isolation, and pre-disaster social vulnerability?
- Why it matters: A physical hazard map alone cannot identify where limited rescue, road-repair, and service-restoration resources will reduce the greatest human hardship in a mountainous transport network.
- Data support currently visible: Existing household surveys describe poverty, service access, disaster preparedness, historical losses, assistance, and coping. Event-specific hazard, settlement, road, facility, and population layers remain to be acquired.
- Key readable variables or data scope: Hazard Intensity, Exposed Population, Exposed Infrastructure, Accessibility Loss, Baseline Deprivation, Preparedness Capacity, Coping Stress, and Intervention Priority.
- What would verify it: A reproducible multi-source analysis identifies settlements or road sections that remain high priority across alternative hazard footprints, road-closure scenarios, vulnerability constructions, and weighting schemes.
- What would falsify or weaken it: The available event footprint cannot be reconstructed with acceptable agreement across independent sources; road failures produce little measurable accessibility change; or survey geography cannot support even area-level vulnerability context.
- Required next feasibility check: Verify survey variable coverage now, then verify event imagery, current road and facility topology, population surfaces, and geographic crosswalks before spatial integration.

### Supporting Research Questions

The final plan should contain 4-5 total research questions: one central question plus supporting questions that deepen or broaden it.

#### Supporting Point 1: Cascading-Hazard Footprint

- Role relative to central point: deepen the physical-hazard component.
- Research question: What was the spatial extent and relative intensity of the ice-rock avalanche, temporary blockage, flood, erosion, and landslide cascade associated with the 2026 event?
- Why it matters: All downstream exposure and network estimates depend on a defensible event footprint rather than a single unvalidated map.
- Data support currently visible: Local survey data do not measure the event footprint; pre-event and post-event satellite imagery, terrain, rainfall, and independent emergency mapping are required.
- Key readable variables or data scope: Surface Change, Inundation or Debris Footprint, Terrain Slope, Flow Path, Distance to Channel, and Hazard Intensity Class.
- What would verify it: Optical, radar, terrain-based, and independent mapped evidence converge on a coherent affected corridor.
- What would falsify or weaken it: Cloud, snow, radar geometry, timing, or lack of reference observations prevents stable delineation.
- Required feasibility check: Confirm suitable pre-event and post-event observations and reference products for the affected corridor.

#### Supporting Point 2: Network Isolation and Service Loss

- Role relative to central point: identify the mechanism translating physical damage into indirect human impact.
- Research question: Which road and bridge disruptions generated the largest increases in travel time or complete loss of access to health care, markets, and administrative services?
- Why it matters: In mountain corridors, a small number of damaged links can isolate communities well beyond the directly affected footprint.
- Data support currently visible: Household surveys contain baseline facility-access and travel measures; a current routable road network, bridge inventory, service locations, and disruption evidence are still required.
- Key readable variables or data scope: Baseline Travel Time, Post-Disruption Travel Time, Accessibility Loss, Isolated Population, Critical Road Section, and Restored Access after Repair.
- What would verify it: Removing or degrading affected links produces plausible and field-consistent changes in shortest paths and service catchments.
- What would falsify or weaken it: The road graph is not routable, closures cannot be located, or alternative routes make estimated isolation negligible.
- Required feasibility check: Audit network completeness, bridge representation, facility locations, closure evidence, and travel-time assumptions.

#### Supporting Point 3: Baseline Social Vulnerability

- Role relative to central point: explain heterogeneity in the capacity to prepare, cope, and recover.
- Research question: Which dimensions of pre-disaster poverty, service deprivation, preparedness, historical loss, assistance, and harmful coping indicate lower capacity to withstand isolation and service interruption?
- Why it matters: Communities with equal physical exposure may experience different hardship because their resources and response capacities differ.
- Data support currently visible: Recent living-standards data support poverty and service-access profiles; a climate-focused survey supports preparedness benchmarks; a three-wave vulnerability panel supports historical shock, loss, assistance, and coping analysis.
- Key readable variables or data scope: Poverty Status, Per Capita Expenditure, Facility Travel Time, Pre-Warning Receipt, Household Preparedness, Risk-Reduction Participation, Shock Loss, Assistance Receipt, and Harmful Coping.
- What would verify it: Weighted estimates yield interpretable, internally coherent deprivation, preparedness, and coping dimensions with acceptable uncertainty at supported reporting domains.
- What would falsify or weaken it: Indicators are too incomplete, inconsistent across surveys, geographically incomparable, or too imprecise in the event area.
- Required feasibility check: Confirm coding, weights, units of observation, cross-wave harmonization, supported geographic domains, and small-sample restrictions.

#### Supporting Point 4: Robust Intervention Priorities

- Role relative to central point: translate evidence into decision support and test robustness.
- Research question: Which settlements, road sections, and service facilities remain high priority across plausible hazard, network-disruption, vulnerability, and weighting assumptions?
- Why it matters: Operational decisions should not depend on one arbitrary composite score or one uncertain hazard boundary.
- Data support currently visible: Survey data can support candidate vulnerability components; all spatial components and intervention scenarios remain to be constructed.
- Key readable variables or data scope: Hazard Intensity, Exposed Population, Accessibility Loss, Social Vulnerability, Priority Rank, Rank Stability, and Population Reconnected.
- What would verify it: Priority ranks are stable under equal weights, policy weights, random-weight simulations, alternative hazard thresholds, and leave-one-component-out checks.
- What would falsify or weaken it: Rankings reverse under minor assumptions or no intervention consistently restores meaningful access.
- Required feasibility check: Pre-specify component scaling, scenario ranges, candidate interventions, validation criteria, and rank-stability thresholds.

### Scope of Analysis

- Topics: Cascading hazards, settlement and infrastructure exposure, road-network isolation, social vulnerability, preparedness, coping, and intervention prioritization.
- Units of analysis: Settlements and road sections for the spatial decision analysis; households, shock episodes, and supported survey domains for the vulnerability evidence. Household survey records will not be assigned to settlements without validated geocodes.
- Spatial scope: The transboundary event corridor with primary operational focus on Rasuwa and downstream connected communities; broader survey domains provide contextual benchmarks only.
- Period: Pre-disaster survey evidence from 2016-2023 and the August 2026 event, with satellite windows and road-disruption scenarios to be defined after data acquisition.

### Study Design Declaration

- Research type: applied
- Study design: Observational, multi-source spatial decision analysis combining weighted survey evidence, remote-sensing change detection, spatial exposure measurement, road-network disruption simulation, and multi-criteria robustness analysis.
- Interpretation limit: Results will identify descriptive exposure, modeled isolation, contextual vulnerability, and robust intervention priorities. They will not identify household-level effects of the 2026 event, establish causal impacts, or provide definitive climate attribution.

## 2. Theoretical Background  /  Conceptual Framework  /  Problem Formulation

Research type: applied
Section focus: Empirical context, actionable prioritization, and cautious interpretation limits.

### Research Gap

- Emergency mapping can delineate a physical hazard footprint, but it does not by itself show which communities lose access to essential services or have the least capacity to cope and recover.
- Household surveys describe socioeconomic vulnerability and preparedness, while disaster remote sensing and road-network studies often remain separate. The applied gap is an auditable framework that links these evidence layers without pretending that pre-disaster surveys directly measure post-disaster household outcomes.

### Conceptual Framework

- The event cascade creates direct physical exposure and can disrupt a sparse mountain transport network. Network disruption increases travel time or isolates settlements from essential services. Pre-existing deprivation, weak preparedness, and constrained coping capacity can amplify the practical consequences of this isolation.
- For settlement or road unit \(s\), the baseline additive priority formulation is:

\[
P_s = w_H H_s + w_E E_s + w_A A_s + w_V V_s
\]

  where \(H_s\) is hazard intensity, \(E_s\) is exposed population and infrastructure, \(A_s\) is modeled accessibility loss, and \(V_s\) is contextual social vulnerability. The study will not treat one weight vector as uniquely correct; it will compare alternative weights, multiplicative formulations, hazard thresholds, and disruption scenarios.
- Scope boundary: Survey indicators will be reported only at geographic levels supported by their design and identifiers. They will not be downscaled to settlements or pixels without validated geographic linkage or an explicit small-area model with independent validation.

### Problem Formulation

- Primary decision outcomes are settlement priority rank, road-section criticality, modeled accessibility loss, isolated population, and population reconnected under candidate repairs.
- Physical explanatory components are event intensity, terrain and flow-path context, and direct exposure. Network components are road or bridge disruption and alternative-route availability. Social components are poverty and service deprivation, preparedness, historical shock loss, assistance, and coping constraints.
- Survey analysis will use sampling weights and uncertainty estimates. Historical panel associations may clarify coping mechanisms but will remain auxiliary to the event-specific spatial analysis.
- Interpretation limit: The design supports descriptive comparison, scenario analysis, and decision prioritization. It does not support household-level causal inference for the 2026 disaster and will explicitly propagate spatial, sampling, scenario, and weighting uncertainty.

## 3. Data Overview

### Data Scope

- The available evidence comprises three principal household-survey families, repeated survey years, spatial boundary layers, and supporting questionnaires and reports.
- The metadata audit read 814 Stata modules and catalogued 23883 variable records.
- Focused descriptive screening summarized 173 disaster-relevant candidate variables and generated 128 distribution plots.
- The most recent climate-focused survey preserves PSU, province, ecological-belt, and risk-stratum identifiers, but the public district, ward, latitude, and longitude values are masked; direct raster linkage requires a restricted PSU-coordinate file or a verified administrative crosswalk.
- A three-wave household panel contains repeated shock, loss, coping, assistance, and welfare measures with district and PSU identifiers.
- The latest living-standards survey contains poverty, service access, transport, housing, and welfare measures with PSU and broader geographic identifiers.
- A current humanitarian administrative-boundary release has been acquired and validated, providing 7 provinces, 77 districts, and 775 third-level units with stable P-codes. Rasuwa, Nuwakot, and Dhading form the initial Nepal-side event-area crosswalk.
- Expanded event-window catalogue screening found 15 Sentinel-1 GRD scenes (12 pre-event and 3 post-event), including a directly comparable same-orbit pre/post combination from 16 and 28 August 2026, and 47 Sentinel-2 L2A scenes (41 pre-event and 6 post-event). The radar comparison is the primary change-detection input because all available post-event optical tiles have substantial cloud cover.
- The initial spatial baseline now includes a validated 2024 administrative release; a 25 August 2026 pre-event OpenStreetMap snapshot; a six-tile Copernicus DEM GLO-30 mosaic with elevation and slope; and four aligned Sentinel-1 RTC rasters at 20 m for VV/VH on 16 and 28 August. The radar processing window has complete valid-pixel coverage and two post-minus-pre dB screening layers, but neither raw backscatter change nor catalogue cloud metadata constitutes a validated hazard footprint.
- Pixel-level Sentinel-2 inputs now include aligned pre-event imagery from 12 August and post-event imagery from 27 August at 20 m, with blue, green, red, near-infrared, shortwave-infrared, scene-classification, and valid-pixel layers. The pre-event valid fraction is 85.9%, while the post-event valid fraction is only 27.1%; therefore optical change will be used for masked validation rather than as the primary footprint estimator.
- An independent UNOSAT preliminary mudflow/rockflow vector derived from 26 August PlanetScope and 27 August Sentinel-2 imagery has been acquired with its explicit analysis footprint. The resource geometry covers 37.354 km² and its analysis footprint covers 363.010 km²; UNOSAT states that it has not been field validated. A descriptive overlap check finds that 29.6% of affected-extent pixels have VH decreases of at least 2 dB, compared with 9.4% in analysed but unmapped areas, supporting radar screening while also demonstrating that a single change threshold is insufficient.
- The population baseline now combines a constrained 2024 population surface with official 2021 census totals. The modeled distribution was calibrated separately for Rasuwa, Nuwakot, and Dhading and yields 32 local-unit estimates that preserve the three official district totals; it remains a modeled exposure denominator rather than a casualty or displacement count.
- Reference hydrography and cryosphere context now cover 4,379 river reaches and 1,300 glacier polygons within the event-area context buffer. The glacier inventory approximates year-2000 conditions and therefore provides source-area context only, not a current glacier boundary or proof of the 2026 trigger.
- Current Copernicus emergency products provide rapid damage grades for buildings, roads, bridges, facilities, and observed-event areas in three mapped areas. A conservative spatial crosswalk links 700 of 706 graded road features and 18 of 32 bridge points to the pre-event road graph; unmatched features are retained rather than forced onto the graph, and the grades remain satellite interpretations rather than field-verified operating status.
- An official health-response update reports four fully damaged health facilities in Rasuwa, two partially damaged facilities in Dhading, and road-related loss of access to two hospitals in Dhading and Trishuli. These counts provide aggregate validation targets, but the published update does not identify facility records or route geometries for direct linkage.
- An independent rapid hazard assessment reports an ice-rock detachment source at 28.288708 N, 85.528159 E and references glacier RGI2000-v7.0-G-15-05732. The reported point lies approximately 42 m from that inventory polygon, strengthening location-level triangulation of the proposed event sequence but not establishing definitive event-specific climate attribution.
- Pre-event OSM overlay identifies 488 road features (130.73 km of line segments inside the reference polygon), 64 bridges, 9 settlements, 27 facilities, and 3,107 buildings intersecting the UNOSAT geometry. These counts describe potential exposure only and are not damage estimates.
- An exploratory undirected motor-road graph contains approximately 744 thousand nodes and 752 thousand segments. Under class-based travel speeds and a 3 km settlement-to-network snap rule, 609 of 767 mapped settlements are connected to at least one health or emergency facility in the baseline topology. Removing segments intersecting the preliminary event geometry isolates 29 previously reachable settlements and delays 52 others by more than five modeled minutes in a conservative facility-loss scenario.
- The pilot isolation result varies from 21 to 29 settlements as the maximum snap distance changes from 500 m to 3 km, corresponding to 3.9-4.8% of baseline-reachable settlements. However, 111 settlements are unreachable in the baseline graph and 47 are more than 3 km from retained motor roads. These topology gaps preclude treating the pilot travel times or isolation counts as final results and motivate explicit graph repair and scenario sensitivity analysis.

### Time-Series Candidates

Potential temporal structure was detected in 1789 variable records, including repeated survey waves and event-recall fields.
Time-series visualizations have not been generated pending explicit user confirmation.

### Data Limitations

- Survey modules are relational and their row counts are not additive; household, person, plot, event, and community files have different units of observation.
- Public NCCS 2022 district and ward values are constant zero and its latitude and longitude values are also zero; field names alone must not be interpreted as usable geocodes.
- Public-use geographic identifiers may be subject to disclosure restrictions and must be validated before household-level spatial outputs are released.
- Some local boundary layers use superseded administrative systems and require replacement or crosswalks to current administrative units.
- Existing surveys predate the 2026 disaster and cannot by themselves identify realized household impacts from that event without new follow-up outcomes.
- The event source mechanism, impact counts, and acquisition envelope remain provisional while official situation reports and scientific assessments continue to change.
- Catalogue-level optical cloud percentages do not measure cloud cover within the exact river corridor; pixel-level cloud and snow masks are required before interpreting surface change.
- Near-real-time precipitation remains unavailable in the reproducible project store because NASA access requires an authorized account, while the quality-controlled final product is not yet available because of product latency.
- Fourteen of 32 rapid-mapping bridge points are not linked to bridge-tagged road edges, and current road, bridge, and facility operating status still requires field or official situation-report validation.
- The calibrated population surface does not observe post-event displacement, and the public survey files still lack usable household coordinates for direct settlement-level linkage.
- Candidate screening is exploratory and does not constitute final variable selection or causal evidence.
- Technical source names, paths, and original variable names are retained only in the data-briefing artifacts.

## 4. Variable Construction  /  Key Variables

The table records the approved survey variables, road-network variables, and confirmed scenario-based hazard-evidence and exposure variables. Survey roles and unresolved formal definitions may be refined during estimation planning. Hazard-evidence classes express confidence in multi-source spatial evidence rather than physical intensity, and every exposure measure remains a scenario estimate rather than confirmed damage, casualties, or displacement.

| variable_name | full_name | role | formal_definition | construction_or_coding | is_final_variable |
|---|---|---|---|---|---|
| Sex of respondent | Sex of respondent | identifier and household context | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Age of respondent | Age of respondent | identifier and household context | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Caste/ethnicity of respondent | Caste/ethnicity of respondent | identifier and household context | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Highest level of edu. of respondent | Highest level of edu. of respondent | identifier and household context | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Years of living this community | Years of living this community | identifier and household context | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| No. of member usually stay | No. of member usually stay | identifier and household context | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Have membership in co-operative / saving groups | Have membership in co-operative / saving groups | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Have regular saving in cooperatives / saving groups | Have regular saving in cooperatives / saving groups | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Regular saving in financial institute/Bank | Regular saving in financial institute/Bank | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Loan taken from Money lender/saving group/co-operatives | Loan taken from Money lender/saving group/co-operatives | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Have involvement in community organisation | Have involvement in community organisation | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Affiliation in Tole Development committee | Affiliation in Tole Development committee | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Receive any service from agri. service center | Receive any service from agri. service center | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Distance to ward office (km) | Distance to ward office (km) | financial, social, and service-access capacity | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Distance to motorable road (km) | Distance to motorable road (km) | financial, social, and service-access capacity | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Distance to nearest health institution (km) | Distance to nearest health institution (km) | financial, social, and service-access capacity | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Distance to nearest basic school (km) | Distance to nearest basic school (km) | financial, social, and service-access capacity | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Distance to nearest local market (km) | Distance to nearest local market (km) | financial, social, and service-access capacity | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Distance to nearest Agr/livestock service center (km) | Distance to nearest Agr/livestock service center (km) | financial, social, and service-access capacity | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Modern Equip./machine used in agriculture | Modern Equip./machine used in agriculture | financial, social, and service-access capacity | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Heard about climate change | Heard about climate change | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Did you receive Pre-Warning information | Did you receive Pre-Warning information | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Main source of pre-warning information | Main source of pre-warning information | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Preparatory work done to protect from disaster | Preparatory work done to protect from disaster | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Type of preparatory work done to protect-1 | Type of preparatory work done to protect-1 | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Type of preparatory work done to protect-2 | Type of preparatory work done to protect-2 | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Type of preparatory work done to protect-3 | Type of preparatory work done to protect-3 | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Type of preparatory work done to protect-4 | Type of preparatory work done to protect-4 | warning and preparedness | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.01 Taking any related agri. adaptation training | K.01 Taking any related agri. adaptation training | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.16 Insurance made for livestock | K.16 Insurance made for livestock | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.19 Insurance made for agri. crops | K.19 Insurance made for agri. crops | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.31 Work on water and land conservation | K.31 Work on water and land conservation | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Any agri. services received from the local office | Any agri. services received from the local office | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.36 Work to minimize climatic induced disaster | K.36 Work to minimize climatic induced disaster | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.38 Behaviour change in food consumption | K.38 Behaviour change in food consumption | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.39 Increase non-agri. business locally | K.39 Increase non-agri. business locally | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.40 Shifted in non-agri. employment | K.40 Shifted in non-agri. employment | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.41 Having temporary out-migration | K.41 Having temporary out-migration | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.42 Participate in flood/landslide risk reduction activities | K.42 Participate in flood/landslide risk reduction activities | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.43 Participate in improvement of road infra | K.43 Participate in improvement of road infra | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.44 Participate in natural resource mgmt | K.44 Participate in natural resource mgmt | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| K.45 Participate in climate induced disaster risk reduction capacity improvement | K.45 Participate in climate induced disaster risk reduction capacity improvement | adaptation and risk reduction | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Altitude Group | Altitude Group | survey design, supported geography, and weight | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Risk Rating | Risk Rating | survey design, supported geography, and weight | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Urban Rural Classification | Urban Rural Classification | survey design, supported geography, and weight | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Ecological Belt | Ecological Belt | survey design, supported geography, and weight | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.16 Type of disaster incidence due to climate change | F.16 Type of disaster incidence due to climate change | historical disaster incidence and prevention | TBD | Retained as text with leading and trailing whitespace removed. | yes |
| F.17 Effect household from disaster incidence during 25 yrs | F.17 Effect household from disaster incidence during 25 yrs | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.18 How to effect family from disaster incidence | F.18 How to effect family from disaster incidence | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.19 Cause of disaster incidence - 1 | F.19 Cause of disaster incidence - 1 | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.19 Cause of disaster incidence - 2 | F.19 Cause of disaster incidence - 2 | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.19 Cause of disaster incidence - 3 | F.19 Cause of disaster incidence - 3 | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.20 Efforts made to prevent/minimize disaster events | F.20 Efforts made to prevent/minimize disaster events | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.20 Efforts made to prevent/minimize disaster events-2 | F.20 Efforts made to prevent/minimize disaster events-2 | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| F.20 Efforts made to prevent/minimize disaster events-3 | F.20 Efforts made to prevent/minimize disaster events-3 | historical disaster incidence and prevention | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| G.02 Type of disaster incidence | G.02 Type of disaster incidence | historical human and livelihood effects | TBD | Retained as text with leading and trailing whitespace removed. | yes |
| G.03 Years of facing disaster incidence | G.03 Years of facing disaster incidence | historical human and livelihood effects | TBD | Decoded from approved value labels and stored as string to preserve mixed labels. | yes |
| G.04 Family affect from disaster incidence | G.04 Family affect from disaster incidence | historical human and livelihood effects | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| G.05 Number of days missed to work | G.05 Number of days missed to work | historical human and livelihood effects | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.06 Family faced food scarcity | G.06 Family faced food scarcity | historical human and livelihood effects | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| G.07 Have family member disable | G.07 Have family member disable | historical human and livelihood effects | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| G.08 Have death of family member | G.08 Have death of family member | historical human and livelihood effects | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| G.16 Types of disaster incidence | G.16 Types of disaster incidence | historical monetary losses | TBD | Retained as text with leading and trailing whitespace removed. | yes |
| G.17 Household lost from disaster incidence | G.17 Household lost from disaster incidence | historical monetary losses | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| G.18 Loss in residential house/shelter etc. (Rs.) | G.18 Loss in residential house/shelter etc. (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.19 Loss in cereal crops (Rs.) | G.19 Loss in cereal crops (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.20 Loss in vegetable crops (Rs.) | G.20 Loss in vegetable crops (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.21 Loss in fruit crops (Rs.) | G.21 Loss in fruit crops (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Q.22 Loss in other crops (Rs.) | Q.22 Loss in other crops (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.23 Loss in livestock/poultry (Rs.) | G.23 Loss in livestock/poultry (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.24 Loss in garden/nursary land (Rs.) | G.24 Loss in garden/nursary land (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.25 Loss in productive land (Rs.) | G.25 Loss in productive land (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| G.26 Loss in other non-agri. business (Rs.) | G.26 Loss in other non-agri. business (Rs.) | historical monetary losses | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Analytical Domain | Analytical Domain | poverty, expenditure, and survey design | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Household size | Household size | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Urban/rural/ktm_urban | Urban/rural/ktm_urban | poverty, expenditure, and survey design | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Paasche index -- food items | Paasche index -- food items | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Per Capita Food Expenditure | Per Capita Food Expenditure | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Per Capita Nonfood Expenditure | Per Capita Nonfood Expenditure | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Per Capita Expenditure | Per Capita Expenditure | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| National Real Poverty Line (NPR/person/year) | National Real Poverty Line (NPR/person/year) | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| National Real Food Poverty Line (NPR/person/year) | National Real Food Poverty Line (NPR/person/year) | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| National Real Non-food Poverty Line (NPR/person/year) | National Real Non-food Poverty Line (NPR/person/year) | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Poverty Status | Poverty Status | poverty, expenditure, and survey design | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Expenditure quintile | Expenditure quintile | poverty, expenditure, and survey design | TBD | Decoded from approved value labels and stored as string to preserve mixed labels. | yes |
| Residential facility | Residential facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Clothing | Clothing | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Health care | Health care | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Childrens schooling | Childrens schooling | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Total income over the past one month | Total income over the past one month | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Health facility | Health facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Health facility (q17_06_b) | Health facility (q17_06_b) | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Education facilities | Education facilities | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Education facilities (q17_07_b) | Education facilities (q17_07_b) | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Drinking water facility | Drinking water facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Drinking water facility (q17_08_b) | Drinking water facility (q17_08_b) | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Electricity facility | Electricity facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Electricity facility (q17_09_b) | Electricity facility (q17_09_b) | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Road facility | Road facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Postal facility | Postal facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Postal facility (q17_11_b) | Postal facility (q17_11_b) | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Telephone facility | Telephone facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Telephone facility (q17_12_b) | Telephone facility (q17_12_b) | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Internet facility | Internet facility | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Internet facility (q17_13_b) | Internet facility (q17_13_b) | subjective welfare and service constraints | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| FACILITY DESCRIPTION | FACILITY DESCRIPTION | facility-specific travel and use | TBD | Retained as text with leading and trailing whitespace removed. | yes |
| How do you OR would you normally travel to the closest .. FACILITY | How do you OR would you normally travel to the closest .. FACILITY | facility-specific travel and use | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| How long does it take to get from your house to the closest .. FACILITY | How long does it take to get from your house to the closest .. FACILITY | facility-specific travel and use | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| HOURS | HOURS | facility-specific travel and use | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| MINUTES | MINUTES | facility-specific travel and use | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| How far is the closest FACILITY to this household | How far is the closest FACILITY to this household | facility-specific travel and use | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Have the members of this household used .. FACILITY .. during the past 12 | Have the members of this household used .. FACILITY .. during the past 12 | facility-specific travel and use | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Shock Type | Shock Type | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Decrease or loss of income or assets | Decrease or loss of income or assets | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| The monetary value of the loss (in Rupees) | The monetary value of the loss (in Rupees) | wave 2016 shock loss, assistance, and coping | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Number of months ago when this shock took place | Number of months ago when this shock took place | wave 2016 shock loss, assistance, and coping | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Spend savings, borrow money, sell or pawn properties | Spend savings, borrow money, sell or pawn properties | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Reduce consumption or expenditure on foods | Reduce consumption or expenditure on foods | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Reduce consumption or expenditures on non-food items | Reduce consumption or expenditures on non-food items | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Education of children affected by the shock | Education of children affected by the shock | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Received assistance or help from others | Received assistance or help from others | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Source of assistance Relatives | Source of assistance Relatives | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Source of assistance Friends/neighbors | Source of assistance Friends/neighbors | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Source of assistance Government | Source of assistance Government | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Source of assistance NGO/Church | Source of assistance NGO/Church | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Source of assistance Other | Source of assistance Other | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Type of assistance Cash | Type of assistance Cash | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Type of assistance In Kind (Food) | Type of assistance In Kind (Food) | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Type of assistance In Kind (Non Food) | Type of assistance In Kind (Non Food) | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| time taken to receive assistance | time taken to receive assistance | wave 2016 shock loss, assistance, and coping | TBD | Retained as text with leading and trailing whitespace removed. | yes |
| Look for work, got employed or worked more | Look for work, got employed or worked more | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Changes in your living arrangements or the number of household members | Changes in your living arrangements or the number of household members | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| First of the two main strategies adopted | First of the two main strategies adopted | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Second of the two main strategies adopted | Second of the two main strategies adopted | wave 2016 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| INGOs | INGOs | wave 2017 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| cash assistance amount | cash assistance amount | wave 2017 shock loss, assistance, and coping | TBD | Retained in the source scale with no imputation, clipping, or transformation. | yes |
| Who provided assistance | Who provided assistance | wave 2018 shock loss, assistance, and coping | TBD | Decoded from approved value labels and stored as a labelled category. | yes |
| Topology repair threshold (m) | Road-network topology repair threshold (m) | network robustness parameter | \(R \in \{0,5,10,20\}\), with \(R=5\) for the primary graph. | Join a dangling endpoint only to the nearest node in a different component when their separation is at most \(R\); reject connectors intersecting mapped waterways. The strict 0 m and alternative 10 m and 20 m graphs are robustness scenarios; the exploratory 50 m rule is excluded. | yes |
| Road edge travel time (minutes) | Modeled road-edge traversal time (minutes) | network cost | \(t_e=L_e/(v_e\times 1000/60)\), where \(L_e\) is edge length in metres and \(v_e\) is class-based speed in kilometres per hour. | Derived for every mapped road segment using the confirmed class-speed lookup. Accepted topology-repair connectors use a conservative speed of 10 km/h. | yes |
| Settlement-to-road snap distance (m) | Euclidean settlement-to-nearest-road-node distance (m) | network linkage and robustness parameter | \(d_s=\min_{n \in N}\operatorname{dist}(s,n)\). | The primary network linkage retains settlements with \(d_s\leq 3000\) m. Thresholds of 500 m, 1000 m, 2000 m, and 3000 m are retained for sensitivity analysis. | yes |
| Baseline health/emergency accessibility (minutes) | Modeled pre-event travel time to the nearest health or emergency facility (minutes) | accessibility outcome | \(A_s(R)=\min_{f \in F} \operatorname{dist}_{G(R)}(n_s,n_f)\), evaluated on topology scenario \(G(R)\). | Computed by multi-source shortest paths from health and emergency facility nodes. Values remain missing when a settlement is more than 3 km from the road graph or no service path exists. | yes |
| Baseline service reachable | Baseline reachability of a health or emergency facility | accessibility outcome | \(I_s(R)=1[A_s(R)<\infty \text{ and } d_s\leq 3000]\). | Boolean indicator calculated separately for the 0 m, 5 m, 10 m, and 20 m topology scenarios; no missing values are imputed. | yes |
| Surface Change | Event-window radar and optical surface-change evidence | hazard evidence | \(\Delta VH_p=VH_{p,post}-VH_{p,pre}\) and \(\Delta MNDWI_p=MNDWI_{p,post}-MNDWI_{p,pre}\). | Preserve signed post-minus-pre radar change. The primary radar decrease rule is \(\Delta VH_p\leq-2\) dB. Optical evidence requires valid pixels on both dates and \(\Delta MNDWI_p\geq0.15\). | yes |
| Terrain Slope | Terrain slope in degrees | terrain context | \(\theta_p=\operatorname{slope}(DEM_p)\). | Derived from the 30 m elevation surface and retained in degrees. Pixels with \(\theta_p\geq30\) degrees provide steep-terrain context but cannot create mapped hazard evidence by themselves. | yes |
| Channel Context | Proximity to the reference river network | flow-path context | \(C_p=1[d(p,R)\leq120]\), where \(R\) is the reference river network. | A 120 m river-network buffer supplies downstream flow-path context. It supports sensor screening but cannot create hazard evidence without a sensor signal. | yes |
| Flow Path | DEM-derived D8 flow path | flow-path context | TBD | Derive from a depression-filled elevation surface using the confirmed D8 rule. This output remains pending and will be used as an additional sensitivity layer rather than replacing the observed river network. | yes |
| Hazard Evidence Class | Multi-source hazard-evidence confidence class | hazard evidence and scenario assignment | \(H_p\in\{0,1,2,3\}\), with 255 reserved for NoData outside the analysis scope. | Class 1 requires at least one sensor signal plus channel or steep-slope context. Class 2 requires at least one rapid-mapping reference or both sensors plus context. Class 3 requires two rapid-mapping references or one mapped reference plus at least one sensor signal. The variable is not physical hazard intensity. | yes |
| Hazard Scenario | Nested hazard-evidence footprint scenario | robustness parameter | \(F_s(p)=1[H_p\geq s]\), for \(s\in\{3,2,1\}\). | The primary conservative, alternative mapped-or-multisensor, and sensitivity screening footprints use minimum evidence classes 3, 2, and 1, respectively. | yes |
| Footprint Area (sq km) | Scenario footprint area in square kilometres | exposure denominator | \(A_s=\sum_p F_s(p)a_p\), where \(a_p=0.0004\) sq km for a 20 m pixel. | Sum the area of all non-NoData pixels meeting each scenario threshold. | yes |
| Exposed Population | Modeled population inside a scenario footprint | exposure outcome | \(E_s=\sum_p P_pF_s(p)\). | Reproject calibrated gridded population counts to the 20 m evidence grid with area-conserving sum resampling, then sum within each nested footprint. This is neither a casualty nor a displacement estimate. | yes |
| Population Share of Analysis Scope (%) | Share of modeled analysis-scope population exposed under a scenario | exposure outcome | \(Q_s=100E_s/\sum_{p\in\mathcal{A}}P_p\). | Use the modeled population inside the analysis scope as the denominator; do not use the full three-district population total. | yes |
| Exposed Road Length (km) | Approximate road length intersecting a scenario footprint | infrastructure exposure outcome | \(L_s=\sum_j \ell_j1[H_{m_j}\geq s]\), where \(m_j\) is an interval midpoint. | Sample road lines at intervals no greater than 20 m and sum represented segment length where the sampled evidence class meets the scenario threshold. | yes |
| Exposed Building Count | Buildings intersecting a scenario footprint | infrastructure exposure outcome | \(B_s=\sum_b1[\max_{p\cap b\neq\emptyset}H_p\geq s]\). | Count a building when its geometry touches at least one footprint pixel meeting the scenario threshold. Intersection indicates exposure, not confirmed structural damage. | yes |
| Exposed Bridge Count | Bridges intersecting a scenario footprint | infrastructure exposure outcome | \(G_s=\sum_g1[\max_{p\cap g\neq\emptyset}H_p\geq s]\). | Count a bridge when its geometry touches at least one footprint pixel meeting the scenario threshold. Intersection indicates exposure, not confirmed bridge failure. | yes |
| Directly Exposed Facility Count | Facility points inside a scenario footprint | service exposure outcome | \(D_s^F=\sum_f1[H(f)\geq s]\). | Sample evidence class at each facility point. Report the separate count of facilities within 250 m of a qualifying pixel as proximity exposure rather than direct exposure. | yes |
| Directly Exposed Settlement Count | Settlement points inside a scenario footprint | settlement exposure outcome | \(D_s^S=\sum_i1[H(i)\geq s]\). | Sample evidence class at each settlement point. Report the separate count of settlements within 500 m of a qualifying pixel as proximity exposure rather than direct exposure. | yes |
| Disruption Candidate Edge Count | Evidence-linked graph edges intersecting a scenario footprint | network disruption input | \(K_s=\sum_e1[D_e=1]1[\max_{p\cap e\neq\emptyset}H_p\geq s]\). | Count graph edges carrying a rapid-mapping grade of possibly damaged, damaged, or destroyed when they intersect the scenario footprint. Multiple graph edges may represent one mapped road feature, so this is not a count of independently damaged roads. | yes |
| Road Closure Rule | Graded evidence-based road-closure assumption | network disruption and robustness parameter | \(Z_{e,c}=1[G_e\in\mathcal{C}_c]\), where \(\mathcal{C}_{primary}=\{Destroyed\}\) and \(\mathcal{C}_{robust}=\{Possibly\ damaged,Damaged,Destroyed\}\). | The primary analysis closes only graph edges graded Destroyed that intersect the selected hazard footprint. Robustness analysis closes every graded disruption-candidate edge intersecting the footprint. These are modeled assumptions, not field-confirmed closures. | yes |
| Facility Availability Rule | Scenario-specific health and emergency destination availability | service disruption and sensitivity parameter | \(F_c=F\) in the primary analysis; \(F_c=F\setminus F_c^{exposed}\) in facility-loss sensitivity analysis. | Retain all mapped health and emergency destinations in the primary road-disruption analysis. In sensitivity analysis only, remove destinations whose point location is directly exposed within the selected hazard footprint. Direct exposure is not treated as observed facility failure. | yes |
| Closed Edge Length (km) | Total modeled length of closed graph edges | network disruption diagnostic | \(L_c^{closed}=\sum_e \ell_e Z_{e,c}/1000\). | Sum the metric length of graph edges closed by the scenario-specific road-closure rule. Multiple graph edges may represent one mapped road feature. | yes |
| Removed Health/Emergency Destination Count | Number of service destinations excluded under a facility-loss scenario | service disruption diagnostic | \(N_c^{removed}=\lvert F\setminus F_c\rvert\). | Equal to zero in the primary analysis. In facility-loss sensitivity analysis, count directly exposed destination points removed from the multi-source shortest-path calculation. | yes |
| Post-Disruption Service Reachable | Modeled reachability of a health or emergency facility after disruption | accessibility outcome | \(I_{s,c}=1[A_{s,c}<\infty]\) for baseline-eligible settlements. | Evaluate reachability on the scenario-specific disrupted graph and available destination set. Preserve missing values for settlements that were ineligible or unreachable at baseline. | yes |
| Post-Disruption Travel Time (minutes) | Modeled post-event travel time to the nearest available health or emergency facility | accessibility outcome | \(A_{s,c}=\min_{f\in F_c}\operatorname{dist}_{G_c}(n_s,n_f)\). | Compute multi-source shortest paths on the disrupted graph after applying the road-closure and facility-availability rules. Preserve missing values for baseline-ineligible settlements and newly isolated settlements. | yes |
| Accessibility Loss (minutes) | Increase in modeled service travel time after disruption | accessibility outcome | \(\Delta A_{s,c}=A_{s,c}-A_s\) when both travel times are finite. | Calculate the finite travel-time increase for baseline-eligible settlements that remain reachable. Preserve missing values for baseline-ineligible or newly isolated settlements; represent isolation with separate indicators. | yes |
| Newly Isolated | Baseline-reachable settlement with no modeled service path after disruption | accessibility outcome | \(J_{s,c}=1[I_s=1\ \land\ I_{s,c}=0]\). | Assign true only when the settlement was service-reachable on the confirmed baseline graph but becomes unreachable under the disruption scenario. | yes |
| Accessibility Loss Is Infinite | Indicator that disruption changes finite baseline access to no available service path | accessibility outcome | \(Q_{s,c}=J_{s,c}\) for baseline-eligible settlements. | Assign true for newly isolated settlements, false for baseline-eligible settlements that remain reachable, and missing for baseline-ineligible settlements. | yes |
| Accessibility Status | Mutually exclusive modeled service-access outcome class | accessibility outcome and reporting category | \(S_{s,c}\in\{Baseline\ ineligible,Newly\ isolated,Delay>5\ min,Limited\ change\}\). | Classify settlements in order as baseline ineligible, newly isolated, delayed by more than 5 minutes, or limited change. The 5-minute threshold is a reporting rule and will be tested in sensitivity analysis. | yes |
| Population Allocation Threshold (m) | Maximum raster-cell-to-settlement assignment distance | population construction and sensitivity parameter | \(T\in\{500,1000,2000,3000\}\), with \(T=3000\) m for the primary analysis. | Apply nested distance thresholds after constraining every nearest-settlement search to the same third-level administrative allocation unit. | yes |
| Population Cell Assignment Distance (m) | Distance from a positive-population raster-cell centre to its nearest eligible settlement | population linkage diagnostic | \(r_p=\min_{s:u(s)=u(p)}d(p,s)\). | Calculate Euclidean distance in EPSG:32645. Leave the nearest settlement missing when the cell's allocation unit contains no mapped settlement. | yes |
| Estimated Settlement Population | Modeled pre-event population assigned to a settlement | population exposure and weighting variable | \(P_s(T)=\sum_p P_p1[u(p)=u(s)]1[s=\operatorname*{argmin}_{j:u(j)=u(p)}d(p,j)]1[r_p\leq T]\). | Assign each calibrated positive-population cell to no more than one nearest OSM settlement inside the same allocation unit. The primary value uses 3000 m and is not an observed settlement census. | yes |
| Has Assigned Population | Indicator that a settlement receives positive modeled population within the allocation threshold | population coverage diagnostic | \(B_s(T)=1[P_s(T)>0]\). | Assign true when at least one positive-population cell is allocated to the settlement under threshold \(T\); do not impute zero-population settlements. | yes |
| Unallocated Population | Calibrated population not assigned to any settlement under the selected threshold | population coverage diagnostic | \(U(T)=P_{scope}-\sum_sP_s(T)\). | Retain population beyond threshold \(T\), outside an eligible allocation unit, or inside an allocation unit with no mapped settlement as unallocated. Do not redistribute this residual. | yes |
| Newly Isolated Population | Modeled population assigned to settlements that become isolated | population-weighted accessibility outcome | \(N_c^{iso}=\sum_sP_s(3000)J_{s,c}\). | Sum primary-threshold settlement population where Newly Isolated is true. Unallocated population and baseline-ineligible settlements do not enter this total. | yes |
| Population Delayed over 5 Minutes | Modeled population assigned to settlements with finite accessibility loss above five minutes | population-weighted accessibility outcome | \(N_c^{delay}=\sum_sP_s(3000)1[\Delta A_{s,c}>5]\). | Sum primary-threshold settlement population among baseline-eligible settlements that remain reachable and exceed the reporting threshold. | yes |
| Population with Positive Accessibility Loss | Modeled population assigned to settlements with any positive finite travel-time increase | population-weighted accessibility outcome | \(N_c^{positive}=\sum_sP_s(3000)1[\Delta A_{s,c}>0]\). | Sum primary-threshold settlement population only where finite accessibility loss is positive. | yes |
| Population-Weighted Accessibility Loss (person-minutes) | Total modeled finite travel-time burden across assigned settlement population | population-weighted accessibility outcome | \(W_c=\sum_{s:\Delta A_{s,c}<\infty}P_s(3000)\Delta A_{s,c}\). | Multiply finite settlement-level accessibility loss by assigned population and sum. Newly isolated settlements are reported separately rather than assigned an arbitrary finite penalty. | yes |
| Population-Weighted Mean Finite Accessibility Loss (minutes) | Average modeled finite travel-time increase weighted by assigned settlement population | population-weighted accessibility outcome | \(\bar{A}_c^P=W_c/\sum_{s:\Delta A_{s,c}<\infty}P_s(3000)\). | Divide total person-minutes by assigned population with a finite post-disruption path. Interpret jointly with Newly Isolated Population. | yes |
| Economic Deprivation | Household poverty and income-inadequacy domain score | contextual social vulnerability component | \(D_{i,e}=(Poor_i+IncomeInadequate_i)/2\). | Code Poverty Status equal to one and income reported as less than adequate as higher vulnerability. Require both indicators; apply no missing-value imputation. | yes |
| Basic Needs Inadequacy | Household basic-needs inadequacy domain score | contextual social vulnerability component | \(D_{i,b}=\operatorname{mean}(Housing_i,Clothing_i,HealthCare_i,Schooling_i)\). | Code each response of less than adequate as one and just or more than adequate as zero. Treat not applicable as missing and require at least three valid indicators. | yes |
| Essential Public Service Deprivation | Household government-service deprivation domain score | contextual social vulnerability component | \(D_{i,s}=\operatorname{mean}(Health_i,Education_i,Water_i,Electricity_i,Road_i)\). | Use government-facility ratings only. Code Bad as one and Good or Fair as zero, treat not applicable as missing, and require at least three valid indicators. | yes |
| Weighted District Vulnerability Domain Estimate | Survey-weighted mean of a vulnerability domain within a district | supported-domain survey estimate | \(\hat{\mu}_{d,k}=\sum_{i\in d}w_iD_{i,k}/\sum_{i\in d}w_i\). | Link households to districts through the verified one-to-one PSU crosswalk and retain only positive household weights. Do not assign household values to settlements. | yes |
| District Vulnerability Domain Standard Error | PSU-clustered linearization standard error for a weighted district-domain estimate | survey uncertainty diagnostic | \(SE(\hat{\mu}_{d,k})=[m_d(m_d-1)^{-1}\sum_h z_h^2]^{1/2}\), where \(z_h=\sum_{i\in h}w_i(D_{i,k}-\hat{\mu}_{d,k})/\sum_{i\in d}w_i\). | Estimate uncertainty from between-PSU variation. Preserve missing uncertainty when a district has fewer than two PSUs. | yes |
| District Vulnerability Domain 95% CI | Cluster-adjusted uncertainty interval for a weighted district-domain estimate | survey uncertainty diagnostic | \(CI_{d,k}=\hat{\mu}_{d,k}\mathbin{+/-}t_{m_d-1,0.975}SE(\hat{\mu}_{d,k})\). | Use a t critical value based on PSU count and bound proportional-domain intervals to zero and one. Do not report a direct interval for Rasuwa because only one PSU is observed. | yes |
| Survey Effective Sample Size | Weight-adjusted effective number of observations | survey precision diagnostic | \(n_{eff}=(\sum_iw_i)^2/\sum_iw_i^2\). | Calculate separately for every reported domain and indicator using complete observations with positive weights. | yes |
| Survey Reliability Category | Qualitative support category based on independent survey clusters | evidence-strength diagnostic | TBD | Classify fewer than two PSUs as insufficient for design-based uncertainty, two to four as very limited, five to nine as limited, ten to twenty-nine as moderate, and thirty or more as broad contextual support. | yes |
| District Social Vulnerability Percentile | Equal-domain district vulnerability score before shrinkage | contextual vulnerability diagnostic | \(V_d=3^{-1}\sum_{k=1}^{3}R_{d,k}\), where \(R_{d,k}\) is the Bagmati district percentile of domain \(k\). | Orient every domain so higher values indicate greater vulnerability, percentile-scale across the thirteen Bagmati districts, and average the three domain percentiles equally. Exclude this score from the primary settlement ranking. | yes |
| Domain Shrinkage Weight | Empirical-Bayes reliability weight for a district-domain estimate | vulnerability sensitivity parameter | \(\lambda_{d,k}=\tau_k^2/(\tau_k^2+v_{d,k})\). | Estimate \(\tau_k^2\) as non-negative between-district variance after subtracting sampling variance; use the observed or PSU-count-adjusted sampling variance \(v_{d,k}\). Set the weight to zero when no between-district variance is resolvable. | yes |
| Shrinkage-Adjusted District Vulnerability Percentile | Equal-domain vulnerability percentile after reliability shrinkage | sensitivity-only contextual vulnerability | \(\widetilde{V}_d=3^{-1}\sum_{k=1}^{3}\widetilde{R}_{d,k}\), with \(\widetilde{\mu}_{d,k}=\lambda_{d,k}\hat{\mu}_{d,k}+(1-\lambda_{d,k})\mu_{Bagmati,k}\). | Shrink each domain toward its weighted Bagmati estimate before percentile scaling and equal-domain averaging. Use only as a sensitivity input, never as a measured settlement characteristic. | yes |
| Settlement Contextual Vulnerability (Sensitivity Only) | District vulnerability context attached to a settlement for sensitivity analysis | settlement-priority sensitivity input | \(V_s^{sens}=\widetilde{V}_{d(s)}\). | Repeat the shrinkage-adjusted district percentile for settlements located in that district. Label it explicitly as district context and exclude it from the primary settlement ranking. | yes |
| Pre-Warning Deficit | Share of households reporting no pre-warning information | supported-domain preparedness indicator | \(W_g=\sum_{i\in g}w_i1[Warning_i=No]/\sum_{i\in g}w_i\). | Estimate only for Bagmati ecological-belt reporting domains using NCCS survey weights and PSU-clustered uncertainty. Do not downscale to districts or settlements. | yes |
| Conditional Preparedness Deficit | Share of warned households reporting no preparatory action | supported-domain preparedness indicator | \(P_g=\sum_{i\in g,Warning_i=Yes}w_i1[Preparation_i=No]/\sum_{i\in g,Warning_i=Yes}w_i\). | Restrict the denominator to households that received pre-warning. Report the very small eligible sample and cluster count explicitly. | yes |
| Flood/Landslide Risk-Reduction Participation Deficit | Share of households reporting no flood or landslide risk-reduction participation | supported-domain preparedness indicator | \(R_g=\sum_{i\in g}w_i1[Participation_i=No]/\sum_{i\in g}w_i\). | Estimate only for supported Bagmati ecological-belt domains; higher values indicate weaker preparedness context. | yes |
| Historical Assistance Receipt | Weighted share of recorded historical shock episodes receiving assistance | supported-domain shock-response indicator | \(A_{d,t}^{hist}=\sum_jw_j1[Assistance_j=Yes]/\sum_jw_j\). | Estimate by observed HRVS district and survey year for all recorded shock episodes. Cluster uncertainty by household and do not fill the absent Rasuwa domain. | yes |
| Historical Food-Consumption Reduction Coping | Weighted share of recorded historical shock episodes involving reduced food consumption or expenditure | supported-domain harmful-coping indicator | \(C_{d,t}^{hist}=\sum_jw_j1[FoodReduction_j=Yes]/\sum_jw_j\). | Estimate by observed HRVS district and survey year for all recorded shock episodes. Treat as contextual historical evidence rather than a 2026 event outcome. | yes |

## 5. Identification Strategy

### Design Principle

The study uses descriptive triangulation, scenario-based network simulation, and multi-criteria decision analysis. Identification comes from an auditable sequence: independent event evidence defines nested hazard-evidence footprints; pre-event roads and services define the baseline network; pre-specified edge-closure and facility-availability rules define counterfactual disruption scenarios; calibrated population measures the modeled population represented by each settlement; and survey estimates describe vulnerability only at supported reporting domains. The framework identifies modeled exposure, access loss, and robust priority under stated assumptions. It does not identify a causal effect of climate change, a household-level impact of the 2026 event, or field-confirmed infrastructure failure.

### Units, Eligibility, and Comparisons

- The settlement is the unit for hazard proximity, population allocation, accessibility loss, and intervention-priority ranking.
- The road edge is the unit for disruption scenarios. Candidate road sections and repair benefits remain a planned extension because Section 4 does not yet contain final variables for Critical Road Section, Population Reconnected, or Restored Access after Repair.
- Households and shock episodes remain the units for survey estimation. Districts and province-by-ecological-belt domains are the supported reporting geographies; survey records are not assigned to settlement locations.
- The primary settlement-ranking population includes settlements that are baseline eligible, have positive Estimated Settlement Population, and show either scenario-consistent hazard proximity or a modeled accessibility change. Baseline-ineligible settlements are reported as a coverage limitation rather than assigned a zero access-loss score.

### Physical-Evidence Identification

Hazard Evidence Class is an evidence-confidence class, not a physical intensity measure. The primary conservative footprint uses class 3; class 2 and class 1 thresholds define alternative and sensitivity footprints. Surface Change, Terrain Slope, Channel Context, and independent mapped references establish convergence and disagreement. Flow Path remains a pending sensitivity input and cannot be cited as completed evidence. The Cascading-Hazard Evidence and Consensus Footprint figure and the Evidence Base and Validation Status and Hazard and Exposure Key Indicators tables provide this evidence.

### Network-Disruption Identification

The confirmed pre-event graph uses a 5 m topology-repair threshold and a 3 km settlement snap rule. The primary disruption scenario removes only edges graded Destroyed that intersect the primary conservative footprint and retains all health and emergency destinations. Robustness scenarios vary hazard threshold, road-closure rule, facility availability, topology repair, and settlement snap distance. Changes in Post-Disruption Travel Time, Newly Isolated, and Accessibility Loss are interpreted as consequences of the modeled network intervention, not as observed travel behavior.

### Survey-Evidence Identification

Economic Deprivation, Basic Needs Inadequacy, and Essential Public Service Deprivation are estimated with positive household weights and PSU-clustered uncertainty. District Social Vulnerability Percentile is excluded from the primary settlement ranking. Shrinkage-Adjusted District Vulnerability Percentile may enter only a sensitivity ranking as district context repeated across settlements; it is not a settlement-level measurement. Pre-Warning Deficit, Conditional Preparedness Deficit, and historical shock-response indicators remain separate supported-domain evidence and do not enter the settlement score.

### Interpretation Limits and Planned Outputs

The framework supports descriptive statements about where evidence converges, which settlements lose modeled road access, how much assigned population is associated with those changes, and whether priority ranks persist across assumptions. It cannot claim realized casualties, displacement, facility failure, household welfare loss, optimal cost effectiveness, or climate attribution. Section 8 can support the central settlement-priority question and the physical, access, vulnerability, and robustness supporting questions after its stale variable names are harmonized. It cannot yet support the road-repair benefit claim because the required repair-section variables are not final in Section 4.

## 6. Main Estimation Framework

### 6.1 Scenario Definition

Let a scenario be

\[
c=(h,z,f,r,t),
\]

where \(h\) is the minimum Hazard Evidence Class, \(z\) is the Road Closure Rule, \(f\) is the Facility Availability Rule, \(r\) is the Topology repair threshold (m), and \(t\) is the maximum Settlement-to-road snap distance (m). The primary scenario is

\[
c_0=(3,\text{Destroyed only},\text{Road disruption only},5,3000).
\]

The alternative scenario set uses \(h\in\{3,2,1\}\), both confirmed road-closure rules, both confirmed facility-availability rules, \(r\in\{0,5,10,20\}\), and \(t\in\{500,1000,2000,3000\}\). The primary result is always reported separately from robustness results.

### 6.2 Settlement Ranking Set

For settlement \(s\), let \(H_s\) be the maximum Hazard Evidence Class within 500 m, let \(P_s(3000)\) be Estimated Settlement Population under the primary allocation threshold, let \(J_{s,c}\) be Newly Isolated, and let \(\Delta A_{s,c}\) be Accessibility Loss (minutes). The scenario-specific ranking set is

\[
\mathcal{S}_c=\{s:BaselineEligible_s=1,\ P_s(3000)>0,\ H_s\geq h_c\ \lor\ J_{s,c}=1\ \lor\ \Delta A_{s,c}>0\}.
\]

This rule keeps direct or proximate hazard exposure and modeled network consequences in scope while excluding settlements for which disruption-induced access loss is not identified. Settlements outside \(\mathcal{S}_c\) remain in coverage and descriptive outputs.

### 6.3 Component Scaling

For any component \(x_s\) observed on \(\mathcal{S}_c\), define its tied midrank scaling as

\[
R_c(x_s)=\frac{rank_{mid,c}(x_s)-1}{n_c-1},
\]

where \(rank_{mid,c}(x_s)\) is the ascending tied midrank and \(n_c\) is the number of settlements in \(\mathcal{S}_c\). If \(n_c=1\), set \(R_c(x_s)=0.5\). Higher values always indicate greater priority.

The hazard and exposure components are

\[
H_{s,c}^{*}=R_c(H_s),\qquad E_{s,c}^{*}=R_c(P_s(3000)).
\]

The accessibility component preserves the qualitative difference between a finite delay and complete modeled isolation:

\[
A_{s,c}^{*}=\begin{cases}
1, & J_{s,c}=1,\\
rank_{+,c}(\Delta A_{s,c})/(n_{+,c}+1), & \Delta A_{s,c}>0\text{ and finite},\\
0, & \Delta A_{s,c}=0.
\end{cases}
\]

Here \(rank_{+,c}(\Delta A_{s,c})\) is the ascending tied rank among positive finite losses and \(n_{+,c}\) is the number of settlements with positive finite loss. Thus every newly isolated settlement receives a higher accessibility-severity value than every finite-delay settlement without assigning an arbitrary travel-time penalty to infinity.

### 6.4 Primary and Vulnerability-Sensitivity Priority Scores

The primary equal-weight settlement score is

\[
\Pi_{s,c}^{main}=\frac{H_{s,c}^{*}+E_{s,c}^{*}+A_{s,c}^{*}}{3}.
\]

The score uses only event-specific settlement evidence. The four-component expression in Section 2 remains a conceptual statement of possible contributing dimensions; the operational primary ranking is the three-component score above. Let \(V_s^{sens}\) be Settlement Contextual Vulnerability (Sensitivity Only), expressed as a district percentile from zero to 100, and define \(V_s^{*}=V_s^{sens}/100\). The vulnerability-sensitivity score is

\[
\Pi_{s,c}^{V}=\frac{H_{s,c}^{*}+E_{s,c}^{*}+A_{s,c}^{*}+V_s^{*}}{4}.
\]

The sensitivity score tests rank dependence on contextual vulnerability; it must not replace \(\Pi_{s,c}^{main}\) or be described as a measured settlement vulnerability score.

Priority Rank is the descending competition rank of \(\Pi_{s,c}^{main}\), with ties assigned the same rank. The same tie rule applies to every robustness score.

### 6.5 Weighting, Functional-Form, and Scenario Robustness

For component vector \(X_{s,c}\) and non-negative weights that sum to one, the general additive score is

\[
\Pi_{s,c}(w)=\sum_{k=1}^{K}w_kX_{s,c,k},\qquad \sum_{k=1}^{K}w_k=1.
\]

Here \(K=3\) for the primary component set and \(K=4\) when vulnerability context is included. Robustness includes equal weights, leave-one-component-out scores, one-component-emphasis scores assigning 0.5 to the emphasized component and sharing 0.5 equally across the others, and 10,000 reproducible random draws from \(Dirichlet(1,\ldots,1)\).

The multiplicative robustness score is

\[
\Pi_{s,c}^{geo}(w)=\prod_{k=1}^{K}(\epsilon+X_{s,c,k})^{w_k},
\]

where \(\epsilon=0.01\) prevents a zero component from mechanically setting the full score to zero. This score is a robustness diagnostic, not the primary estimand.

Across \(M\) retained scenario-weight specifications, top-ten selection frequency is

\[
F_s^{top10}=\frac{1}{M}\sum_{m=1}^{M}1[Rank_{s,m}\leq10].
\]

Rank Stability is summarized by \(F_s^{top10}\), median rank, interquartile rank range, and the 5th-95th percentile rank interval. The Priority-Rank Robustness Across Assumptions figure reports these distributions rather than one deterministic rank alone.

### 6.6 Population and Access-Loss Estimands

Each scenario reports Newly Isolated Settlements, Newly Isolated Population, Settlements Delayed over 5 Minutes, Population Delayed over 5 Minutes, Population with Positive Accessibility Loss, and Population-Weighted Accessibility Loss (person-minutes). Finite accessibility losses and newly isolated population are reported separately. Unallocated Population, baseline-ineligible settlements, and settlements without positive assigned population remain explicit coverage quantities rather than being silently treated as zero impact.

### 6.7 Deferred Road-Repair Framework

The Road-Repair Reconnection Benefits figure and Top 10 Priority Road Repairs table are not yet estimable from final Section 4 variables. Before those outputs are generated, data preprocessing must define Critical Road Section, Population Reconnected, Restored Access after Repair, candidate-section construction, and the repair simulation rule. Until then, the framework supports disruption prioritization but not repair-benefit ranking or cost-effectiveness claims.

## 7. Analytical Workflow

| step | variables used | formula or model used | generated figure or table title | claim evaluated | planned support status |
|---|---|---|---|---|---|
| 1. Audit source evidence and linkage | Surface Change, Terrain Slope, Channel Context, Flow Path, Survey Reliability Category | Evidence availability, validation, linkage, and limitation audit | Evidence Base and Validation Status | Required physical, network, population, and survey evidence is adequate for its stated role. | Partially supportable: Flow Path and road-repair variables remain pending. |
| 2. Construct nested hazard evidence | Surface Change, Terrain Slope, Channel Context, Hazard Evidence Class, Hazard Scenario | Evidence-class rules and scenario threshold \(h\) in Section 6.1 | Cascading-Hazard Evidence and Consensus Footprint; Hazard and Exposure Key Indicators | Independent mapped, radar, optical, and terrain evidence converges on a coherent event corridor. | Planned descriptive support; no causal or intensity claim. |
| 3. Measure physical and population exposure | Footprint Area (sq km), Exposed Population, Exposed Road Length (km), Exposed Building Count, Exposed Bridge Count, Directly Exposed Facility Count, Directly Exposed Settlement Count | Scenario overlay and exposure sums defined in Section 4 | Hazard and Exposure Key Indicators | The event corridor intersects population and critical infrastructure under nested evidence thresholds. | Planned descriptive support with exposure-not-damage limit. |
| 4. Establish baseline and disrupted access | Topology repair threshold (m), Settlement-to-road snap distance (m), Baseline health/emergency accessibility (minutes), Road Closure Rule, Facility Availability Rule, Post-Disruption Travel Time (minutes), Newly Isolated, Accessibility Loss (minutes) | Scenario \(c\) in Section 6.1 and shortest-path definitions in Section 4 | Road Disruption and Service-Access Loss; Accessibility and Isolation Scenarios | Candidate road disruptions generate finite delays or complete modeled service isolation. | Planned model-based support, conditional on topology and closure assumptions. |
| 5. Aggregate affected population | Estimated Settlement Population, Newly Isolated Population, Population Delayed over 5 Minutes, Population-Weighted Accessibility Loss (person-minutes), Unallocated Population | Population and access-loss estimands in Section 6.6 | Accessibility and Isolation Scenarios | Modeled network disruption affects a non-trivial assigned population. | Planned support with explicit 3 km allocation and coverage limits. |
| 6. Estimate contextual vulnerability | Economic Deprivation, Basic Needs Inadequacy, Essential Public Service Deprivation, Weighted District Vulnerability Domain Estimate, District Vulnerability Domain 95% CI, Survey Reliability Category, Pre-Warning Deficit, Historical Assistance Receipt, Historical Food-Consumption Reduction Coping | Survey-weighted means, PSU-clustered uncertainty, and empirical-Bayes shrinkage from Section 4 | Pre-Disaster Vulnerability Profile by Supported Domain; Pre-Disaster Vulnerability Dimensions | Survey evidence identifies interpretable vulnerability, preparedness, and coping dimensions at supported domains. | Planned partial support; Rasuwa uncertainty and HRVS coverage remain limited. |
| 7. Rank settlements under the primary framework | Hazard Evidence Class, Estimated Settlement Population, Newly Isolated, Accessibility Loss (minutes) | Ranking set and component scaling in Sections 6.2-6.3; \(\Pi_{s,c}^{main}\) in Section 6.4 | Settlement Exposure, Isolation, and Intervention Priority; Top 10 Priority Settlements | Event-specific evidence identifies settlements with high joint hazard, population, and access-loss priority. | Planned decision-support evidence, not a causal effect or welfare estimate. |
| 8. Test vulnerability sensitivity | Settlement Contextual Vulnerability (Sensitivity Only), Shrinkage-Adjusted District Vulnerability Percentile, Survey Reliability Category | \(\Pi_{s,c}^{V}\) in Section 6.4 | Settlement Exposure, Isolation, and Intervention Priority; Top 10 Priority Settlements | Priority conclusions are or are not sensitive to district vulnerability context. | Planned sensitivity evidence; cannot establish settlement-level vulnerability. |
| 9. Test rank robustness | Hazard Scenario, Road Closure Rule, Facility Availability Rule, Topology repair threshold (m), Population Allocation Threshold (m), Domain Shrinkage Weight | Additive, leave-one-out, emphasized, random-weight, multiplicative, and scenario specifications in Section 6.5 | Priority-Rank Robustness Across Assumptions | The same settlements remain high priority across plausible structural and weighting choices. | Planned; stability must be judged from rank distributions and top-ten frequency. |
| 10. Simulate road repairs | Closed Edge Length (km), Newly Isolated Population, Population-Weighted Accessibility Loss (person-minutes) | Deferred pending final repair-section and restoration variables in Section 6.7 | Road-Repair Reconnection Benefits; Top 10 Priority Road Repairs | Specific road repairs reconnect the most population and restore the most access. | Boundary-limited: return to data-preprocessing before estimation. |

### Evidence-Support Checkpoints

1. Accept the hazard-support claim only if the primary footprint is coherent across independent mapped and sensor evidence and conclusions remain directionally stable under class 2 and class 1 thresholds.
2. Accept the network-mechanism claim only if baseline routing is reproducible, modeled closures create plausible access changes, and results are not driven solely by one topology or snap-distance rule.
3. Accept the population-impact claim only with explicit reporting of Unallocated Population and baseline-ineligible settlements.
4. Accept the vulnerability-context claim only at supported survey geographies with uncertainty and reliability labels; do not interpret district context as settlement measurement.
5. Treat the central priority result as robust only when top-ten selection frequency and rank intervals show persistence across scenario, weight, and functional-form variations.
6. Treat road-repair prioritization as unsupported until Critical Road Section, Population Reconnected, and Restored Access after Repair are constructed and validated.

## 8. Figure and Table Plan

The confirmed output plan follows the evidence chain from event reconstruction through network disruption and contextual vulnerability to intervention priorities and robustness. Manuscript tables are intentionally compact. Complete settlement and road rankings will be retained as machine-readable supplementary outputs rather than reproduced as oversized tables.

### Figures

| title | what it expresses | figure type | subpanels | key variables | status |
|---|---|---|---:|---|---|
| Cascading-Hazard Evidence and Consensus Footprint | Assesses whether satellite, terrain, flow-path, and independent mapped evidence converge on a coherent cascading-hazard footprint. | map | 4 | Surface Change, Terrain Slope, Flow Path, Hazard Intensity Class | pending |
| Road Disruption and Service-Access Loss | Shows how candidate road disruptions translate the physical footprint into travel-time increases or complete service isolation. | map | 3 | Road edge travel time (minutes), Baseline health/emergency accessibility (minutes), Post-Disruption Travel Time, Accessibility Loss | pending |
| Settlement Exposure, Isolation, and Intervention Priority | Integrates physical exposure, population, modeled isolation, and contextual vulnerability to identify priority settlements. | map | 4 | Hazard Intensity Class, Exposed Population, Accessibility Loss, Social Vulnerability, Intervention Priority | pending |
| Pre-Disaster Vulnerability Profile by Supported Domain | Compares poverty, service deprivation, warning, preparedness, historical loss, assistance, and harmful coping only at survey-supported reporting domains. | heatmap and bar | 3 | Poverty Status, Per Capita Expenditure, Distance to nearest health institution (km), Did you receive Pre-Warning information, Preparatory work done to protect from disaster, The monetary value of the loss (in Rupees), Received assistance or help from others, Reduce consumption or expenditure on foods | pending |
| Road-Repair Reconnection Benefits | Identifies which candidate road repairs restore the most population and essential-service access. | map and bar | 2 | Critical Road Section, Population Reconnected, Restored Access after Repair, Road edge travel time (minutes) | pending |
| Priority-Rank Robustness Across Assumptions | Tests whether intervention priorities remain stable across topology, hazard, disruption, vulnerability, and weighting assumptions. | heatmap and line | 2 | Topology repair threshold (m), Priority Rank, Rank Stability, Intervention Priority | pending |

### Tables

| title | what it expresses | rows | columns | row meaning | column meaning | status |
|---|---|---:|---:|---|---|---|
| Evidence Base and Validation Status | Summarizes whether each required evidence layer is available, validated, linkable, and adequate for its intended research use. | 8 | 7 | One evidence layer or validation domain | Evidence type, period, coverage, linkage, validation status, principal limitation, analytical role | pending |
| Hazard and Exposure Key Indicators | Reports the compact set of physical-footprint, population, building, road, bridge, and facility exposure indicators needed to characterize the event corridor. | 6 | 7 | One exposure dimension | Footprint or exposed amount, unit, primary estimate, alternative estimate, difference, evidence status, interpretation | pending |
| Pre-Disaster Vulnerability Dimensions | Reports weighted, domain-supported summaries of the principal deprivation, preparedness, loss, assistance, and coping dimensions. | 8 | 7 | One vulnerability dimension | Indicator, supported domain, estimate, uncertainty interval, sample size, missingness, interpretation | pending |
| Accessibility and Isolation Scenarios | Compares the primary network-disruption result with the small set of pre-specified topology, snap-distance, and hazard scenarios. | 8 | 8 | One primary or robustness scenario | Scenario, topology rule, snap rule, reachable settlements, isolated settlements, affected population, travel-time change, interpretation | pending |
| Top 10 Priority Settlements | Presents a readable decision summary for the ten settlements with the strongest combined evidence for intervention. | 10 | 9 | One priority settlement | Settlement, hazard class, exposed population, accessibility loss, vulnerability, priority score, primary rank, rank stability, decision note | pending |
| Top 10 Priority Road Repairs | Presents a readable decision summary for the ten road repairs with the largest robust reconnection benefits. | 10 | 9 | One candidate road repair | Road section, road class, disruption evidence, repair length, settlements reconnected, population reconnected, time restored, rank stability, decision note | pending |

### Variable Coverage Warnings

⚠️ 警告：以下变量在 AnaSOP Section 4 中不存在或未标记为最终分析变量，建议返回 data-preprocessing 补充：

- Surface Change （用于 Cascading-Hazard Evidence and Consensus Footprint）
- Terrain Slope （用于 Cascading-Hazard Evidence and Consensus Footprint）
- Flow Path （用于 Cascading-Hazard Evidence and Consensus Footprint）
- Hazard Intensity Class （用于 Cascading-Hazard Evidence and Consensus Footprint、Settlement Exposure, Isolation, and Intervention Priority、Hazard and Exposure Key Indicators 及优先级表）
- Post-Disruption Travel Time （用于 Road Disruption and Service-Access Loss 及 Accessibility and Isolation Scenarios）
- Accessibility Loss （用于 Road Disruption and Service-Access Loss、Settlement Exposure, Isolation, and Intervention Priority、Accessibility and Isolation Scenarios 及 Top 10 Priority Settlements）
- Exposed Population （用于 Settlement Exposure, Isolation, and Intervention Priority、Hazard and Exposure Key Indicators 及优先级表）
- Social Vulnerability （用于 Settlement Exposure, Isolation, and Intervention Priority 及 Top 10 Priority Settlements）
- Intervention Priority （用于 Settlement Exposure, Isolation, and Intervention Priority、Priority-Rank Robustness Across Assumptions 及优先级表）
- Critical Road Section （用于 Road-Repair Reconnection Benefits 及 Top 10 Priority Road Repairs）
- Population Reconnected （用于 Road-Repair Reconnection Benefits 及 Top 10 Priority Road Repairs）
- Restored Access after Repair （用于 Road-Repair Reconnection Benefits 及 Top 10 Priority Road Repairs）
- Priority Rank （用于 Priority-Rank Robustness Across Assumptions 及优先级表）
- Rank Stability （用于 Priority-Rank Robustness Across Assumptions 及优先级表）
