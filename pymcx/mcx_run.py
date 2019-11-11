# -*- coding: utf-8 -*-

def run(cfg, flag, mcxbin = './mcx'):

	"""
	input:
		cfg:
			mcx config json file for the simulation as a python dictionary
		
		flag:
			flag for runing mcx
			
		mcxbin:
			path for the mcx binary

	output:
		mch_data:
	"""

	import os
	import json
	import pymcx as mcx
	
	SID = cfg['Session']['ID']

	f = open(SID+'.json', 'w')
	f.write(json.dumps(cfg, sort_keys=True, indent=2))
	f.close()

	os.system(mcxbin+' -f '+SID+'.json '+flag)


	mch = []
	mc2 = []


	if os.isfile(SID+'.mch'):
		mch = mcx.loadmch(SID+'.mch')

	if os.isfile(SID+'.mc2'):
		dt = round((cfg["Forward"]["T1"] - cfg["Forward"]["T0"])/cfg["Forward"]["Dt"])
		mc2 = mcx.loadmc2(SID+'.mc2',cfg["Shapes"]["Size"]+[dt])


	return mch, mc2