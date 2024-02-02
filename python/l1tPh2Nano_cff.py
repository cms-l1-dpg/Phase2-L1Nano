import FWCore.ParameterSet.Config as cms
# from PhysicsTools.NanoAOD.nano_eras_cff import *
from PhysicsTools.NanoAOD.common_cff import *

l1tPh2NanoTask = cms.Task()

## P2GT objects
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

    if True:
        ## Gen all 
        # genParticleTable.src = "genParticles" # see 
        ## Mini default, see  https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/PatAlgos/python/slimming/prunedGenParticles_cfi.py
        # genParticleTable.src = "prunedGenParticles"
        ## Nano default, see https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/genparticles_cff.py#L8
        # genParticleTable.src = "finalGenParticles" 

        ## add pruned gen particles a la Mini
        process.prunedGenParticleTable = genParticleTable.clone()
        process.prunedGenParticleTable.src = "prunedGenParticles"
        process.prunedGenParticleTable.name = "prunedGenPart"
        process.l1tPh2NanoTask.add(process.prunedGenParticleTable)


    ## add more GenVariables
    if True:
        # from L1Ntuple Gen: https://github.com/artlbv/cmssw/blob/94a5ec13b8ce76afb8ea4f157bb92fb547fadee2/L1Trigger/L1TNtuples/plugins/L1GenTreeProducer.cc#L203
        genParticleTable.variables.vertX = Var("vertex.x", float, "vertex X")
        genParticleTable.variables.vertY = Var("vertex.y", float, "vertex Y")
        genParticleTable.variables.lXY = Var("sqrt(vertex().x() * vertex().x() + vertex().y() * vertex().y())", float, "lXY")
        genParticleTable.variables.dXY = Var("-vertex().x() * sin(phi()) + vertex().y() * cos(phi())", float, "dXY")

    process.l1tPh2NanoTask.add(
                puTable, metMCTable,
                genParticleTask, genParticleTablesTask,
                genJetTable, patJetPartonsNano,genJetFlavourAssociation, genJetFlavourTable,
                genTauTask,
    )

    return process

### AllGen

def addFullPh2L1Nano(process):
    addGenObjects(process)
    addPh2L1Objects(process)
    addPh2GTObjects(process)

    return process

