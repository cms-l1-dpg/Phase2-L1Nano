# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --conditions 131X_mcRun4_realistic_v5 -n 2 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT -s RAW2DIGI,L1:RUNP2GT --datatier GEN-SIM-DIGI-RAW-MINIAOD --fileout file:test.root --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2.addHcalTriggerPrimitives,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT --geometry Extended2026D95  
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9

process = cms.Process('L1',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D95Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
# process.load('L1Trigger.Phase2L1GT.l1tGTProducer_cff')
process.load('L1Trigger.Phase2L1GT.l1tGTMenu_hadr_metSeeds_cff')
process.load('L1Trigger.Phase2L1GT.l1tGTMenu_lepSeeds_cff')
process.load('L1Trigger.Phase2L1GT.l1tGTAlgoBlockProducer_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    ## Full samples
        "/store/mc/Phase2Spring23DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30000/0074b621-ce6a-4f66-8536-729c401b09a4.root",
        "/store/mc/Phase2Spring23DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30001/b4bddcdb-25e1-4193-b125-a8e1c8f64384.root",
        "/store/mc/Phase2Spring23DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30000/e77e895d-2cd7-41a9-a035-cc1457c0a1a3.root",
        "/store/mc/Phase2Spring23DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30000/e089e52e-9461-4339-809c-329acef008d6.root",
        "/store/mc/Phase2Spring23DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30001/061b4e8c-acd1-4a52-9026-3a6757ad6e9d.root",
        "/store/mc/Phase2Spring23DIGIRECOMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30001/5bad5ebd-c5f3-43dd-aedf-54c4a3b92ed3.root",
    ),
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop l1tPFJets_*_*_*',
        'drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    #FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    #SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:2'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-MINIAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:/tmp/alobanov/test.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun4_realistic_v5', '')
process.FEVTDEBUGHLToutput.outputCommands.append('keep *P2GT*_*_*_*')
process.FEVTDEBUGHLToutput.outputCommands.append('drop l1tPFJets_*_*_*')

### Fix GT producer with new vertex name
import FWCore.ParameterSet.Config as cms
from L1Trigger.Phase2L1GT.l1tGTScales import scale_parameter

process.l1tGTProducer = cms.EDProducer(
    "L1GTProducer",
    scales=scale_parameter,
    GTTPromptJets = cms.InputTag("l1tTrackJetsEmulation", "L1TrackJets"),
    GTTDisplacedJets = cms.InputTag("l1tTrackJetsExtendedEmulation", "L1TrackJetsExtended"),
    GTTPrimaryVert = cms.InputTag("l1tVertexFinderEmulator", "L1VerticesEmulation"),
    GMTSaPromptMuons = cms.InputTag("l1tSAMuonsGmt", "promptSAMuons"),
    GMTSaDisplacedMuons = cms.InputTag("l1tSAMuonsGmt", "displacedSAMuons"),
    GMTTkMuons = cms.InputTag("l1tTkMuonsGmtLowPtFix", "l1tTkMuonsGmtLowPtFix"),
    CL2Jets = cms.InputTag("l1tSCPFL1PuppiCorrectedEmulator"),
    CL2Electrons = cms.InputTag("l1tLayer2EG", "L1CtTkElectron"),
    CL2Photons = cms.InputTag("l1tLayer2EG", "L1CtTkEm"),
    CL2Taus = cms.InputTag("l1tNNTauProducerPuppi", "L1PFTausNN"),
    CL2EtSum = cms.InputTag("l1tMETPFProducer"),
    CL2HtSum = cms.InputTag("l1tSCPFL1PuppiCorrectedEmulatorMHT")
)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.Phase2L1GTProducer = cms.Path(process.l1tGTProducer)
process.pPuppiHT400 = cms.Path(process.PuppiHT400)
process.pPuppiHT450 = cms.Path(process.PuppiHT450)
process.pPuppiMET200 = cms.Path(process.PuppiMET200)
process.pQuadJet70_55_40_40 = cms.Path(process.QuadJet70554040)
process.pSinglePuppiJet230 = cms.Path(process.SinglePuppiJet230)
process.pDoubleEGEle37_24 = cms.Path(process.DoubleEGEle3724)
process.pDoubleIsoTkPho22_12 = cms.Path(process.DoubleIsoTkPho2212)
process.pDoublePuppiTau52_52 = cms.Path(process.DoublePuppiTau5252)
process.pDoubleTkEle25_12 = cms.Path(process.DoubleTkEle2512)
process.pDoubleTkMuon15_7 = cms.Path(process.DoubleTkMuon157)
process.pIsoTkEleEGEle22_12 = cms.Path(process.IsoTkEleEGEle2212)
process.pSingleEGEle51 = cms.Path(process.SingleEGEle51)
process.pSingleIsoTkEle28 = cms.Path(process.SingleIsoTkEle28)
process.pSingleIsoTkPho36 = cms.Path(process.SingleIsoTkPho36)
process.pSingleTkEle36 = cms.Path(process.SingleTkEle36)
process.pSingleTkMuon22 = cms.Path(process.SingleTkMuon22)
process.pTripleTkMuon5_3_3 = cms.Path(process.TripleTkMuon533)
process.Phase2L1GTAlgoBlockProducer = cms.Path(process.l1tGTAlgoBlockProducer)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

## NTUPLERS

## GT ntupler
# process.load('L1Trigger.Configuration.GTemulator_cff')
# process.GTemulation_step = cms.Path(process.GTemulator)

process.GToutput = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *P2GT*_*_*_L1',
    ),
    fileName=cms.untracked.string("l1t_emulation.root")
)

process.pGToutput = cms.EndPath(process.GToutput)

## NANO
process.load('PhysicsTools.L1Nano.l1Ph2Nano_cff')

process.outnano = cms.OutputModule("NanoAODOutputModule",
                                   fileName = cms.untracked.string("perfNano_Ph2Menu.root"),
                                   outputCommands = cms.untracked.vstring("drop *", "keep nanoaodFlatTable_*Table_*_*"),
                                   compressionLevel = cms.untracked.int32(4),
                                   compressionAlgorithm = cms.untracked.string("ZLIB"),
)
process.end = cms.EndPath(process.outnano)

process.schedule = cms.Schedule(
    process.raw2digi_step,
    process.L1simulation_step,
    ## GT
    process.Phase2L1GTProducer,
    process.Phase2L1GTAlgoBlockProducer,
    ## GT algos
    process.pPuppiHT400,process.pPuppiHT450,
    process.pPuppiMET200,process.pQuadJet70_55_40_40,
    process.pSinglePuppiJet230,process.pDoubleEGEle37_24,
    process.pDoubleIsoTkPho22_12,process.pDoublePuppiTau52_52,
    process.pDoubleTkEle25_12,process.pDoubleTkMuon15_7,process.pIsoTkEleEGEle22_12,
    process.pSingleEGEle51,process.pSingleIsoTkEle28,
    process.pSingleIsoTkPho36,process.pSingleTkEle36,process.pSingleTkMuon22,process.pTripleTkMuon5_3_3,
    ## GT ntuple
    # process.pGToutput,
    process.endjob_step,
    # process.FEVTDEBUGHLToutput_step,
    process.end,
    tasks = [
        process.p2L1TablesTask
    ],
)

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2
from L1Trigger.Configuration.customisePhase2 import addHcalTriggerPrimitives 

#call to customisation function addHcalTriggerPrimitives imported from L1Trigger.Configuration.customisePhase2
process = addHcalTriggerPrimitives(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT
from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT import customisePhase2FEVTDEBUGHLT 

#call to customisation function customisePhase2FEVTDEBUGHLT imported from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT
process = customisePhase2FEVTDEBUGHLT(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
