#!/usr/bin/env python3
"""Recompute graph, component and settlement states without changing production outputs."""
from __future__ import annotations

import argparse,gc,hashlib,heapq,importlib.util,json,time
from pathlib import Path
import numpy as np
import pandas as pd


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def file_sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''):h.update(c)
    return h.hexdigest()


def fingerprint(*arrays):
    h=hashlib.sha256()
    for a in arrays:
        a=np.asarray(a)
        if a.dtype.kind=='f':a=np.nan_to_num(np.round(a,8),nan=-1e300,posinf=1e300,neginf=-1e300)
        h.update(str(a.shape).encode());h.update(a.tobytes())
    return h.hexdigest()


def components(adjacency,closed):
    labels=np.full(len(adjacency),-1,dtype=np.int64);count=0
    for start in range(len(adjacency)):
        if labels[start]>=0:continue
        count+=1;labels[start]=start;stack=[start]
        while stack:
            u=stack.pop()
            for v,_,e in adjacency[u]:
                if not closed[e] and labels[v]<0:labels[v]=start;stack.append(v)
    return labels,count


def paths(adjacency,sources,closed):
    n=len(adjacency);d=np.full(n,np.inf);parent=np.full(n,-1,dtype=np.int64);pe=np.full(n,-1,dtype=np.int64)
    q=[]
    for s in sources:d[s]=0.;heapq.heappush(q,(0.,s))
    while q:
        du,u=heapq.heappop(q)
        if du!=d[u]:continue
        for v,c,e in adjacency[u]:
            if closed[e]:continue
            cand=du+c
            if cand<d[v]:d[v]=cand;parent[v]=u;pe[v]=e;heapq.heappush(q,(cand,v))
    return d,parent,pe


def witness_edges(nodes,parent,pe):
    visited=set();used=set()
    for n in nodes:
        n=int(n)
        while n>=0 and n not in visited:
            visited.add(n)
            if pe[n]<0:break
            used.add(int(pe[n]));n=int(parent[n])
    return used


def equal_numeric(a,b,atol=1e-8):
    return np.allclose(np.asarray(a,dtype=float),np.asarray(b,dtype=float),rtol=0,atol=atol,equal_nan=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path.cwd());root=ap.parse_args().root.resolve()
    out=root/'Rev/docs/evidence/reviewer-4-comment-7';out.mkdir(parents=True,exist_ok=True)
    prod=load(root/'src/preprocessing/build_accessibility_robustness_grid.py','structural_prod')
    oldaudit=load(root/'src/analyses/structural_scenario_factor_activity.py','old_factor')
    net=root/prod.NETWORK_DIR;exp=root/prod.EXPOSURE_DIR
    files={'nodes':net/'road_nodes_preprocessed.parquet','edges':net/'road_edges_preprocessed.parquet','settlements':net/'settlement_road_crosswalk_preprocessed.parquet','facilities':net/'facility_road_crosswalk_preprocessed.parquet','damage':exp/'road_damage_scenario_exposure_preprocessed.parquet','facility_exposure':exp/'facility_hazard_exposure_preprocessed.parquet','saved_detail':root/prod.OUTPUT_DIR/'settlement_disruption_accessibility_robustness_preprocessed.parquet','saved_summary':root/prod.OUTPUT_DIR/'accessibility_robustness_scenario_summary_preprocessed.parquet','priority':root/'data/processed/decision/settlement_priority_scenarios_preprocessed.parquet','production_code':root/'src/preprocessing/build_accessibility_robustness_grid.py','legacy_audit_code':root/'src/analyses/structural_scenario_factor_activity.py'}
    inputs={k:{'path':str(p.relative_to(root)),'sha256':file_sha(p)} for k,p in files.items()}
    nodes=pd.read_parquet(files['nodes']);edges=pd.read_parquet(files['edges']);sett=pd.read_parquet(files['settlements']);fac=pd.read_parquet(files['facilities']);damage=pd.read_parquet(files['damage']);fexp=pd.read_parquet(files['facility_exposure'])
    saved=pd.read_parquet(files['saved_detail']);summ=pd.read_parquet(files['saved_summary']).set_index('Scenario ID');pri=pd.read_parquet(files['priority'])
    ids=sett['OSM settlement ID'].astype(str).to_numpy();sn=sett['Nearest road node ID'].to_numpy(np.int64);sd=sett['Settlement-to-road snap distance (m)'].to_numpy(float)
    assert np.array_equal(nodes['Road node ID'],np.arange(len(nodes))) and not edges['Edge ID'].duplicated().any()
    groups={k:g.set_index('OSM Settlement ID').reindex(ids) for k,g in saved.groupby('Scenario ID',sort=False)}
    pop=pri.loc[pri['Primary Scenario']].set_index('OSM Settlement ID')['Estimated Settlement Population'].reindex(ids).to_numpy(float)
    oldsummary=oldaudit.build_scenario_summary().set_index('Scenario ID')
    maxid=int(edges['Edge ID'].max());empty=np.zeros(maxid+1,bool);sources,_=prod.service_nodes(fac,fexp,1,False)
    rows=[];details=[];toprows=[];mechanism=[];edge_mechanism=[];previous_baseline=None
    for top in prod.TOPOLOGY_THRESHOLDS_M:
        t0=time.monotonic();ee=edges.loc[edges['Minimum topology repair threshold (m)'].le(top)].copy()
        adj=prod.build_adjacency(len(nodes),ee[['Edge ID','From node ID','To node ID','Edge travel time (minutes)']])
        base,_,_=paths(adj,sources,empty);blabel,bcount=components(adj,empty)
        graphhash=fingerprint(ee['Edge ID'].to_numpy(np.int64));basevec=base[sn]
        tr={'Topology (m)':top,'Included edges':len(ee),'Included connectors':int(ee['Edge type'].eq('topology repair').sum()),'Baseline components':bcount,'Baseline edge hash':graphhash,'Baseline component hash':fingerprint(blabel),'Baseline-eligible settlements at 3km':int(((sd<=3000)&np.isfinite(basevec)).sum())}
        if previous_baseline is not None:
            prev=previous_baseline;changed=~np.isclose(prev,basevec,rtol=0,atol=1e-8,equal_nan=True)
            for i in np.flatnonzero(changed):details.append({'Comparison':'baseline topology to previous level','Topology (m)':top,'OSM Settlement ID':ids[i],'Previous minutes':float(prev[i]),'Current minutes':float(basevec[i]),'Assigned Population':float(pop[i])})
        previous_baseline=basevec.copy();toprows.append(tr)
        print('TOPOLOGY',tr,'seconds',round(time.monotonic()-t0,2),flush=True)
        # Compute each graph/retained-destination state once; snap is a settlement filter.
        for _,haz in prod.HAZARD_SCENARIOS:
            damaged=damage['Maximum Intersecting Evidence Class'].ge(haz).fillna(False)
            cache={}
            for closure,grades,cslug in prod.CLOSURE_RULES:
                closed_ids=damage.loc[damaged&damage['CEMS Damage Grade'].isin(grades),'Edge ID'].to_numpy(np.int64)
                closed_ids=np.intersect1d(closed_ids,ee['Edge ID'].to_numpy(np.int64));closed=empty.copy();closed[closed_ids]=True
                active=ee.loc[~ee['Edge ID'].isin(closed_ids)]
                labels,ncomp=components(adj,closed);posthash=fingerprint(active['Edge ID'].to_numpy(np.int64));comphash=fingerprint(labels)
                for fr,remove,fslug in prod.FACILITY_RULES:
                    src,removed=prod.service_nodes(fac,fexp,haz,remove);dist,pa,pe=paths(adj,src,closed)
                    witnesses=witness_edges(sn[(sd<=3000)&np.isfinite(basevec)&np.isfinite(dist[sn])],pa,pe)
                    cache[(cslug,fslug)]={'dist':dist,'witnesses':witnesses,'closed_ids':closed_ids,'labels':labels,'closed':closed}
                    for snap in prod.SNAP_THRESHOLDS_M:
                        sc=prod.scenario_identifier(haz,cslug,fslug,top,snap);ref=groups[sc];eligible=(sd<=snap)&np.isfinite(basevec);reach=(sd<=snap)&np.isfinite(dist[sn]);isolated=eligible&~reach;finite=eligible&reach
                        bt=np.where(eligible,basevec,np.nan);pt=np.where(finite,dist[sn],np.nan);loss=pt-bt;loss[np.isclose(loss,0,atol=1e-10)]=0
                        assert np.array_equal(eligible,ref['Baseline Eligible'].to_numpy(bool)),sc
                        for a,col in [(bt,'Baseline Health/Emergency Accessibility (minutes)'),(pt,'Post-Disruption Travel Time (minutes)'),(loss,'Accessibility Loss (minutes)')]:assert equal_numeric(a,ref[col]),(sc,col)
                        assert np.array_equal(isolated,ref['Newly Isolated'].fillna(False).to_numpy(bool)),sc
                        assert np.array_equal(np.where(eligible,reach,False),ref['Post-Disruption Service Reachable'].fillna(False).to_numpy(bool)),sc
                        delayed=finite&(loss>5);agg=[float(pop[isolated].sum()),float(pop[delayed].sum()),float((pop[finite]*np.maximum(loss[finite],0)).sum())]
                        assert equal_numeric(agg,oldsummary.loc[sc,oldaudit.OUTCOME_COLUMNS],1e-6),sc
                        assert len(closed_ids)==int(summ.loc[sc,'Closed Graph Edges'])
                        assert removed==int(summ.loc[sc,'Removed Health/Emergency Destinations'])
                        prev=oldsummary.loc[sc];rows.append({'Scenario ID':sc,'Minimum Evidence Class':haz,'Road Closure Rule':closure,'Facility Availability Rule':fr,'Topology Repair Threshold (m)':top,'Maximum Settlement Snap Distance (m)':snap,'Included Graph Edges':len(ee),'Connector Edges':tr['Included connectors'],'Closed Graph Edges':len(closed_ids),'Baseline components':bcount,'Post components':ncomp,'Baseline graph hash':graphhash,'Post graph hash':posthash,'Component partition hash':comphash,'Service node hash':fingerprint(np.array(sorted(src),dtype=np.int64)),'Service nodes':len(src),'Eligibility hash':fingerprint(eligible),'Settlement path vector hash':fingerprint(eligible,bt,pt,loss),'Aggregate outcome hash':fingerprint(np.round(agg,3)),'Newly Isolated Population':agg[0],'Population Delayed over 5 Minutes':agg[1],'Population-Weighted Accessibility Loss (person-minutes)':agg[2],'Top-10 Settlement Set':prev['Top-10 Settlement Set'],'Top-10 Settlement Order':prev['Top-10 Settlement Order']})
                    print('verified',top,haz,cslug,fslug,flush=True)
            for _,_,fslug in prod.FACILITY_RULES:
                a=cache[('destroyed',fslug)];b=cache[('all_candidate',fslug)];extra=np.setdiff1d(b['closed_ids'],a['closed_ids']);base_mask=(sd<=3000)&np.isfinite(basevec);oldreach=np.isfinite(a['dist'][sn])&base_mask;newreach=np.isfinite(b['dist'][sn])&base_mask
                assert np.array_equal(oldreach,newreach)
                assert equal_numeric(a['dist'][sn][oldreach],b['dist'][sn][oldreach])
                hits=set(extra)&a['witnesses'];endpoints=edges.set_index('Edge ID').loc[extra,['From node ID','To node ID']]
                mechanism.append({'Topology (m)':top,'Minimum class':haz,'Facility slug':fslug,'Extra closed edges':len(extra),'Extra edges on retained-settlement shortest-path witness':len(hits),'Changed eligible-settlement reachable status':0,'Changed eligible-settlement finite times':0,'Full nodes whose service time changes':int((~np.isclose(a['dist'],b['dist'],rtol=0,atol=1e-8)).sum()),'Component partition changes':fingerprint(a['labels'])!=fingerprint(b['labels'])})
                for eid,(u,v) in endpoints.iterrows():edge_mechanism.append({'Topology (m)':top,'Minimum class':haz,'Facility slug':fslug,'Edge ID':int(eid),'From node':int(u),'To node':int(v),'On retained-settlement shortest-path witness':int(eid) in hits,'From finite service path before':bool(np.isfinite(a['dist'][u])),'To finite service path before':bool(np.isfinite(a['dist'][v])),'From time changes':not bool(np.isclose(a['dist'][u],b['dist'][u],rtol=0,atol=1e-8)),'To time changes':not bool(np.isclose(a['dist'][v],b['dist'][v],rtol=0,atol=1e-8))})
            del cache;gc.collect()
        del adj;gc.collect()
    frame=pd.DataFrame(rows);assert len(frame)==192
    factors=[]
    fcols=oldaudit.FACTOR_COLUMNS
    for name,col in fcols.items():
        held=[c for c in fcols.values() if c!=col];gg=list(frame.groupby(held,dropna=False));record={'Factor':name,'Levels':oldaudit.stable_levels(frame[col]),'Comparison groups':len(gg)}
        for label,cols in {'Baseline graph active':['Baseline graph hash'],'Post graph active':['Post graph hash'],'Component partition active':['Component partition hash'],'Destinations active':['Service node hash'],'Baseline eligibility active':['Eligibility hash'],'Settlement path vector active':['Settlement path vector hash'],'Aggregate outcome active':['Aggregate outcome hash'],'Top-10 set active':['Top-10 Settlement Set'],'Top-10 order active':['Top-10 Settlement Order']}.items():record[label]=sum(any(g[c].nunique()>1 for c in cols) for _,g in gg)
        record['Maximum closed-edge count change']=max(int(g['Closed Graph Edges'].max()-g['Closed Graph Edges'].min()) for _,g in gg)
        factors.append(record)
    frame.to_parquet(out/'scenario-state-audit.parquet',index=False);pd.DataFrame(factors).to_parquet(out/'factor-activity-corrected.parquet',index=False);pd.DataFrame(toprows).to_parquet(out/'topology-graph-summary.parquet',index=False);pd.DataFrame(details).to_parquet(out/'baseline-topology-settlement-changes.parquet',index=False);pd.DataFrame(mechanism).to_parquet(out/'closure-witness-summary.parquet',index=False);pd.DataFrame(edge_mechanism).to_parquet(out/'extra-closure-edge-witnesses.parquet',index=False)
    assert all(file_sha(files[k])==v['sha256'] for k,v in inputs.items())
    report={'status':'validated','inputs':inputs,'production_outputs_modified':False,'all_192_saved_settlement_vectors_reproduced':True,'path_tolerance_minutes':1e-8,'aggregate_tolerance':1e-6,'fingerprint_rounding_decimals':8,'aggregate_state_rounding_decimals':3,'distinct_baseline_graphs':frame['Baseline graph hash'].nunique(),'distinct_post_graphs':frame['Post graph hash'].nunique(),'distinct_component_partitions':frame['Component partition hash'].nunique(),'distinct_path_vectors':frame['Settlement path vector hash'].nunique(),'distinct_aggregate_states':frame['Aggregate outcome hash'].nunique(),'distinct_top10_sets':frame['Top-10 Settlement Set'].nunique(),'distinct_top10_orders':frame['Top-10 Settlement Order'].nunique(),'topology_summary':toprows,'factor_activity':factors,'closure_witness_summary':mechanism,'runtime_note':'Component counts include all original graph nodes, including those isolated after closures; snap changes eligibility, not graph edge sets. Witness paths are one shortest-path forest, not a claim that an edge lies on no possible shortest path.'}
    (out/'audit.json').write_text(json.dumps(report,indent=2,default=lambda v:v.item() if isinstance(v,np.generic) else str(v))+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['inputs','closure_witness_summary']},indent=2,default=lambda v:v.item() if isinstance(v,np.generic) else str(v)),flush=True)


if __name__=='__main__':main()
