# -*- coding: utf-8 -*-
import os
import time

def recovery_code(autyPath):
	for scriptPath in open(os.path.join(autyPath,'scripts','all_scripts_selection.txt')):
		scriptPath = scriptPath.strip('\n')
		lines = open(scriptPath).readlines()
		try:
			if ('utf' in lines[0]) and ('os' in lines[1]) and ('sys' in lines[2]) and ('sys.path.append' in lines[3]):
				print('Recovry:'+scriptPath)
				del lines[3]
				del lines[2]
				del lines[1]
				del lines[0]
				open(scriptPath,'w').writelines(lines)
		except Exception, e:
			raise
		else:
			pass
		finally:
			pass