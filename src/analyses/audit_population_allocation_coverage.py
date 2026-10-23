#!/usr/bin/env python3
"""Read-only-production audit of cell allocation, population conservation and coverage."""
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
from rasterio.features import rasterize
from pyproj import Transformer
from shapely import points
from shapely.strtree import STRtree


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path.cwd())
    root=parser.parse_args().root.resolve()
    out=root/'Rev/docs/evidence/reviewer-4-comment-3'
    out.mkdir(parents=True,exist_ok=True)
    code=root/'src/preprocessing/build_settlement_population_allocation.py'
    spec=importlib.util.spec_from_file_location('allocation',code)
    allocation=importlib.util.module_from_spec(spec);spec.loader.exec_module(allocation)
    rank_spec=importlib.util.spec_from_file_location('priority_audit',root/'src/preprocessing/build_settlement_priority_metrics.py')
    ranking=importlib.util.module_from_spec(rank_spec);rank_spec.loader.exec_module(ranking)
    popdir=root/allocation.OUTPUT_DIR
    paths={
        'allocation_code':code,'priority_code':root/'src/preprocessing/build_settlement_priority_metrics.py',
        'raster':root/allocation.POPULATION_RASTER,'admin':root/allocation.ADMIN_SOURCE,'osm':root/allocation.OSM_SOURCE,
        'cells':popdir/'population_cell_settlement_crosswalk_preprocessed.parquet',
        'sensitivity':popdir/'settlement_population_allocation_sensitivity_preprocessed.parquet',
        'threshold_summary':popdir/'population_allocation_threshold_summary_preprocessed.parquet',
        'primary_priority':root/'data/processed/decision/settlement_intervention_priority_preprocessed.parquet',
        'allocation_priority':root/'data/processed/decision/settlement_priority_population_allocation_sensitivity_preprocessed.parquet',
    }
    inputs={k:{'path':str(p.relative_to(root)),'sha256':sha(p)} for k,p in paths.items()}
    cells=pd.read_parquet(paths['cells']);sens=pd.read_parquet(paths['sensitivity'])
    summary=pd.read_parquet(paths['threshold_summary']);priority=pd.read_parquet(paths['primary_priority'])
    ranks=pd.read_parquet(paths['allocation_priority'])
    assert not cells['Population Cell ID'].duplicated().any()
    assert not sens.duplicated(['OSM Settlement ID','Allocation Threshold (m)']).any()
    units=gpd.read_file(paths['admin'],layer='local_units')
    districts=gpd.read_file(paths['admin'],layer='districts')
    settlements=allocation.assign_settlement_admin(gpd.read_file(paths['osm'],layer='settlements'),units,districts)
    metric=settlements.to_crs(allocation.METRIC_CRS).reset_index(drop=True)
    sid=metric['osm_id'].astype(str).to_numpy()
    with rasterio.open(paths['raster']) as r:
        v=r.read(1);valid=np.isfinite(v)&(v>0)
        if r.nodata is not None:valid&=v!=r.nodata
        rr,cc=np.nonzero(valid);pop=v[rr,cc].astype(float)
        unit_grid=rasterize(((g,i) for i,g in enumerate(units.to_crs(r.crs).geometry)),out_shape=v.shape,transform=r.transform,fill=-1,dtype='int16',all_touched=False)
        ui=unit_grid[rr,cc]
        lon,lat=rasterio.transform.xy(r.transform,rr,cc)
        x,y=Transformer.from_crs(r.crs,allocation.METRIC_CRS,always_xy=True).transform(lon,lat)
        assert np.array_equal(cells['Population Cell ID'],rr.astype('int64')*v.shape[1]+cc)
        assert np.array_equal(cells['Calibrated Population'],pop)
    xy=np.column_stack((x,y));near=np.full(len(pop),-1,dtype=int);distance=np.full(len(pop),np.inf)
    ties=np.zeros(len(pop),dtype=int);counts={t:np.zeros(len(pop),dtype=int) for t in allocation.THRESHOLDS_M}
    for i,u in units.iterrows():
        pi=np.flatnonzero(ui==i);si=np.flatnonzero(metric['adm3_pcode'].to_numpy()==u['adm3_pcode'])
        if not len(pi) or not len(si):continue
        tree=STRtree(metric.geometry.iloc[si].to_numpy());pg=points(xy[pi])
        pair,dist=tree.query_nearest(pg,all_matches=False,return_distance=True)
        near[pi[pair[0]]]=si[pair[1]];distance[pi[pair[0]]]=dist
        all_pair=tree.query_nearest(pg,all_matches=True)
        ties[pi]=np.bincount(all_pair[0],minlength=len(pi))
        for t in counts:
            matches=tree.query(pg,predicate='dwithin',distance=t)
            counts[t][pi]=np.bincount(matches[0],minlength=len(pi))
    expected=np.full(len(pop),'',dtype=object);has=near>=0;expected[has]=sid[near[has]]
    assert np.array_equal(cells['Nearest OSM Settlement ID'].fillna('').astype(str),expected)
    assert np.allclose(cells['Nearest Settlement Distance (m)'].fillna(np.inf),distance,rtol=0,atol=1e-7)
    expected_codes=np.full(len(pop),'',dtype=object);inside=ui>=0
    expected_codes[inside]=units['adm3_pcode'].to_numpy()[ui[inside]]
    assert np.array_equal(cells['Local Unit P-Code'].fillna('').astype(str),expected_codes)
    global_pairs,global_distances=STRtree(metric.geometry.to_numpy()).query_nearest(points(xy),all_matches=False,return_distance=True)
    global_dist=np.full(len(pop),np.inf);global_dist[global_pairs[0]]=global_distances
    global_candidates={t:(global_dist<=t) for t in allocation.THRESHOLDS_M}
    local_rows=[];threshold_rows=[];coverage_rows=[];cross_rows=[]
    pop_lookup=priority.set_index('OSM Settlement ID')['Estimated Settlement Population']
    primary_ids=set(priority.loc[priority['Priority Rank'].le(10).fillna(False),'OSM Settlement ID'])
    primary_access=priority.set_index('OSM Settlement ID')
    for t in allocation.THRESHOLDS_M:
        allocated=has&(distance<=t)
        sums=np.bincount(near[allocated],weights=pop[allocated],minlength=len(metric))
        group=sens.loc[sens['Allocation Threshold (m)'].eq(t)].set_index('OSM Settlement ID').reindex(sid)
        assert np.allclose(sums,group['Estimated Settlement Population'],rtol=0,atol=1e-7)
        assert int(allocated.sum())==int(group['Allocated Population Cell Count'].sum())
        s=summary.loc[summary['Allocation Threshold (m)'].eq(t)].iloc[0]
        assert np.isclose(pop[allocated].sum(),s['Allocated Settlement Population'],rtol=0,atol=1e-6)
        assert np.isclose(pop[~allocated].sum(),s['Unallocated Population'],rtol=0,atol=1e-6)
        if t==3000:assert np.array_equal(allocated,cells['Allocated within 3000 m'])
        reasons=np.select([~inside,~has,distance>t],['outside local units','no settlement in same local unit','beyond same-unit distance threshold'],default='allocated')
        for label in np.unique(reasons):
            mask=reasons==label
            cross_rows.append({'Threshold (m)':t,'Allocation status':label,'Cell count':int(mask.sum()),'Population':float(pop[mask].sum()),'Population with any settlement within threshold across units':float(pop[mask&global_candidates[t]].sum())})
        for i,u in units.iterrows():
            pm=ui==i;sm=metric['adm3_pcode'].to_numpy()==u['adm3_pcode']
            assigned=float(sums[sm].sum());unassigned=float(pop[pm&~allocated].sum());total=float(pop[pm].sum())
            assert abs(total-assigned-unassigned)<1e-6
            local_rows.append({'Threshold (m)':t,'Local Unit P-Code':u['adm3_pcode'],'Input Population':total,'Assigned Population':assigned,'Unassigned Population':unassigned,'Residual':total-assigned-unassigned})
        access=primary_access.reindex(sid);rank=ranks.loc[ranks['Allocation Threshold (m)'].eq(t)].set_index('OSM Settlement ID').reindex(sid)
        eligible=access['Baseline Eligible'].to_numpy(dtype=bool);snap=access['Settlement-to-Road Snap Distance (m)'].to_numpy(float)
        disjoint=np.select([snap>3000,~eligible],['beyond 3 km road snap','baseline unreachable within road snap'],default='baseline eligible')
        for label in np.unique(disjoint):
            mask=disjoint==label;coverage_rows.append({'Threshold (m)':t,'Coverage group':label,'Settlement count':int(mask.sum()),'Assigned Population':float(sums[mask].sum()),'Settlements without assigned population':int((mask&(sums==0)).sum())})
        isolated=access['Newly Isolated'].fillna(False).to_numpy(bool)
        included=eligible&(sums>0)&(access['Maximum Evidence Class within 500 m'].ge(access['Minimum Evidence Class']).fillna(False).to_numpy(bool)|isolated|access['Accessibility Loss (minutes)'].fillna(0).gt(0).to_numpy())
        assert np.array_equal(included,rank['Included in Priority Ranking'])
        assert rank.loc[~included,'Priority Rank'].isna().all()
        scored=ranking.score_priority_frame(rank.reset_index())
        for col in ['Included in Priority Ranking','Priority Rank','Intervention Priority','Hazard Priority Component','Exposure Priority Component','Accessibility Priority Component']:
            pd.testing.assert_series_equal(scored[col].reset_index(drop=True),rank[col].reset_index(drop=True),check_dtype=False,check_names=False,rtol=0,atol=1e-12)
        top=set(rank.loc[rank['Priority Rank'].le(10).fillna(False)].index)
        threshold_rows.append({'Threshold (m)':t,'Assigned Population':float(pop[allocated].sum()),'Unassigned Population':float(pop[~allocated].sum()),'Assigned Share (%)':float(100*pop[allocated].sum()/pop.sum()),'Cells with multiple same-unit settlements within threshold':int((counts[t]>1).sum()),'Priority eligible settlements':int(included.sum()),'Population in priority ranking':float(sums[included].sum()),'Top-10 set size':len(top),'Top-10 retained from primary':len(top&primary_ids),'Newly Isolated Population':float(sums[isolated].sum()),'Population Delayed over 5 Minutes':float(sums[access['Accessibility Status'].eq('delay over 5 minutes').fillna(False).to_numpy(bool)].sum())})
    assert np.allclose(pop_lookup.reindex(sid),sums,rtol=0,atol=1e-7)
    pd.DataFrame(local_rows).to_parquet(out/'local-unit-conservation.parquet',index=False)
    pd.DataFrame(coverage_rows).to_parquet(out/'baseline-coverage-partition.parquet',index=False)
    pd.DataFrame(cross_rows).to_parquet(out/'unallocated-reasons.parquet',index=False)
    pd.DataFrame(threshold_rows).to_parquet(out/'threshold-coverage-and-ranks.parquet',index=False)
    diagnostic=cells.copy();diagnostic['Nearest exact tie count']=ties
    diagnostic['Same-unit settlements within 3000 m']=counts[3000]
    diagnostic['Any settlement within 3000 m ignoring unit']=global_candidates[3000]
    diagnostic.to_parquet(out/'cell-allocation-audit.parquet',index=False)
    assert all(sha(paths[k])==v['sha256'] for k,v in inputs.items())
    report={'inputs':inputs,'production_outputs_modified':False,'cell_crosswalk_reproduction':'exact IDs/population; distance tolerance 1e-7 m','settlement_aggregation_reproduction':'all four thresholds within 1e-7 persons','total_population':float(pop.sum()),'positive_cells':len(pop),'duplicate_cell_ids':0,'nearest_exact_tie_cells':int((ties>1).sum()),'local_units_without_settlements':int(sum(not (metric['adm3_pcode']==u).any() for u in units['adm3_pcode'])),'threshold_summary':threshold_rows,'baseline_coverage_partition':coverage_rows,'unallocated_reasons':cross_rows,'maximum_local_conservation_residual':max(abs(r['Residual']) for r in local_rows),'shortest_paths_recomputed':False,'scores_recomputed':'all four allocation frames in memory; inclusion, components, score and rank match saved outputs','note':'Coverage diagnostics and aggregates from fixed primary paths; global-nearest comparison is diagnostic only, not a changed allocation rule.'}
    (out/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='inputs'},indent=2))


if __name__=='__main__':main()
