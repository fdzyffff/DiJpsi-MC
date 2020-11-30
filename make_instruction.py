from input_card import *

def make_instruction(process_in, year):
	if year not in ["2016", "2017", "2018"]:
		print ("Wrong year : %s"%(year))
		return


	out_dir = "Instruction/%s/GENSIM-%s"%(process_in.name, year)
	# write configure file:
	file_name = "BPH_%s_%s.py"%(process_in.name, year)
	os.system("mkdir -p %s"%(out_dir))

	f_config_temp = open("%s_%s.py"%(process_in.temp_config_name, year))
	f_config_out = open(os.path.join(out_dir,file_name), "w")

	for line in f_config_temp:
		#print (line)
		out_line = line.replace("\r\n","\n")
		out_line = out_line.replace("@@local_Nevent@@",str(process_in.local_Nevent))
		out_line = out_line.replace("@@out_name@@",process_in.out_name)
		out_line = out_line.replace("@@pythia8_config_text@@",process_in.pythia8_config_text[1:-1])
		f_config_out.write(out_line)

	f_config_temp.close()
	f_config_out.close()

	# write crab file:
	crab_name = "crab_BPH_%s_%s.py"%(process_in.name, year)
	os.system("mkdir -p %s"%(out_dir))

	f_config_temp = open("%s.py"%(process_in.temp_crab_name))
	f_config_out = open(os.path.join(out_dir,crab_name), "w")

	for line in f_config_temp:
		#print (line)
		out_line = line.replace("\r\n","\n")
		out_line = out_line.replace("@@year@@",year)
		out_line = out_line.replace("@@name@@",process_in.name)
		out_line = out_line.replace("@@file_name@@",file_name)
		out_line = out_line.replace("@@crab_Njob@@",str(process_in.crab_Njob))
		out_line = out_line.replace("@@crab_Nevent@@",str(process_in.crab_Nevent))
		out_line = out_line.replace("@@extra_line@@",process_in.extra_line)
		f_config_out.write(out_line)

	f_config_temp.close()
	f_config_out.close()

	# write readme file:
	readme_name = "README_%s_%s.txt"%(process_in.name, year)
	os.system("mkdir -p %s"%(out_dir))

	f_config_temp = open("%s_%s.txt"%(process_in.temp_readme_name,year))
	f_config_out = open(os.path.join(out_dir,readme_name), "w")

	for line in f_config_temp:
		#print (line)
		out_line = line.replace("\r\n","\n")
		out_line = out_line.replace("@@year@@",year)
		out_line = out_line.replace("@@name@@",process_in.name)
		out_line = out_line.replace("@@crab_name@@",crab_name)
		out_line = out_line.replace("@@file_name@@",file_name)
		out_line = out_line.replace("@@extra_line@@",process_in.extra_line)
		f_config_out.write(out_line)

	f_config_temp.close()
	f_config_out.close()

	for file_name in process_in.file_list:
		os.system("cp %s %s"%(os.path.join(process_in.temp_dir,file_name), out_dir))


for process_in in process_dic:
	make_instruction(process_dic[process_in], "2016")
	make_instruction(process_dic[process_in], "2017")
	make_instruction(process_dic[process_in], "2018")