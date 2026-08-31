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
- An independent UNOSAT preliminary mudflow/rockflow vector derived from 26 August PlanetScope and 27 August Sentinel-2 imagery has been acquired with its explicit analysis footprint. The resource geometry covers 37.354 km² and its analysis footprint covers 363.010 km²; UNOSAT states that it has not been field validated. A descriptive overlap check finds that 29.6% of affected-extent pixels have VH decreases of at least 2 dB, compared with 9.4% in analysed but unmapped areas, supporting radar screening while also demonstrating that a single change threshold is insufficient.
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
- Candidate screening is exploratory and does not constitute final variable selection or causal evidence.
- Technical source names, paths, and original variable names are retained only in the data-briefing artifacts.

## 4. Variable Construction  /  Key Variables

The table records the approved initial survey variables. Roles and formal definitions may be refined after spatial data acquisition and figure-table planning.

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
