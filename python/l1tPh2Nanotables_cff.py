import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.NanoAOD.l1trig_cff import *

#### GTT Vertex
vtxTable = cms.EDProducer(
    "SimpleL1VtxWordCandidateFlatTableProducer", ## note the use of a dedicated table producer which is defined in the plugins/L1TableProducer.cc
    src = cms.InputTag('l1tVertexFinderEmulator','L1VerticesEmulation'),
    cut = cms.string(""),
    name = cms.string("L1Vertex"),
    doc = cms.string("GTT Vertices"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        z0 = Var("z0()",float, doc = "primary vertex position z coordinate"),
        sumPt = Var("pt()",float, doc = "sum pt of tracks")
    )
)

### Store Primary Vertex only (first vertex)
pvtxTable = vtxTable.clone(
    maxLen = cms.uint32(1),
    name = cms.string("L1PV"),
    doc = cms.string("GTT Leading Primary Vertex"),
)

#### EG
tkPhotonTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tLayer2EG','L1CtTkEm'),
    cut = cms.string(""),
    name = cms.string("L1tkPhoton"),
    doc = cms.string("Tk Photons (EM)"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1ObjVars,
        relIso = Var("trkIsol", float, doc = "relative Isolation based on trkIsol variable"),
        # tkIso   = Var("trkIsol", float), ## use above instead to be consistent with the GT and with the tkEle
        # tkIsoPV  = Var("trkIsolPV", float),
        # pfIso   = Var("pfIsol", float),
        # puppiIso  = Var("puppiIsol", float),
        ## quality WPs, see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePhysicsCutParser#Suppported_operators_and_functio
        saId  = Var("test_bit(hwQual(),0)", bool, doc = "standalone ID, bit 0 of hwQual"),
        eleId = Var("test_bit(hwQual(),1)", bool, doc = "electron ID, bit 1 of hwQual"),
        phoId = Var("test_bit(hwQual(),2)", bool, doc = "photon ID, bit 2 of hwQual"),
    )
)

tkEleTable = tkPhotonTable.clone(
    src = cms.InputTag('l1tLayer2EG','L1CtTkElectron'),
    name = cms.string("L1tkElectron"),
    doc = cms.string("Tk Electrons"),
)
tkEleTable.variables.z0     = Var("trkzVtx", float, "track vertex z0")
tkEleTable.variables.charge = Var("charge", int, doc="charge")
## additional variables that are not used in the menu/GT
## from https://github.com/p2l1pfp/FastPUPPI/blob/12_5_X/NtupleProducer/python/runPerformanceNTuple.py#L499C8-L501C83
# tkEleTable.variables.tkEta = Var("trkPtr.eta", float,precision=8)
# tkEleTable.variables.tkPhi = Var("trkPtr.phi", float,precision=8)
# tkEleTable.variables.tkPt = Var("trkPtr.momentum.perp", float,precision=8)

# merge EG
staEGmerged = cms.EDProducer("CandViewMerger",
       src = cms.VInputTag(
           cms.InputTag('l1tPhase2L1CaloEGammaEmulator','GCTEGammas'),
           cms.InputTag('l1tLayer2EG','L1CtEgEE'),
  )
)

# #staEGTable = tkPhotonTable.clone(
#     src = cms.InputTag("staEGmerged"),
#     name = cms.string("L1EG"),
#     doc = cms.string("standalone EG merged endcap and barrel"),
#     variables = cms.PSet(
#         l1P3Vars,
#     )
# )

staEGTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("staEGmerged"),
    cut = cms.string(""),
    name = cms.string("L1EG"),
    doc = cms.string("standalone EG merged endcap and barrel"),
    # singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1P3Vars,
        ### FIXME
        ### NOTE THE BELOW DOES NOT WORK FOR NOW
        ### This only works when using each collection barrel/endcap separately with the SimpleTriggerL1EGFlatTableProducer -> Need to fix this !
        # hwQual = Var("hwQual",int,doc="hardware qual"),
        ## quality WPs, see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePhysicsCutParser#Suppported_operators_and_functio
        # saId  = Var("test_bit(hwQual(),0)", bool),
        # eleId = Var("test_bit(hwQual(),1)", bool),
        # phoId = Var("test_bit(hwQual(),2)", bool),
    )
)

staEGebTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tPhase2L1CaloEGammaEmulator','GCTEGammas'),
    cut = cms.string(""),
    name = cms.string("L1EGbarrel"),
    doc = cms.string("standalone EG barrel"),
    # singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1P3Vars,
        ### FIXME
        ### This only works when using each collection barrel/endcap separately with the SimpleTriggerL1EGFlatTableProducer -> Need to fix this !
        hwQual = Var("hwQual",int,doc="hardware qual"),
        # quality WPs, see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePhysicsCutParser#Suppported_operators_and_functio
        saId  = Var("test_bit(hwQual(),0)", bool, doc = "standalone ID, bit 0 of hwQual"),
        eleId = Var("test_bit(hwQual(),1)", bool, doc = "electron ID, bit 1 of hwQual"),
        phoId = Var("test_bit(hwQual(),2)", bool, doc = "photon ID, bit 2 of hwQual"),
    )
)

staEGeeTable =  staEGebTable.clone(
    src = cms.InputTag('l1tLayer2EG','L1CtEgEE'),
    name = cms.string("L1EGendcap"),
    doc = cms.string("standalone EG endcap"),
)

### Muons

staMuTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tSAMuonsGmt','promptSAMuons'),
    name = cms.string("L1gmtMuon"),
    doc = cms.string("GMT standalone Muons"),
    cut = cms.string(""),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        # l1ObjVars,
        ### WARNING : the pt/eta/phi/vz methods give rounded results -> use the "physical" accessors
        # vz = Var("vz",float),
        chargeNoPh = Var("charge", int, doc="charge id"),

        ## physical values
        #phPt = Var("phPt()",float),
        pt  = Var("phPt()",float),
        eta = Var("phEta()",float),
        phi = Var("phPhi()",float),
        z0 = Var("phZ0()",float),
        d0 = Var("phD0()",float),
        charge  = Var("phCharge", int, doc="charge id"),

        ## hw Values
        hwPt = Var("hwPt()",int,doc="hardware pt"),
        hwEta = Var("hwEta()",int,doc="hardware eta"),
        hwPhi = Var("hwPhi()",int,doc="hardware phi"),
        hwQual = Var("hwQual()",int,doc="hardware qual"),
        hwIso = Var("hwIso()",int,doc="hardware iso"),
        hwBeta = Var("hwBeta()",int,doc="hardware beta"),

        # ## more info
        # nStubs = Var("stubs().size()",int,doc="number of stubs"),
    )
)

gmtTkMuTable = staMuTable.clone(
    src = cms.InputTag('l1tTkMuonsGmtLowPtFix','l1tTkMuonsGmtLowPtFix'),
    name = cms.string("L1gmtTkMuon"),
    doc = cms.string("GMT Tk Muons"),
)
# gmtTkMuTable.variables.nStubs = Var("stubs().size()",int,doc="number of stubs")

### Jets
sc4JetTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tSC4PFL1PuppiCorrectedEmulator'),
    cut = cms.string(""),
    name = cms.string("L1puppiJetSC4"),
    doc = cms.string("SeededCone 0.4 Puppi jet,  origin: Correlator"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1P3Vars,
        et = Var("et",float),
        z0 = Var("vz", float, "vertex z0"), ## empty
    )
)

sc8JetTable = sc4JetTable.clone(
    src = 'l1tSC8PFL1PuppiCorrectedEmulator',
    name = "L1puppiJetSC8",
    doc = "SeededCone 0.8 Puppi jet,  origin: Correlator"
)

sc4ExtJetTable = sc4JetTable.clone(
    src = cms.InputTag('l1tSC4PFL1PuppiExtendedCorrectedEmulator'),
    name = cms.string("L1puppiExtJetSC4"),
    doc = cms.string("SeededCone 0.4 Puppi jet from extended Puppi,  origin: Correlator"),
    externalVariables = cms.PSet(
        btagScore = ExtVar(cms.InputTag("l1tBJetProducerPuppiCorrectedEmulator", "L1PFBJets"),float, doc="NNBtag score"),
    ),
)

histoJetTable = sc4JetTable.clone(
    src = cms.InputTag("l1tPhase1JetCalibrator9x9trimmed" ,   "Phase1L1TJetFromPfCandidates"),
    name = cms.string("L1puppiJetHisto"),
    doc = cms.string("Puppi Jets histogrammed 9x9, trimmed, origin: Correlator"),
)


caloJetTable = sc4JetTable.clone(
    src = cms.InputTag("l1tCaloJet","L1CaloJetCollectionBXV"),
    name = cms.string("L1caloJet"),
    doc = cms.string("Calo Jets, origin: GCT"),
    cut = cms.string("pt > 5"), ## increase this to save space
)

### SUMS

puppiMetTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("l1tMETPFProducer",""),
    name = cms.string("L1puppiMET"),
    doc = cms.string("Puppi MET, origin: Correlator"),
    singleton = cms.bool(True), # the number of entries is variable
    variables = cms.PSet(
        l1PtVars,
        et = Var("et",float)
    )
)

sc4SumsTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("l1tSC4PFL1PuppiCorrectedEmulatorMHT",""),
    name = cms.string("L1puppiJetSC4sums"),
    doc = cms.string("HT and MHT from SeededCone Radius 0.8 jets; idx 0 is HT, idx 1 is MHT, origin: Correlator"),
    singleton = cms.bool(False), # the number of entries is not variable
    cut = cms.string(""),
    variables = cms.PSet(
        l1PtVars,
        #ht = Var("pt[0]", float)
    )
)

histoSumsTable = sc4SumsTable.clone(
    src = cms.InputTag("l1tPhase1JetSumsProducer9x9trimmed","Sums"),
    name = cms.string("L1puppiHistoJetSums"),
    doc = cms.string("HT and MHT from histogrammed 9x9 jets, origin: Correlator"),
    )


### Taus
caloTauTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("l1tCaloJet","L1CaloTauCollectionBXV"),
    cut = cms.string("pt > 5"),
    name = cms.string("L1caloTau"),
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
    name = cms.string("L1nnTau"),
    doc = cms.string("NN Taus"),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
        l1P3Vars,
        charge = Var("charge", int),
        z0 = Var("z0", float, "vertex z0"),                
        ## copy paste from old menu ntuple https://github.com/artlbv/cmssw/blob/from-CMSSW_12_5_2_patch1/L1Trigger/L1TNtuples/src/L1AnalysisPhaseIIStep1.cc#L543C1-L555C1
        chargedIso = Var("chargedIso", int),
        fullIso = Var("fullIso", int),
        id = Var("id", int),
        passLooseNN = Var("passLooseNN", int),
        passLoosePF = Var("passLoosePF", int),
        passTightPF = Var("passTightPF", int),
        passTightNN = Var("passTightNN", int),
        passLooseNNMass = Var("passLooseNNMass", int),
        passTightNNMass = Var("passTightNNMass", int),
        passMass = Var("passMass", int),
        dXY = Var("dxy", float),
    )
)

## L1 Objects
p2L1TablesTask = cms.Task(
    ## Muons
    gmtTkMuTable,
    staMuTable,
    ## EG
    tkEleTable,
    tkPhotonTable,
    staEGmerged, staEGTable, ## Need to run merger before Table task! Stanalone EG – not in GT yet
    staEGebTable, staEGeeTable,
    # ## jets
    sc4JetTable,
    sc8JetTable,
    sc4ExtJetTable, 
    histoJetTable,
    caloJetTable,
    # ## sums
    puppiMetTable,
    sc4SumsTable,
    histoSumsTable,
    # taus
    caloTauTable,
    nnTauTable,
    # GTT
    vtxTable,
    pvtxTable,
)
