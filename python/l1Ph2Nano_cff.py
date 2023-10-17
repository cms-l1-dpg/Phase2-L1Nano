import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.nano_eras_cff import *
from PhysicsTools.NanoAOD.common_cff import *

## Inspired by: 
## FastPUPPI ntupler https://github.com/p2l1pfp/FastPUPPI/blob/12_5_X/NtupleProducer/python/runPerformanceNTuple.py
## https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCandidateModules#Merging_Candidate_Collections 

##################################################################
### This part can be taken from l1trig_cff starting from 13X
l1_float_precision_=16

l1PtVars = cms.PSet(
    pt  = Var("pt",  float, precision=l1_float_precision_),
    phi = Var("phi", float, precision=l1_float_precision_),
)
l1P3Vars = cms.PSet(
    l1PtVars,
    eta = Var("eta", float, precision=l1_float_precision_),
)

l1ObjVars = cms.PSet(
    l1P3Vars,
    hwPt = Var("hwPt()",int,doc="hardware pt"),
    hwEta = Var("hwEta()",int,doc="hardware eta"),
    hwPhi = Var("hwPhi()",int,doc="hardware phi"),
    hwQual = Var("hwQual()",int,doc="hardware qual"),
    hwIso = Var("hwIso()",int,doc="hardware iso")
)

l1GTObjVars = cms.PSet(
    l1P3Vars,
    # z0 = Var("vz",int,doc="z0"),
)
### This above part can be taken from l1trig_cff starting from 13X
##################################################################

### Tables definitions    

### Vertex

gtVtxTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','GTTPrimaryVert'),
    cut = cms.string(""),
    name = cms.string("GTvertices"),
    doc = cms.string("GT GTT Vertices"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
        z0 = Var("vz",float),
    )
)

vtxTable = cms.EDProducer(
    "SimpleVtxWordCandidateFlatTableProducer", ## note the use of a dedicated table producer which is defined in the plugins/L1TableProducer.cc
    src = cms.InputTag('l1tVertexFinderEmulator','l1verticesEmulation'),
    cut = cms.string(""),
    name = cms.string("gttVert"),
    doc = cms.string("GTT Vertices"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        # l1GTObjVars,
        z0 = Var("z0()",float),
        pt = Var("pt()",float),
    )
)

### GT
gtTkEleTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2Electrons'),
    cut = cms.string(""),
    name = cms.string("GTtkElectron"),
    doc = cms.string("GT tkElectrons"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
        #hwPt = Var("hwPT()",int,doc="hardware pt"),
        z0 = Var("vz",float),
    )
)

gtTkPhoTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2Photons'),
    cut = cms.string(""),
    name = cms.string("GTtkPhoton"),
    doc = cms.string("GT tkPhotons"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
        #iso = Var("iso()",int,doc="z0"),
    )
)

gtTkMuTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','GMTTkMuons'),
    cut = cms.string(""),
    name = cms.string("GTgmtTkMuon"),
    doc = cms.string("GT GMT tkMuon"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
        #iso = Var("iso()",int,doc="z0"),
        #hwQual = Var("hwQual()",int,doc="hwQual"),
        z0 = Var("vz",float),
    )
)

gtSCJetsTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2Jets'),
    cut = cms.string(""),
    name = cms.string("GTscJets"),
    doc = cms.string("GT seededCone Puppi Jets"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
    )
)

gtNNTauTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2Taus'),
    cut = cms.string(""),
    name = cms.string("GTnnTaus"),
    doc = cms.string("GT NNpuppi Taus"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1GTObjVars,
    )
)

gtEtSumTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2EtSum'),
    name = cms.string("GTetSum"),
    doc = cms.string("GT etSum"),
    singleton = cms.bool(True), # the number of entries is variable
    variables = cms.PSet(
        # l1GTObjVars,
        pt = Var("pt", int, doc="MET pt"),
        phi = Var("phi", int, doc="MET phi"),
    )
)

gtHtSumTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tGTProducer','CL2HtSum'),
    name = cms.string("GThtSum"),
    doc = cms.string("GT htSum"),
    singleton = cms.bool(True), # the number of entries is variable
    variables = cms.PSet(
        # l1GTObjVars,
        mht = Var("pt", int, doc="MHT"),
        #ht = Var("scasum", int, doc="HT"),
    )
)

#### EG

tkPhotonTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tLayer2EG','L1CtTkEm'),
    cut = cms.string(""),
    name = cms.string("tkPhoton"),
    doc = cms.string("Tk Photons (EM)"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1ObjVars,
        tkIso   = Var("trkIsol", float, precision=8),
        tkIsoPV  = Var("trkIsolPV", float, precision=8),
    )
)

tkEleTable = tkPhotonTable.clone(
    src = cms.InputTag('l1tLayer2EG','L1CtTkElectron'),
    name = cms.string("tkElectron"),
    doc = cms.string("Tk Electrons"),
    # variables = charge  = Var("charge", int, doc="charge id"),
)
tkEleTable.variables.charge = Var("charge", int, doc="charge")
tkEleTable.variables.z0     = Var("trkzVtx", float, "vertex z0")
# tkEleTable.variables.caloEta = Var("EGRef.eta",float)
# tkEleTable.variables.caloPhi = Var("EGRef.phi",float)

## merge EG 
staEGmerged = cms.EDProducer("CandViewMerger",
       src = cms.VInputTag(
           cms.InputTag('l1tPhase2L1CaloEGammaEmulator','GCTEGammas'), 
           cms.InputTag('l1tLayer2EG','L1CtEgEE'),
  )
)

staEGTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("staEGmerged"),
    cut = cms.string(""),
    name = cms.string("EG"),
    doc = cms.string("standalone EG merged endcap and barrel"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1PtVars,
    )
)

### Muons
gmtTkMuTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tTkMuonsGmt',''),
    cut = cms.string(""),
    name = cms.string("gmtTkMuon"),
    doc = cms.string("GMT Tk Muons"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1ObjVars,
        charge  = Var("charge", int, doc="charge id"),
        z0 = Var("phZ0()",float),
        vz = Var("vz",float),
        phPt = Var("phPt()",float),

# phPt = Var("phPt()",float),
# phEta()
# phPhi()
# phZ0()
# phD0()
# phCharge()
# hwPt()
# hwEta()
# hwPhi()
# hwZ0()
# hwD0()
# hwCharge()
# hwIso()
# hwQual()
# hwBeta()

    )
)

staMuTable = gmtTkMuTable.clone(
    src = cms.InputTag('l1tSAMuonsGmt','promptSAMuons'),
    name = cms.string("StaMu"),
    doc = cms.string("GMT STA Muons"),
)

### Jets
scJetTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tSCPFL1PuppiCorrectedEmulator'),
    cut = cms.string(""),
    name = cms.string("seededConeJet"),
    doc = cms.string("SeededCone 0.4 Puppi jet"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1P3Vars,
        et = Var("et",float)
    )
)

histoJetTable = scJetTable.clone(
    src = cms.InputTag("l1tPhase1JetCalibrator9x9trimmed" ,   "Phase1L1TJetFromPfCandidates"),
    name = cms.string("histoJet"),
    doc = cms.string("Puppi Jets 9x9"),
)


caloJetTable = scJetTable.clone(
    src = cms.InputTag("l1tCaloJet","L1CaloJetCollectionBXV"),
    name = cms.string("caloJet"),
    doc = cms.string("Calo Jets"),
)

### SUMS

puppiMetTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("l1tMETPFProducer",""),
    name = cms.string("puppiMET"),
    doc = cms.string("Puppi MET"),
    singleton = cms.bool(True), # the number of entries is variable
    variables = cms.PSet(
        l1PtVars
    )
)

seededConeSumsTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("l1tSCPFL1PuppiCorrectedEmulatorMHT",""),
    name = cms.string("seededConeHTMHT"),
    doc = cms.string("HT and MHT from SeededCone jets"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1PtVars
    )
)

### CHANGE TO TRIMMED WHEN AVAILABLE
### TAG IS l1tPhase1JetSumsProducer9x9trimmed

histoSumsTable = seededConeSumsTable.clone(
    src = cms.InputTag("l1tPhase1JetSumsProducer9x9","Sums"),
    name = cms.string("histoHTMHT"),
    doc = cms.string("HT and MHT from histogrammed jets"),
    )


### Taus
caloTauTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("l1tCaloJet","L1CaloTauCollectionBXV"),
    cut = cms.string(""),
    name = cms.string("caloTau"),
    doc = cms.string("Calo Taus"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1P3Vars,
    )
)

nnTauTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("l1tNNTauProducerPuppi","L1PFTausNN"),
    cut = cms.string(""),
    name = cms.string("nnTau"),
    doc = cms.string("NN Taus"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1P3Vars,
    )
)

## GT objects
p2GTL1TablesTask = cms.Task(
    gtTkPhoTable,
    gtTkEleTable,
    gtTkMuTable,
    gtSCJetsTable,
    gtNNTauTable,
    gtEtSumTable,
    gtHtSumTable,
    gtVtxTable,
)
    
p2L1TablesTask = cms.Task(
    ## Muons
    gmtTkMuTable,
    staMuTable,
    ## EG
    tkEleTable,
    tkPhotonTable,
    staEGmerged, staEGTable, ## Need to run merger before Table task! Stanalone EG – not in GT yet
    # ## jets
    scJetTable,
    histoJetTable,
    caloJetTable,
    # ## sums
    puppiMetTable,
    seededConeSumsTable,
    histoSumsTable,
    # taus
    caloTauTable,
    nnTauTable,
    # GTT 
    vtxTable,

)

## Add GT ntuple to L1Task
p2L1TablesTask.add(p2GTL1TablesTask)