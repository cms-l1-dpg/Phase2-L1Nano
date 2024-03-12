import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.NanoAOD.l1trig_cff import *

## Import GT scales for HW to physical value conversion
from L1Trigger.Phase2L1GT.l1tGTScales import scale_parameter

### common variables set (pt/eta/phi)
l1GTObjVars = cms.PSet(
    l1P3Vars,
)

### P2GT Algo Block - trigger decisions
gtAlgoTable = cms.EDProducer(
    "P2GTAlgoBlockFlatTableProducer",
    src = cms.InputTag('l1tGTAlgoBlockProducer'),
    cut = cms.string(""),
    name = cms.string("L1GT"),
    doc = cms.string("GT Algo Block decisions"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        # name = Var("algoName",string, doc = "algo name"), # does not work
        final = Var("decisionFinal",float, doc = "final decision"),
        initial = Var("decisionBeforeBxMaskAndPrescale",float, doc = "initial decision"),
    )
)

### Vertex
gtVtxTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','GTTPrimaryVert'),
    cut = cms.string(""),
    name = cms.string("L1GTVertex"),
    doc = cms.string("GT GTT Vertices"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        z0 = Var("vz",float, doc = "primary vertex position z coordinate"),
        # sumPt = Var("hwSum_pT_pv_toInt()*0.25",float, doc = "sum pt of tracks"),
        ## hw vars
        hwZ0 = Var("hwZ0_toInt()",int, doc = "HW primary vertex position z coordinate"),
        # hwSum_pT_pv = Var("hwSum_pT_pv_toInt()",int, doc = "HW sum pt of tracks"),
    )
)

### Store Primary Vertex only (first vertex)
gtPvTable = gtVtxTable.clone(
    name = cms.string("L1GTPV"),
    doc = cms.string("GT GTT Leading Primary Vertex"),
    maxLen = cms.uint32(1),
)

### GT
gtTkPhoTable =cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2Photons'),
    name = cms.string("L1GTtkPhoton"),
    doc = cms.string("GT tkPhotons"),
    cut = cms.string(""),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
        ## hw values
        # hwPt = Var("hwPT_toInt()",int,doc="hardware pt"),
        hwQual = Var("hwQual_toInt()",int),
        hwIso = Var("hwIso_toInt()",int),
        ## more physical values
        ## using the GT scales for HW to physicsal vonversion, see scales in https://github.com/cms-sw/cmssw/blob/master/L1Trigger/Phase2L1GT/python/l1tGTScales.py
        iso = Var(f"hwIso_toInt()*{scale_parameter.isolation_lsb.value()}",float, doc = "absolute isolation"),
        relIso = Var(f"hwIso_toInt()*{scale_parameter.isolation_lsb.value()} / pt",float, doc = "relative isolation")
    )
)

## GT tkElectrons
gtTkEleTable = gtTkPhoTable.clone(
    src = cms.InputTag('l1tGTProducer','CL2Electrons'),
    name = cms.string("L1GTtkElectron"),
    doc = cms.string("GT tkElectrons"),
)

gtTkEleTable.variables.z0 = Var("vz",float)
gtTkEleTable.variables.charge = Var("charge", int, doc="charge id")
gtTkEleTable.variables.hwZ0 = Var("hwZ0_toInt()",int)

## GT gmtTkMuons
gtTkMuTable = gtTkEleTable.clone(
    src = cms.InputTag('l1tGTProducer','GMTTkMuons'),
    name = cms.string("L1GTgmtTkMuon"),
    doc = cms.string("GT GMT tkMuon"),
    variables = cms.PSet(
        l1GTObjVars,
        z0 = Var("vz",float),
        charge = Var("charge", int, doc="charge id"),
        ## hw
        hwQual = Var("hwQual_toInt()",int),
        hwD0 = Var("hwD0_toInt()",int),
        hwZ0 = Var("hwZ0_toInt()",int),
        # hwBeta = Var("hwBeta_toInt()",int)
    )
)

gtSaMuTable = gtTkMuTable.clone(
    src = cms.InputTag('l1tGTProducer','GMTSaPromptMuons'),
    name = cms.string("L1GTgmtMuon"),
    doc = cms.string("GT GMT standalone Muon"),
)

gtSaDispMuTable = gtTkMuTable.clone(
    src = cms.InputTag('l1tGTProducer','GMTSaDisplacedMuons'),
    name = cms.string("L1GTgmtDispMuon"),
    doc = cms.string("GT GMT standalone displaced Muon"),
)

## GT seededCone puppi Jets
gtSCJetsTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2Jets'),
    cut = cms.string(""),
    name = cms.string("L1GTscJet"),
    doc = cms.string("GT CL2Jets: seededCone Puppi Jets"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
        z0 = Var("vz",float),
    )
)

gtNNTauTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2Taus'),
    cut = cms.string(""),
    name = cms.string("L1GTnnTau"),
    doc = cms.string("GT CL2Taus: NN puppi Taus"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
        z0 = Var(f"hwSeed_z0_toInt()*{scale_parameter.seed_z0_lsb.value()}",float, doc = "z0"),
        hwZ0 = Var(f"hwSeed_z0_toInt()",int, doc = "hwZ0"),
    )
)

gtEtSumTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2EtSum'),
    name = cms.string("L1GTpuppiMET"),
    doc = cms.string("GT CL2EtSum"),
    singleton = cms.bool(True), # the number of entries is variable
    variables = cms.PSet(
        pt = Var("pt", float, doc="MET pt"),
        phi = Var("phi", float, doc="MET phi"),
    )
)

gtHtSumTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2HtSum'),
    name = cms.string("L1GTscJetSum"),
    doc = cms.string("GT CL2HtSum"),
    singleton = cms.bool(True), # the number of entries is variable
    variables = cms.PSet(
        # l1GTObjVars,
        mht = Var("pt", float, doc="MHT pt"),
        mhtPhi = Var("phi", float, doc="MHT phi"),
        ht = Var(f"hwSca_sum_toInt()*{scale_parameter.sca_sum_lsb.value()}", float, doc="HT"), ## HACK via hw value!
    )
)

## GT objects
p2GTL1TablesTask = cms.Task(
    gtAlgoTable,
    gtTkPhoTable,
    gtTkEleTable,
    gtTkMuTable,
    gtSaMuTable, gtSaDispMuTable,
    gtSCJetsTable,
    gtNNTauTable,
    gtEtSumTable,
    gtHtSumTable,
    gtVtxTable,
    gtPvTable,
)
