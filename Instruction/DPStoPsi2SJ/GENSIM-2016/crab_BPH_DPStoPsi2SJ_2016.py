from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DPStoPsi2SJ_GENSIM'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'BPH_DPStoPsi2SJ_2016.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'Pythia8_DPStoPsi2SJ'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100000
NJOBS = 3000   # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.outputDatasetTag = 'MC2016_Pythia_DPStoPsi2SJ_v1' # Change here with your lxplus name

config.section_('Site')
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_CN_Beijing'
config.Data.outLFNDirBase = '/store/user/XXXXXXXXX/MC2016/v1/'  # Change here with your lxplus name