from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SPStoYY_GENSIM'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'BPH_SPStoYY_2017.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'Pythia8_SPStoYY'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 1000   # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.outputDatasetTag = 'MC2017_Pythia_SPStoYY_v1' # Change here with your lxplus name

config.section_('Site')
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_CN_Beijing'
config.Data.outLFNDirBase = '/store/user/XXXXXXXXX/MC2017/v1/'  # Change here with your lxplus name