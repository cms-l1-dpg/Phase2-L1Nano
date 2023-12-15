#include "PhysicsTools/NanoAOD/interface/SimpleFlatTableProducer.h"

#include "DataFormats/L1Trigger/interface/VertexWord.h"
typedef SimpleFlatTableProducer<l1t::VertexWord> SimpleL1VtxWordCandidateFlatTableProducer;

#include "DataFormats/L1Trigger/interface/P2GTAlgoBlock.h"
typedef SimpleFlatTableProducer<l1t::P2GTAlgoBlock> P2GTAlgoBlockFlatTableProducer;

#include "DataFormats/L1Trigger/interface/TkJetWord.h"
typedef SimpleFlatTableProducer<l1t::TkJetWord> SimpleL1TkJetWordCandidateFlatTableProducer;

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SimpleL1VtxWordCandidateFlatTableProducer);
DEFINE_FWK_MODULE(P2GTAlgoBlockFlatTableProducer);
DEFINE_FWK_MODULE(SimpleL1TkJetWordCandidateFlatTableProducer);
