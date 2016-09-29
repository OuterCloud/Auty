# -*- coding: utf-8 -*-
import sys
import os

def read_selection():
	path = os.path.abspath(os.path.dirname(__file__))
	parentPath = os.path.dirname(path)
	selectionFilePath = os.path.join(parentPath,'scripts','selection.txt')
	selection = []
	for line in open(selectionFilePath):
		selection.append(line.replace('\n',''))
	return selection