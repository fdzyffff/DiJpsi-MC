import os
import collections

class template_instruction():
      def __init__(self, name):
            self.name = name
            self.out_name = "%s-GENSIM"%(name)
            self.pythia8_config_text = ""
            self.local_Nevent = 100
            self.crab_Njob = 1000
            self.crab_Nevent = 1000
            self.temp_dir = "template"
            self.temp_config_name = "template/template"
            self.temp_crab_name = "template/template_crab"
            self.temp_readme_name = "template/template_readme"
            self.extra_line = ""
            self.file_list = []


      def print_info(self):
            print ("#"*30)
            print ("name : %s"%(self.name))
            print ("out_name : %s.root"%(self.out_name))
            print ("pythia8_config_text : %s"%(self.pythia8_config_text))
            print ("crab_Njob : %s"%(self.crab_Njob))
            print ("crab_Nevent : %s"%(self.crab_Nevent))


process_dic = collections.OrderedDict()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("DPStoJJ")
tmp_t.pythia8_config_text = """
            'Charmonium:gg2ccbar(3S1)[3S1(1)]g = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[3S1(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on,off',
            'Charmonium:gg2ccbar(3S1)[1S0(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[1S0(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[1S0(8)]g = on,off',
            'Charmonium:gg2ccbar(3S1)[3PJ(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[3PJ(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3PJ(8)]g = on,off',
#           'Charmonium:all = on',
            'SecondHard:generate = on',
            'SecondHard:Charmonium = on',
            'PhaseSpace:pTHatMin = 1.',      
            '100443:onMode = off', # Others
            '10441:onMode = off',
            '20443:onMode = off',
            '443:onMode = off',
            '443:onIfMatch = -13 13',
            'PartonLevel:MPI = on',              #! no multiparton interactions
            'PartonLevel:ISR = on',              #! no initial-state radiation
            'PartonLevel:FSR = on',              #! no final-state radiation
            'HadronLevel:all = on',              #! continue after parton level
            'HadronLevel:Hadronize = on',        #! no hadronization
            'HadronLevel:Decay = on',            #! no decays
"""
tmp_t.local_Nevent = 10000
tmp_t.crab_Njob = 3000
tmp_t.crab_Nevent = 100000 # 1/10000
process_dic[tmp_t.name] = tmp_t

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("DPStoJY")
tmp_t.pythia8_config_text = """
            'Charmonium:gg2ccbar(3S1)[3S1(1)]g = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[3S1(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on,off',
            'Charmonium:gg2ccbar(3S1)[1S0(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[1S0(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[1S0(8)]g = on,off',
            'Charmonium:gg2ccbar(3S1)[3PJ(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[3PJ(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3PJ(8)]g = on,off',
#           'Charmonium:all = on',
            'SecondHard:generate = on',
            'SecondHard:bottomonium = on',
#           'PhaseSpace:mHatMin = 10.',
            'PhaseSpace:pTHatMin = 1.',
#           'PhaseSpace:pTHatMinSecond = 1.',
#           'PhaseSpace:pTHatMinDiverge = 0.1',
            '100443:onMode = off', # Others
            '10441:onMode = off',
            '20443:onMode = off',
            '445:onMode = off',
            '443:onMode = off', # J/psi
            '443:onMode = off',
            '443:onIfMatch = -13 13',
            '553:onMode = off',
            '553:onIfMatch = -13 13',
            'PartonLevel:MPI = on',              #! no multiparton interactions
            'PartonLevel:ISR = on',              #! no initial-state radiation
            'PartonLevel:FSR = on',              #! no final-state radiation
            'HadronLevel:all = on',              #! continue after parton level
            'HadronLevel:Hadronize = on',        #! no hadronization
            'HadronLevel:Decay = on',            #! no decays
"""
tmp_t.local_Nevent = 1000
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 100000 #11/10000
process_dic[tmp_t.name] = tmp_t

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("DPStoPsi2SJ")
tmp_t.pythia8_config_text = """
            'Charmonium:gg2ccbar(3S1)[3S1(1)]g = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[3S1(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on,off',
            'Charmonium:gg2ccbar(3S1)[1S0(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[1S0(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[1S0(8)]g = on,off',
            'Charmonium:gg2ccbar(3S1)[3PJ(8)]g = on,off',
            'Charmonium:qg2ccbar(3S1)[3PJ(8)]q = on,off',
            'Charmonium:qqbar2ccbar(3S1)[3PJ(8)]g = on,off',
#           'Charmonium:all = on',
            'SecondHard:generate = on',
            'SecondHard:Charmonium = on',
#           'PhaseSpace:mHatMin = 10.',
            'PhaseSpace:pTHatMin = 1.',      
#           'PhaseSpace:pTHatMinSecond = 1.',
#           'PhaseSpace:pTHatMinDiverge = 0.1',
            '10441:onMode = off',
            '20443:onMode = off',
            '443:onMode = off',
            '443:onIfMatch = -13 13',
            '100443:onMode = off',
            '100443:onIfMatch = -13 13',
            'PartonLevel:MPI = on',              #! no multiparton interactions
            'PartonLevel:ISR = on',              #! no initial-state radiation
            'PartonLevel:FSR = on',              #! no final-state radiation
            'HadronLevel:all = on',              #! continue after parton level
            'HadronLevel:Hadronize = on',        #! no hadronization
            'HadronLevel:Decay = on',            #! no decays
"""
tmp_t.local_Nevent = 10000
tmp_t.crab_Njob = 3000
tmp_t.crab_Nevent = 100000 #1/10000
process_dic[tmp_t.name] = tmp_t


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("DPStoYY")
tmp_t.pythia8_config_text = """
#           'Charmonium:gg2ccbar(3S1)[3S1(1)]g = on,off',
#           'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on,off',
            'Bottomonium:all = on',
            'SecondHard:generate = on',
            'SecondHard:bottomonium = on',
#           'PhaseSpace:mHatMin = 10.',
            'PhaseSpace:pTHatMin = 1.',
#           'PhaseSpace:pTHatMinSecond = 1.',
#           'PhaseSpace:pTHatMinDiverge = 0.1',
            '553:onMode = off',
            '553:onIfMatch = -13 13',
            'PartonLevel:MPI = on',              #! no multiparton interactions
            'PartonLevel:ISR = on',              #! no initial-state radiation
            'PartonLevel:FSR = on',              #! no final-state radiation
            'HadronLevel:all = on',              #! continue after parton level
            'HadronLevel:Hadronize = on',        #! no hadronization
            'HadronLevel:Decay = on',            #! no decays
"""
tmp_t.local_Nevent = 1000
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 10000 #11/1000
process_dic[tmp_t.name] = tmp_t


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("SPStoJJ_Direct")
tmp_t.pythia8_config_text = """
            'Charmonium:gg2doubleccbar(3S1)[3S1(1)] = on,off,off',
            'Charmonium:qqbar2doubleccbar(3S1)[3S1(1)] = on,off,off',
            'Charmonium:states(3S1)1  = 443,443,100443',
            'Charmonium:states(3S1)2  = 443,100443,100443',
            '443:onMode = off',
            '443:onIfMatch = 13 -13',
            'PhaseSpace:pTHatMin = 1.'
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',   #off
            'HadronLevel:all = on',
            'HadronLevel:Hadronize = on',
            'HadronLevel:Decay = on',
"""
tmp_t.local_Nevent = 100
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 2000 #5/100
process_dic[tmp_t.name] = tmp_t


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("SPStoJJ_Feeddown")
tmp_t.pythia8_config_text = """
            'Charmonium:gg2doubleccbar(3S1)[3S1(1)] = off,on,on',
            'Charmonium:qqbar2doubleccbar(3S1)[3S1(1)] = off,on,on',
            'Charmonium:states(3S1)1  = 443,443,100443',
            'Charmonium:states(3S1)2  = 443,100443,100443',
            '443:onMode = off',
            '443:onIfMatch = 13 -13',
            'PhaseSpace:pTHatMin = 1.'
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',   #off
            'HadronLevel:all = on',
            'HadronLevel:Hadronize = on',
            'HadronLevel:Decay = on',
"""
tmp_t.local_Nevent = 100
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 2000 #5/100
process_dic[tmp_t.name] = tmp_t


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("SPStoPsi2SJ")
tmp_t.pythia8_config_text = """
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
"""
tmp_t.local_Nevent = 100
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 2000 #5/100
process_dic[tmp_t.name] = tmp_t


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("SPStoYY")
tmp_t.pythia8_config_text = """
            'Bottomonium:gg2doublebbbar(3S1)[3S1(1)]= on,on,on,on,on,on',
            'Bottomonium:qqbar2doublebbbar(3S1)[3S1(1)] = on,on,on,on,on,on',
            'Bottomonium:states(3S1)1    = 553,553,553,100553,100553,200553',
            'Bottomonium:states(3S1)2    = 553,100553,200553,100553,200553,200553',
            '553:onMode = off',
            '553:onIfMatch = 13 -13',
            'PhaseSpace:pTHatMin = 1.'
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',   #off
            'HadronLevel:all = on',
            'HadronLevel:Hadronize = on',
            'HadronLevel:Decay = on',
"""
tmp_t.local_Nevent = 100
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 500 #27/100
process_dic[tmp_t.name] = tmp_t


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("BBartoJJ")
tmp_t.pythia8_config_text = """
            'SoftQCD:nonDiffractive = off', #on
            #'PTFilter:filter = on',
            #'PTFilter:quarkToFilter = 5',
            #'PTFilter:scaleToFilter = 1.0'
            'HardQCD:hardbbbar = on',
            '443:onMode = off',
            '443:onIfMatch = 13 13',
            'PartonLevel:MPI = on',              #! no multiparton interactions
            'PartonLevel:ISR = on',              #! no initial-state radiation
            'PartonLevel:FSR = on',              #! no final-state radiation
            'HadronLevel:all = on',              #! continue after parton level
            'HadronLevel:Hadronize = on',        #! no hadronization
            'HadronLevel:Decay = on',            #! no decays
"""
tmp_t.local_Nevent = 100
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 1000
tmp_t.temp_dir = "template/BBartoJJ"
tmp_t.temp_config_name = "template/BBartoJJ/template_BBartoJJ"
tmp_t.temp_crab_name = "template/BBartoJJ/template_BBartoJJ_crab"
tmp_t.temp_readme_name = "template/BBartoJJ/template_readme"
tmp_t.file_list.append("myBBartoJpsi.dec")
tmp_t.extra_line = "#if run locally, replace the input file str '../myBBartoJpsi.dec' with 'myBBartoJpsi.dec' "
process_dic[tmp_t.name] = tmp_t


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tmp_t = template_instruction("EtabtoJJ")
tmp_t.pythia8_config_text = """
            'Bottomonium:gg2bbbar(3PJ)[3PJ(1)]g = on,off,off',
            #'Bottomonium:qqbar2bbbar(3PJ)[3PJ(1)]g = on,off,off',
            'Bottomonium:states(3PJ) = 10551,20553,555',
            #'10551:m0 = 9399.0'
            '10551:oneChannel = 1 1.0 0 443 443',
            '443:onMode = off',
            '443:onIfMatch = 13 -13',
            #'PhaseSpace:pTHatMin = 1.'
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',   #off
            'HadronLevel:all = on',
            'HadronLevel:Hadronize = on',
            'HadronLevel:Decay = on',

"""
tmp_t.local_Nevent = 100
tmp_t.crab_Njob = 1000
tmp_t.crab_Nevent = 1000
process_dic[tmp_t.name] = tmp_t

