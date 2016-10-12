# -*- coding: utf-8 -*-
import sys
import os

def read_selection():
	path = os.path.abspath(os.path.dirname(__file__))
	parentPath = os.path.dirname(path)
	selectionFolderPath = os.path.join(parentPath,'scripts','selections')
	selectionFilePaths = []
	for filePath in os.walk(selectionFolderPath):
		for thePath in filePath[2]:
			selectionFilePaths.append(os.path.join(selectionFolderPath,thePath))
	selection = []
	for selectionFilePath in selectionFilePaths:
		for line in open(selectionFilePath):
			selection.append(line.replace('\n',''))
	return selection

#if __name__ == '__main__':
#	read_selection()
