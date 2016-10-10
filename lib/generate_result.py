# -*- coding: utf-8 -*-
import os
import time
import csv

def generate_result(resultFileName,result):
	filePath = os.path.abspath(os.path.dirname(__file__))
	resultFilePath = os.path.join(os.path.dirname(filePath),'results',resultFileName)
	#print resultFilePath
	csvFile = file(resultFilePath,'a+')
	writer = csv.writer(csvFile)
	data = [result]
	writer.writerows(data)
	csvFile.close()