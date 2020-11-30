# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: cmsDriver.py my_etabjj_cfi.py --fileout file:etabJJ-GEN.root -s GEN,SIM --mc --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2017Collision --conditions 94X_mc2017_realistic_v17 --eventcontent RAWSIM --era Run2_2017 --python_filename etabJJ_pythia8_2017_cfg.py --no_exec -n 1000
import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(@@local_Nevent@@)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('EtaB --> J/psi J/psi, 13TeV, Tune CUETP8M1'),
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: my_etabJJ_cfi.py $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:@@out_name@@.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v17', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    crossSection = cms.untracked.double(1.0),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
@@pythia8_config_text@@
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
            )
    )
)

process.FourMuonFilter = cms.EDFilter("FourLepFilter", # require 4-mu in the final state
        MinPt = cms.untracked.double(1.8),
        MaxPt = cms.untracked.double(4000.0),
        MaxEta = cms.untracked.double(2.5),
        MinEta = cms.untracked.double(0.),
        ParticleID = cms.untracked.int32(13)
)

process.DiJpsiFilter = cms.EDFilter("MCParticlePairFilter",  # require 2-mu mass to be 8.5 - 11.5 GeV
        MinPt = cms.untracked.vdouble(1.0,1.0),
        MaxPt = cms.untracked.vdouble(4000.0,4000.0),
        MaxEta = cms.untracked.vdouble( 2.5,2.5),
        MinEta = cms.untracked.vdouble(-2.5,-2.5),
        ParticleID1 = cms.untracked.vint32(443, -443),
        ParticleID2 = cms.untracked.vint32(443, -443),
        MinInvMass = cms.untracked.double(1.0),
        MaxInvMass = cms.untracked.double(16.0),
)

process.ProductionFilterSequence = cms.Sequence(process.generator+process.FourMuonFilter)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
