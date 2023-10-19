#include "PhysicsTools/NanoAOD/interface/SimpleFlatTableProducer.h"

#include "DataFormats/L1Trigger/interface/VertexWord.h"
typedef SimpleFlatTableProducer<l1t::VertexWord> SimpleL1VtxWordCandidateFlatTableProducer;

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SimpleL1VtxWordCandidateFlatTableProducer);