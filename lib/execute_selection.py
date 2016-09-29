# -*- coding: utf-8 -*-
from .read_selection import read_selection
import os
import time
from .exe_deco import exe_deco
from .write_log import write_log
from utils.utils import str_2_tuple
from utils.utils import get_local_time
from utils.utils import get_specific_time
from generate_result import generate_result

def execute_selection():
	selection = read_selection()
	genTime = get_local_time()
	resultFileName = genTime+' test_result.csv'
	autyPath = os.getcwd()
	resultFilePath = os.path.join(autyPath,'results',resultFileName)
	generate_result(resultFilePath,('scriptPath','detail','startTime','endTime','duration'))
	for scriptPath in selection:
		result = str_2_tuple(scriptPath)
		startTime = get_specific_time()
		ret,result2 = execute_script(scriptPath)
		endTime = get_specific_time()
		duration = (endTime-startTime).microseconds*0.000001
		result = result+result2+str_2_tuple(startTime)+str_2_tuple(endTime)+str_2_tuple(duration)
		generate_result(resultFilePath,result)

@exe_deco
def execute_script(scriptPath):
	write_log('execute_script: '+scriptPath)
	os.system('python '+scriptPath)