# Phase2-L1Nano
NanoAOD ntupler for Phase-2 L1 Objects

## Setup

This is for the event content of the 140x MC campaign `Phase2Spring24DIGIRECOMiniAOD`.

NO corresponding menu twiki section YET.

```bash
cmsrel CMSSW_14_1_0_pre4
cd CMSSW_14_1_0_pre4/src/
cmsenv
### ADDING NANO
git clone git@github.com:cms-l1-dpg/Phase2-L1Nano.git PhysicsTools/L1Nano
scram b -j 8
```

## Usage

### Direct config
 
NA

### Via cmsDriver

One can append the L1Nano output to the `cmsDriver` command via this customisation: 
```bash
--eventcontent NANOAOD
-s USER:PhysicsTools/L1Nano/l1tPh2Nano_cff.l1tPh2NanoTask --customise PhysicsTools/L1Nano/l1tPh2Nano_cff.addFullPh2L1Nano
```

`cmsDriver` command to only run the P2GT and NANO from the event content:
```bash
cmsDriver.py step1 --conditions auto:phase2_realistic_T25 -n 2 --era Phase2C17I13M9 --eventcontent NANOAOD -s L1P2GT,USER:PhysicsTools/L1Nano/l1tPh2Nano_cff.l1tPh2NanoTask --customise PhysicsTools/L1Nano/l1tPh2Nano_cff.addFullPh2L1Nano --datatier FEVTDEBUGHLT --fileout file:nano_from_fevt.root --geometry Extended2026D95 --nThreads 1 --filein /store/mc/Phase2Spring24DIGIRECOMiniAOD/TT_TuneCP5_14TeV-POWHEG-Pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU140_Trk1GeV_140X_mcRun4_realistic_v4-v2/70000/1ab06eaa-9574-486d-954b-8535337fd5c5.root
```


## Output

The output file is a nanoAOD file with the output branches in the `Events` tree.

An overview of the corresponding content is shown here: https://alobanov.web.cern.ch/L1T/Phase2/L1Nano/l1menu_nano_V38_1400pre3V9_doc_report.html

Size report: https://alobanov.web.cern.ch/L1T/Phase2/L1Nano/l1menu_nano_V38_1400pre3V9_size_report.html

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
