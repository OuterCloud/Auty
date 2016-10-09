# -*- coding: utf-8 -*-
from lib.execute_selection import execute_selection
import os

if __name__ == '__main__':
	#Save the auty path into file.
	autyPath = os.path.dirname(__file__)
	pathFilePath = os.path.join(autyPath,'root_path')
	open(pathFilePath,'w').write(autyPath)
	#execute scripts.
	execute_selection(autyPath)