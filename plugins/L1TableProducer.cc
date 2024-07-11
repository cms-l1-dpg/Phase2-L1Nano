#include "PhysicsTools/NanoAOD/interface/SimpleFlatTableProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

// P2GT objects
#include "DataFormats/L1Trigger/interface/P2GTAlgoBlock.h"
typedef SimpleFlatTableProducer<l1t::P2GTAlgoBlock> P2GTAlgoBlockFlatTableProducer;
DEFINE_FWK_MODULE(P2GTAlgoBlockFlatTableProducer);

#include "DataFormats/L1Trigger/interface/P2GTCandidate.h"
typedef SimpleFlatTableProducer<l1t::P2GTCandidate> P2GTCandidateFlatTableProducer;
DEFINE_FWK_MODULE(P2GTCandidateFlatTableProducer);

// GMT objects
#include "DataFormats/L1TMuonPhase2/interface/TrackerMuon.h"
typedef SimpleFlatTableProducer<l1t::TrackerMuon> L1TrackerMuonFlatTableProducer;
DEFINE_FWK_MODULE(L1TrackerMuonFlatTableProducer);

#include "DataFormats/L1TMuonPhase2/interface/SAMuon.h"
typedef SimpleFlatTableProducer<l1t::SAMuon> L1SAMuonFlatTableProducer;
DEFINE_FWK_MODULE(L1SAMuonFlatTableProducer);

// Correlator
#include "DataFormats/L1TCorrelator/interface/TkElectron.h"
typedef SimpleFlatTableProducer<l1t::TkElectron> L1TkElectronFlatTableProducer;
DEFINE_FWK_MODULE(L1TkElectronFlatTableProducer);

#include "DataFormats/L1TCorrelator/interface/TkEm.h"
typedef SimpleFlatTableProducer<l1t::TkEm> L1TkEmFlatTableProducer;
DEFINE_FWK_MODULE(L1TkEmFlatTableProducer);

#include "DataFormats/L1TParticleFlow/interface/PFJet.h"
typedef SimpleFlatTableProducer<l1t::PFJet> SimpleL1PFJetFlatTableProducer;
DEFINE_FWK_MODULE(SimpleL1PFJetFlatTableProducer);

#include "DataFormats/L1TParticleFlow/interface/PFTau.h"
typedef SimpleFlatTableProducer<l1t::PFTau> SimpleL1PFTauFlatTableProducer;
DEFINE_FWK_MODULE(SimpleL1PFTauFlatTableProducer);

#include "DataFormats/L1Trigger/interface/EtSum.h"
typedef SimpleFlatTableProducer<l1t::EtSum> SimpleL1EtSumFlatTableProducer;
DEFINE_FWK_MODULE(SimpleL1EtSumFlatTableProducer);

// GTT objects
#include "DataFormats/L1Trigger/interface/VertexWord.h"
typedef SimpleFlatTableProducer<l1t::VertexWord> SimpleL1VtxWordCandidateFlatTableProducer;
DEFINE_FWK_MODULE(SimpleL1VtxWordCandidateFlatTableProducer);

#include "DataFormats/L1Trigger/interface/TkJetWord.h"
typedef SimpleFlatTableProducer<l1t::TkJetWord> SimpleL1TkJetWordCandidateFlatTableProducer;
DEFINE_FWK_MODULE(SimpleL1TkJetWordCandidateFlatTableProducer);

#include "DataFormats/L1Trigger/interface/TkTripletWord.h"
typedef SimpleFlatTableProducer<l1t::TkTripletWord> SimpleTkTripletWordCandidateFlatTableProducer;
DEFINE_FWK_MODULE(SimpleTkTripletWordCandidateFlatTableProducer);



