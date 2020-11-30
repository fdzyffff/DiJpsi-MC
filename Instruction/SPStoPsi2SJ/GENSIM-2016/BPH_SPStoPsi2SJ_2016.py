# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: cmsDriver.py my_etabJJ_cfi.py --fileout file:etabJJ-GEN.root --mc --eventcontent RAWSIM --era Run2_2016 --datatier GEN-SIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v8 --beamspot Realistic50ns13TeVCollision --step GEN,SIM --python_filename etabJJ_pythia8_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

process = cms.Process('SIM')

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
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
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
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:SPStoPsi2SJ-GENSIM.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    crossSection = cms.untracked.double(1.0),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'Charmonium:gg2doubleccbar(3S1)[3S1(1)] = off,on,off',
            'Charmonium:qqbar2doubleccbar(3S1)[3S1(1)] = off,on,off',
            'Charmonium:states(3S1)1  = 443,443,100443',
            'Charmonium:states(3S1)2  = 443,100443,100443',
            '443:onMode = off',
            '443:onIfMatch = 13 -13',
            '100443:onMode = off',
            '100443:onIfMatch = 13 -13',
            'PhaseSpace:pTHatMin = 1.'
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',   #off
            'HadronLevel:all = on',
            'HadronLevel:Hadronize = on',
            'HadronLevel:Decay = on',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
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
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

