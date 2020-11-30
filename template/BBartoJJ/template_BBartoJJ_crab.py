from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '@@name@@_GENSIM'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '@@file_name@@'
config.JobType.allowUndistributedCMSSW = True
config.JobType.inputFiles = ['myBBartoJpsi.dec']

config.Data.outputPrimaryDataset = 'Pythia8_@@name@@'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = @@crab_Njob@@
NJOBS = @@crab_Nevent@@   # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.outputDatasetTag = 'MC@@year@@_Pythia_@@name@@_v1' # Change here with your lxplus name

config.section_('Site')
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_CN_Beijing'
config.Data.outLFNDirBase = '/store/user/XXXXXXXXX/MC@@year@@/v1/'  # Change here with your lxplus name