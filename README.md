# Phase2-L1Nano
NanoAOD ntupler for Phase-2 L1 Objects

## Setup

Tested under latest CMSSW_13_3 "nightly" build: `CMSSW_13_3_X_2023-10-10-2300`:

```bash
cmsrel CMSSW_13_3_X_2023-10-10-2300
cd CMSSW_13_3_X_2023-10-10-2300/src
git cms-rebase-topic -u artlbv:CMSSW_13_3_X_FixP2GT_HW_access # getting fix for P2GT HW access/conversion to int
git clone git@github.com:cms-l1-dpg/Phase2-L1Nano.git PhysicsTools/L1Nano
scram b -j 8
```

## Usage

In the `test` directory there is a `cmsRun` config to rerun the L1 trigger + the P2GT emulator and produce the nano ntuple from these outputs.

Usage: `cmsRun rerunL1_133_Nano_cfg.py`


## Output

The output file is a nanoAOD file with the output branches in the `Events` tree:

Example:

```python
['ngmtTkMuons',
 'gmtTkMuons_charge',
 'gmtTkMuons_hwEta',
 'gmtTkMuons_hwIso',
 'gmtTkMuons_hwPhi',
 'gmtTkMuons_hwPt',
 'gmtTkMuons_hwQual',
 'gmtTkMuons_eta',
 'gmtTkMuons_phPt',
 'gmtTkMuons_phi',
 'gmtTkMuons_pt',
 'gmtTkMuons_vz',
 'gmtTkMuons_z0',
 'nGTgmtTkMuon',
 'GTgmtTkMuon_eta',
 'GTgmtTkMuon_phi',
 'GTgmtTkMuon_pt',
 'GTgmtTkMuon_z0']
```

This can be easily handled with [`uproot/awkward`](https://gitlab.cern.ch/cms-podas23/dpg/trigger-exercise/-/blob/solutions/1_Intro_NanoAwk_Analysis_Solution.ipynb) like this:

```python
f = uproot.open("l1nano.root")
events = f["Events"].arrays() 
```