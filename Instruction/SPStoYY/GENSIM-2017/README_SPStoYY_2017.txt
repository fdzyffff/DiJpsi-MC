path:
/afs/cern.ch/user/x/xgao/public/Di-Jpsi/Instruction/

There are 9 processes
DPStoJJ
DPStoJY
DPStoPsi2SJ
DPStoYY
SPStoJJ
SPStoPsi2SJ
SPStoYY
BBartoJJ
EtabtoJJ (preliminary signal mc)

I will introduce procedure of 2017 SPStoYY here
PS: the difference between this generation and Prof. Hu ZHen's is: he use LHE file, so in his step 1 and step 2, he transfers LHE file to root file, and runs GEN-SIM at step 3. BUT in this generation procedure, we will produce events directly at GEN-SIM step, so we can follow his nice instruction from step4 :)

our step 1
#setup the CMSSW
ssh -Y XXXX@lxslc7.ihep.ac.cn (ssh -Y XXXX@lxplus.cern.ch)
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
cd work
mkdir PrivateMC
cd PrivateMC
cmsrel CMSSW_9_4_2
cd CMSSW_9_4_2/src/
cmsenv
mkdir mypythia_crab
cd mypythia_crab
cp -r /afs/cern.ch/user/x/xgao/public/Di-Jpsi/Instruction ./
cd Instruction/SPStoYY/GENSIM-2017
ls

our step 2
#run locally first to check

cmsRun BPH_SPStoYY_2017.py
#modify the crab3_etabJJ_GEN.py and then submit jobs to crab3
#please note that, you have to modify config.Data.unitsPerJob according to efficiency, to make sure there are less than 1000 events in each job. (i.e., if efficiency is ~0.01, you should set config.Data.unitsPerJob = 100000 or smaller value, or the job will be very slow and in risk of failure)
crab submit -c crab_BPH_SPStoYY_2017.py

our step 3
follow Zhen's instruction to go rest steps, the DIGI-RAW and RECO






