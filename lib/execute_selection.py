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
import subprocess

def execute_selection():
	#Read selection.
	selection = read_selection()
	genTime = get_local_time()
	resultFileName = genTime+' test_result'
	resultFileName = resultFileName.replace(':','_')
	#autyPath = os.getcwd()
	autyPath = os.path.dirname(os.path.dirname(__file__))
	#Save the auty path into file.
	pathFilePath = os.path.join(autyPath,'utils','root_path.py')
	writeContent = '# -*- coding: utf-8 -*-\n'+'autyPath=\''+autyPath+'\''
	open(pathFilePath,'w').write(writeContent)
	#Result generation.
	resultFilePath = os.path.join(autyPath,'results',resultFileName)
	generate_result(resultFilePath,('scriptPath','detail','startTime','endTime','duration','result'))
	for scriptPath in selection:
		result = str_2_tuple(scriptPath)
		startTime = get_specific_time()
		#Execution of scripts.
		ret,result2 = execute_script(scriptPath,autyPath)
		endTime = get_specific_time()
		duration = (endTime-startTime).microseconds*0.000001
		#Generation of results.
		result = result+result2+str_2_tuple(startTime)+str_2_tuple(endTime)+str_2_tuple(duration)+str_2_tuple(ret)
		generate_result(resultFilePath,result)

@exe_deco
def execute_script(scriptPath,autyPath):
	#Auto-created code.
	with open(scriptPath,'r') as original:
		data = original.read()
	with open(scriptPath,'w') as modified:
		autyCode = '# -*- coding: utf-8 -*-\nimport os\nimport sys\nsys.path.append("'+autyPath+'")\n'
		modified.write(autyCode+data)
	#Execute script.
	write_log('execute_script: '+scriptPath)
	print 'execute_script: '+scriptPath
	stdout,stderr = subprocess.Popen(['python',scriptPath],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	r = stdout+stderr
	print r
	#Auto-deleted code.
	lines = open(scriptPath).readlines()
	del lines[3]
	del lines[2]
	del lines[1]
	del lines[0]
	open(scriptPath,'w').writelines(lines)
	#Return the result.
	return r