# -*- coding: utf-8 -*-
import sys
import os

def create_selection():
	path = sys.path[0]
	selection = []
	for i in os.walk(os.path.join(path,'scripts')):
		for fileName in i[2:3][0]:
			filePath = os.path.join(i[0],fileName)
			if(check_if_python(filePath)):
				selection.append(filePath)
	return selection

def check_if_python(fileName):
	if fileName.endswith('.py'):
		return True

def create_selection_file(selection):
	filePath = os.path.join(sys.path[0],'all_scripts_selection.txt')
	file = open(filePath,'w')
	for scriptPath in selection:
		file.write(scriptPath+'\n')
	file.close()

if __name__ == '__main__':
    selection = create_selection()
    create_selection_file(selection)
