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

def addFullPh2L1Nano(process):
    addGenObjects(process)
    addPh2L1Objects(process)
    addPh2GTObjects(process)

    return process


def customise_L1Nano_13xContent(process):
    ## use old vertex collection
    process.vtxTable.src = cms.InputTag('l1tVertexFinderEmulator','l1verticesEmulation')
    process.pvtxTable.src = cms.InputTag('l1tVertexFinderEmulator','l1verticesEmulation')
    # use old muon collection
    process.gmtTkMuTable.src = cms.InputTag('l1tTkMuonsGmt','')
    # remove old barrel EG collection
    # process.staEGmerged.src = cms.VInputTag(
    #     cms.InputTag('l1tEGammaClusterEmuProducer',''),
    #     cms.InputTag('l1tLayer2EG','L1CtEgEE')
    #     )
    process.p2L1TablesTask.remove(process.staEGmerged)
    process.p2L1TablesTask.remove(process.staEGTable)
    # process.staEGebTable.src = cms.InputTag('l1tEGammaClusterEmuProducer','')
    process.p2L1TablesTask.remove(process.staEGebTable)
    ## remove extended puppi jets
    process.p2L1TablesTask.remove(process.scExtJetTable)
    process.l1tPh2NanoTask.remove(process.p2GTL1TablesTask)
    ## keep L1PF jets
    process.p2L1TablesTask.remove(process.scJetTable)
    # process.source.inputCommands = cms.untracked.vstring('keep *')

# customise_L1Nano_13xContent(process)