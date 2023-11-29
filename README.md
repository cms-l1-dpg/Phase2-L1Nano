# Phase2-L1Nano
NanoAOD ntupler for Phase-2 L1 Objects

## Setup

Tested under latest CMSSW_13_3 pre-release: `CMSSW_13_3_0_pre4`:

```bash
cmsrel CMSSW_13_3_0_pre4
cd CMSSW_13_3_0_pre4/src
git cms-checkout-topic -u p2l1-gtEmulator:phase2-l1t-integration-13_3_0_pre3 #latest P2GT PR: https://github.com/cms-l1t-offline/cmssw/pull/1183
git cms-rebase-topic -u artlbv:CMSSW_13_3_X_FixP2GT_HW_access # getting fix for P2GT HW access/conversion to int
## eventually remove the tkJet sequence from the L1Sim step: 
git clone git@github.com:cms-l1-dpg/Phase2-L1Nano.git PhysicsTools/L1Nano
scram b -j 8
```

## Usage

### Direct config

In the `test` directory there is a `cmsRun` config to rerun the L1 trigger + the P2GT emulator and produce the nano ntuple from these outputs.

Usage: `cmsRun rerunL1_133_Nano_cfg.py`

### Via cmsDriver

One can append the L1Nano output to the `cmsDriver` command via this customisation: 
```bash
-s USER:PhysicsTools/L1Nano/l1tPh2Nano_cff.l1tPh2NanoTask --customise PhysicsTools/L1Nano/l1tPh2Nano_cff.addFullPh2L1Nano
```

Example command (w/o P2GT yet, pending https://github.com/cms-sw/cmssw/pull/43210 ):
```bash
cmsDriver.py reL1Nano --conditions 125X_mcRun4_realistic_v2 -n 2 --era Phase2C17I13M9 --eventcontent NANOAOD -s RAW2DIGI,L1,NANO --datatier GEN-SIM-DIGI-RAW-MINIAOD --fileout file:test.root --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2.addHcalTriggerPrimitives,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT --geometry Extended2026D88 --nThreads 1 --filein file:/eos/cms/store/mc/Phase2Spring23DIGIRECOMiniAOD/VBFHToInvisible_M-125_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/2520000/0294bad4-867c-43c9-850f-4beaef783e39.root --mc --inputCommands='keep *, drop l1tPFJets_*_*_*' --outputCommands='keep *P2GT*_*_*_*, drop l1tPFJets_*_*_*' --python_filename rerunL1_only_cfg_NANO.py --no_exec -s USER:PhysicsTools/L1Nano/l1tPh2Nano_cff.l1tPh2NanoTask --customise PhysicsTools/L1Nano/l1tPh2Nano_cff.addFullPh2L1Nano
```


## Output

The output file is a nanoAOD file with the output branches in the `Events` tree:

Example:

```python
['run',
 'luminosityBlock',
 'event',
 'bunchCrossing',
 'nL1caloJet',
 'L1caloJet_et',
 'L1caloJet_eta',
 'L1caloJet_phi',
 'L1caloJet_pt',
 'L1caloJet_z0',
 'nL1caloTau',
 'L1caloTau_eta',
 'L1caloTau_phi',
 'L1caloTau_pt',
 'nGenJet',
 'GenJet_eta',
 'GenJet_mass',
 ...
```

This can be easily handled with [`uproot/awkward`](https://gitlab.cern.ch/cms-podas23/dpg/trigger-exercise/-/blob/solutions/1_Intro_NanoAwk_Analysis_Solution.ipynb) like this:

```python
f = uproot.open("l1nano.root")
events = f["Events"].arrays() 
```

### P2GT emulator decisions
The GT emulator decisions are stored like this for now:
```
'nL1GT', -> number of algorithms, the names are not stored, but are alphabetically sorted
'L1GT_final', -> final decision
'L1GT_initial', -> initial decision (no difference at the moment)
```