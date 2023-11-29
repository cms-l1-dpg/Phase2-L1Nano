import FWCore.ParameterSet.Config as cms
# from PhysicsTools.NanoAOD.nano_eras_cff import *
from PhysicsTools.NanoAOD.common_cff import *

l1tPh2NanoTask = cms.Task()

### P2GT objects
from PhysicsTools.L1Nano.l1tPh2GTtables_cff import *
def addPh2GTObjects(process):
    process.l1tPh2NanoTask.add(p2GTL1TablesTask)
    return process

### Main Ph2L1 objects
from PhysicsTools.L1Nano.l1tPh2Nanotables_cff import *
def addPh2L1Objects(process):
    process.l1tPh2NanoTask.add(p2L1TablesTask)
    return process

#### GENERATOR INFO
## based on https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/nanogen_cff.py#L2-L36
from PhysicsTools.NanoAOD.genparticles_cff import * ## for GenParts
from PhysicsTools.NanoAOD.jetMC_cff import * ## for GenJets
from PhysicsTools.NanoAOD.met_cff import metMCTable ## for GenMET
from PhysicsTools.NanoAOD.globals_cff import puTable ## for PU
from PhysicsTools.NanoAOD.taus_cff import * ## for Gen taus
def addGenObjects(process):
    process.l1tPh2NanoTask.add(
                puTable, metMCTable,
                genParticleTask, genParticleTablesTask,
                genJetTable, patJetPartonsNano,genJetFlavourAssociation, genJetFlavourTable,
                genTauTask,
    )
    return process

def addFullPh2L1Nano(process):
    addGenObjects(process)
    addPh2L1Objects(process)
    addPh2GTObjects(process)

    return process

