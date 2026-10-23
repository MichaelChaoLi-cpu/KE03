#!/usr/bin/env python3
"""Reproduce closure evidence and diagnose matching without changing production data."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.features import shapes
from shapely.geometry import shape
from shapely import distance, intersection, length, union_all


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def normalize(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.sort_values('Edge ID').reset_index(drop=True).copy()
    for col in out.select_dtypes(include=['object', 'str', 'string']).columns:
        out[col] = out[col].astype('string')
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    out = root / 'Rev/docs/evidence/reviewer-4-comment-2'
    out.mkdir(parents=True, exist_ok=True)
    cross = load_module(root/'src/preprocessing/build_copernicus_road_damage_crosswalk.py', 'closure_crosswalk')
    hazard = load_module(root/'src/preprocessing/build_hazard_scenario_exposure.py', 'closure_hazard')
    paths = {
        'reference': root/cross.REFERENCE_RELATIVE,
        'edges': root/cross.EDGES_RELATIVE,
        'nodes': root/cross.NODES_RELATIVE,
        'saved_crosswalk': root/cross.OUTPUT_RELATIVE,
        'saved_damage_exposure': root/hazard.OUTPUT_DIR/'road_damage_scenario_exposure_preprocessed.parquet',
        'hazard': root/hazard.HAZARD,
        'crosswalk_code': root/'src/preprocessing/build_copernicus_road_damage_crosswalk.py',
        'hazard_code': root/'src/preprocessing/build_hazard_scenario_exposure.py',
        'scenario_code': root/'src/preprocessing/build_accessibility_robustness_grid.py',
    }
    input_hashes = {key: {'path': str(p.relative_to(root)), 'sha256': sha256(p)} for key,p in paths.items()}
    roads = gpd.read_file(paths['reference'], layer='roads').to_crs(cross.TARGET_CRS)
    bridges = gpd.read_file(paths['reference'], layer='bridges').to_crs(cross.TARGET_CRS)
    nodes = pd.read_parquet(paths['nodes'])
    edges = pd.read_parquet(paths['edges'])
    saved = pd.read_parquet(paths['saved_crosswalk'])
    saved_exposure = pd.read_parquet(paths['saved_damage_exposure'])
    assert not edges['Edge ID'].duplicated().any()
    assert not saved['Edge ID'].duplicated().any()
    assert not roads['CEMS Feature ID'].duplicated().any()
    assert not bridges['CEMS Feature ID'].duplicated().any()

    bounds = np.vstack([roads.total_bounds, bridges.total_bounds])
    xmin, ymin = bounds[:,:2].min(axis=0) - cross.SEARCH_MARGIN_M
    xmax, ymax = bounds[:,2:].max(axis=0) + cross.SEARCH_MARGIN_M
    candidate_nodes = nodes.loc[nodes['Easting (m)'].between(xmin,xmax) & nodes['Northing (m)'].between(ymin,ymax)]
    ids = set(candidate_nodes['Road node ID'])
    candidates = edges.loc[edges['From node ID'].isin(ids) | edges['To node ID'].isin(ids)]
    graph = cross.edge_geometry(candidates, nodes)
    coordinates = nodes.set_index('Road node ID')[['Easting (m)', 'Northing (m)']]
    starts = coordinates.reindex(edges['From node ID']).to_numpy()
    ends = coordinates.reindex(edges['To node ID']).to_numpy()
    assert np.isfinite(starts).all() and np.isfinite(ends).all()
    intersects_box = ((np.maximum(starts[:,0],ends[:,0])>=xmin)
                      & (np.minimum(starts[:,0],ends[:,0])<=xmax)
                      & (np.maximum(starts[:,1],ends[:,1])>=ymin)
                      & (np.minimum(starts[:,1],ends[:,1])<=ymax))
    missed_box_candidates = int((intersects_box & ~edges['Edge ID'].isin(graph['Edge ID']).to_numpy()).sum())
    assert missed_box_candidates == 0, 'Endpoint bounding-box prefilter needs further review'
    print(f'Candidate graph: {len(graph)} edges', flush=True)
    road_pairs = cross.road_matches(graph, roads)
    bridge_pairs = cross.bridge_matches(graph, bridges)
    pairs = pd.concat([road_pairs, bridge_pairs], ignore_index=True)
    actual_road_distances = distance(
        graph.set_index('Edge ID').geometry.reindex(road_pairs['Edge ID']).to_numpy(),
        roads.set_index('CEMS Feature ID').geometry.reindex(road_pairs['evidence_id']).to_numpy(),
    )
    assert np.all(actual_road_distances <= cross.ROAD_MATCH_TOLERANCE_M + 1e-6)
    road_pairs['Audit measured line distance (m)'] = actual_road_distances
    pairs = pd.concat([road_pairs, bridge_pairs], ignore_index=True)
    recomputed = cross.collapse_matches(pairs)
    pd.testing.assert_frame_equal(normalize(saved), normalize(recomputed)[saved.columns], check_dtype=False)
    pd.testing.assert_series_equal(
        pairs.groupby('Edge ID')['severity'].max().sort_index().astype(int),
        recomputed.set_index('Edge ID')['Damage Severity Order'].sort_index().astype(int),
        check_names=False,
    )
    print('Stored crosswalk reproduced exactly', flush=True)

    # Diagnostic counterfactual only: one CEMS bridge point -> nearest OSM bridge
    # segment(s), retaining exact-distance ties. Do not replace production output.
    preferred = graph.loc[graph['Is bridge']].copy()
    fallback = preferred.empty
    if fallback:
        preferred = graph
    reverse = gpd.sjoin_nearest(
        bridges, preferred, how='inner', max_distance=cross.BRIDGE_MATCH_TOLERANCE_M,
        distance_col='match_distance_m',
    )
    reverse['evidence_id'] = reverse['CEMS Feature ID']
    reverse['grade'] = reverse['Damage Grade']
    reverse['aoi'] = reverse['AOI']
    reverse['severity'] = reverse['grade'].map(cross.SEVERITY).fillna(-2)
    reverse['evidence_type'] = 'Copernicus bridge point'
    reverse['match_type'] = 'diagnostic CEMS point to nearest OSM bridge within 100 m'
    reverse_pairs = pd.DataFrame(reverse.drop(columns='geometry'))
    alternative = cross.collapse_matches(pd.concat([road_pairs, reverse_pairs], ignore_index=True))

    geom_ids = sorted(set(recomputed['Edge ID']) | set(alternative['Edge ID']))
    geometry = graph.set_index('Edge ID').loc[geom_ids].copy()
    with rasterio.open(paths['hazard']) as raster:
        classes = raster.read(1)
        transform = raster.transform
        assert raster.crs == graph.crs
    observed_classes = pd.Series([
        hazard.max_class_for_geometry(classes, transform, g) for g in geometry.geometry
    ], index=geom_ids).replace(hazard.OUTSIDE_ANALYSIS, pd.NA).astype('Int64')
    recomputed['Maximum Intersecting Evidence Class'] = recomputed['Edge ID'].map(observed_classes)
    alternative['Maximum Intersecting Evidence Class'] = alternative['Edge ID'].map(observed_classes)
    pd.testing.assert_series_equal(
        recomputed.set_index('Edge ID')['Maximum Intersecting Evidence Class'].sort_index(),
        saved_exposure.set_index('Edge ID')['Maximum Intersecting Evidence Class'].sort_index(),
        check_dtype=False,
    )
    print('Stored raster evidence classes reproduced exactly', flush=True)

    rules = {'Destroyed only': {'Destroyed'}, 'All disruption candidates': cross.DISRUPTION_GRADES}
    rows = []
    closed_ids = {}
    alt_closed_ids = {}
    for topology in (0,5,10,20):
        included = set(edges.loc[edges['Minimum topology repair threshold (m)']<=topology,'Edge ID'])
        for threshold in (3,2,1):
            for rule, grades in rules.items():
                def select(table):
                    mask = (table['Maximum Intersecting Evidence Class'].ge(threshold).fillna(False)
                            & table['CEMS Damage Grade'].isin(grades) & table['Edge ID'].isin(included))
                    return set(table.loc[mask,'Edge ID'].astype(int))
                current, alt = select(recomputed), select(alternative)
                key=(topology,threshold,rule);closed_ids[key]=current;alt_closed_ids[key]=alt
                total_length=edges.loc[edges['Edge ID'].isin(current),'Edge length (m)'].sum()
                rows.append({'topology_m':topology,'minimum_hazard_class':threshold,'closure_rule':rule,
                             'closed_edges':len(current),'closed_length_km':float(total_length/1000),
                             'closed_edge_ids_sha256':hashlib.sha256(','.join(map(str,sorted(current))).encode()).hexdigest(),
                             'diagnostic_bridge_reverse_closed_edges':len(alt),
                             'diagnostic_added_edges':len(alt-current),'diagnostic_removed_edges':len(current-alt)})
    closure_summary=pd.DataFrame(rows)
    primary=closed_ids[(5,3,'Destroyed only')]
    alt_primary=alt_closed_ids[(5,3,'Destroyed only')]
    lengths=edges.set_index('Edge ID')['Edge length (m)']
    mask=(classes>=3)&(classes!=hazard.OUTSIDE_ANALYSIS)
    footprint=union_all([shape(g) for g,v in shapes(mask.astype('uint8'),mask=mask,transform=transform) if v==1])
    primary_geoms=geometry.loc[sorted(primary)].geometry
    overlap=length(intersection(primary_geoms.to_numpy(),footprint))
    denom=length(primary_geoms.to_numpy())
    fractions=np.divide(overlap,denom,out=np.zeros_like(overlap),where=denom>0)
    partial=(overlap>1e-6)&(overlap<denom-1e-6)
    edge_detail=recomputed.merge(edges[['Edge ID','From node ID','To node ID','Edge length (m)',
                                      'Minimum topology repair threshold (m)']],on='Edge ID',validate='one_to_one')
    edge_detail['Primary closed']=edge_detail['Edge ID'].isin(primary)
    edge_detail['Diagnostic reverse primary closed']=edge_detail['Edge ID'].isin(alt_primary)
    edge_detail['Class3 overlap length (m)']=edge_detail['Edge ID'].map(dict(zip(primary_geoms.index,overlap)))
    measured = pd.concat([
        road_pairs[['Edge ID','Audit measured line distance (m)']].rename(columns={'Audit measured line distance (m)':'distance'}),
        bridge_pairs[['Edge ID','match_distance_m']].rename(columns={'match_distance_m':'distance'}),
    ],ignore_index=True).groupby('Edge ID')['distance'].min()
    edge_detail['Audit measured minimum reference distance (m)']=edge_detail['Edge ID'].map(measured)
    most_severe=pairs.loc[pairs['severity'].eq(pairs.groupby('Edge ID')['severity'].transform('max'))]
    defining=most_severe.groupby('Edge ID')['evidence_id'].agg(lambda x:';'.join(sorted(set(x))))
    edge_detail['Grade-defining CEMS Feature IDs']=edge_detail['Edge ID'].map(defining)
    changed=sorted(primary ^ alt_primary)
    changed_detail=edges.loc[edges['Edge ID'].isin(changed)].copy()
    for col in ['CEMS Damage Grade','CEMS Feature IDs','CEMS Evidence Type']:
        changed_detail['Current '+col]=changed_detail['Edge ID'].map(recomputed.set_index('Edge ID')[col])
        changed_detail['Diagnostic '+col]=changed_detail['Edge ID'].map(alternative.set_index('Edge ID')[col])
    changed_detail['Current primary closed']=changed_detail['Edge ID'].isin(primary)
    changed_detail['Diagnostic primary closed']=changed_detail['Edge ID'].isin(alt_primary)

    source_rows=[]
    for label,frame,matched in [('roads',roads,road_pairs),('bridges',bridges,bridge_pairs)]:
        counts=matched.groupby('evidence_id')['Edge ID'].nunique()
        source=frame.drop(columns='geometry').copy();source['Evidence layer']=label
        source['Matched graph edges']=source['CEMS Feature ID'].map(counts).fillna(0).astype(int)
        source_rows.append(source)
    source_detail=pd.concat(source_rows,ignore_index=True)
    pairs.drop(columns=[c for c in ['geometry'] if c in pairs]).to_parquet(out/'current-evidence-edge-pairs.parquet',index=False)
    reverse_pairs.to_parquet(out/'diagnostic-bridge-point-first-pairs.parquet',index=False)
    edge_detail.to_parquet(out/'current-edge-closure-evidence.parquet',index=False)
    changed_detail.to_parquet(out/'diagnostic-primary-closure-differences.parquet',index=False)
    source_detail.to_parquet(out/'source-feature-coverage.parquet',index=False)
    closure_summary.to_parquet(out/'closure-rule-summary.parquet',index=False)

    current_bridge_min=bridge_pairs.groupby('evidence_id')['match_distance_m'].min()
    too_far=bridge_pairs['match_distance_m'] > bridge_pairs['evidence_id'].map(current_bridge_min)+1e-7
    report={
        'schema':'ke03-road-closure-evidence-audit/v1','inputs':input_hashes,
        'production_outputs_modified':False,'crosswalk_reproduction':'exact','raster_class_reproduction':'exact',
        'candidate_nodes':len(candidate_nodes),'candidate_edges':len(graph),'matched_graph_edges':len(recomputed),
        'omitted_edges_crossing_candidate_search_box':missed_box_candidates,
        'source_road_features':len(roads),'source_bridge_features':len(bridges),
        'matched_road_features':int(road_pairs['evidence_id'].nunique()),
        'matched_bridge_features':int(bridge_pairs['evidence_id'].nunique()),
        'road_pairs':len(road_pairs),'bridge_pairs':len(bridge_pairs),
        'road_pairs_with_nonzero_measured_distance':int((actual_road_distances>1e-6).sum()),
        'maximum_measured_road_match_distance_m':float(actual_road_distances.max()),
        'road_distance_metadata_note':'Production road match_distance_m is a zero placeholder for buffer intersection, not a measured line distance; audit values are computed separately.',
        'duplicate_evidence_edge_pairs':int(pairs.duplicated(['Edge ID','evidence_type','evidence_id']).sum()),
        'edges_with_multiple_source_features':int(pairs.groupby('Edge ID')['evidence_id'].nunique().gt(1).sum()),
        'edges_with_multiple_distinct_source_grades':int(pairs.groupby('Edge ID')['grade'].nunique().gt(1).sum()),
        'bridge_matching_direction': 'each OSM bridge edge to its nearest CEMS bridge point within 100 m',
        'bridge_fallback_used':fallback,
        'current_bridge_pairs_not_nearest_from_evidence_point':int(too_far.sum()),
        'diagnostic_point_first_bridge_pairs':len(reverse_pairs),
        'diagnostic_point_first_matched_bridge_features':int(reverse_pairs['evidence_id'].nunique()),
        'primary_current_closed_edges':len(primary),'primary_diagnostic_closed_edges':len(alt_primary),
        'primary_diagnostic_added_edges':sorted(alt_primary-primary),'primary_diagnostic_removed_edges':sorted(primary-alt_primary),
        'primary_diagnostic_symmetric_difference_km':float(lengths.reindex(changed).sum()/1000),
        'all_tested_bridge_direction_closure_sets_identical':all(closed_ids[k]==alt_closed_ids[k] for k in closed_ids),
        'primary_closed_full_length_km':float(denom.sum()/1000),
        'primary_closed_class3_overlap_length_km':float(overlap.sum()/1000),
        'primary_partially_intersecting_closed_edges':int(partial.sum()),
        'primary_closed_edges_zero_positive_overlap':int((overlap<=1e-6).sum()),
        'primary_overlap_fraction_quantiles':{str(q):float(np.quantile(fractions,q)) for q in (0,.25,.5,.75,1)},
        'closure_summary':rows,
        'interpretation_boundary':'Bridge reversal is a diagnostic comparison, not an approved production-rule correction. No routing, population outcomes or new manuscript prose is updated.',
    }
    for key,item in input_hashes.items():
        assert sha256(paths[key])==item['sha256'],key
    (out/'audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in {'inputs','closure_summary'}},ensure_ascii=False,indent=2),flush=True)
    print(closure_summary.query('topology_m == 5').to_string(index=False),flush=True)


if __name__=='__main__':
    main()
