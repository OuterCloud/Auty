# -*- coding: utf-8 -*-
import os
import time
import csv
from .generate_html import write_csv_to_html

def generate_result(resultFileName,result):
	filePath = os.path.abspath(os.path.dirname(__file__))
	resultFilePath = os.path.join(os.path.dirname(filePath),'results',resultFileName+'.csv')
	#print resultFilePath
	csvFile = file(resultFilePath,'a+')
	writer = csv.writer(csvFile)
	data = [result]
	writer.writerows(data)
	csvFile.close()
	html_result_path = os.path.join(os.path.dirname(filePath),'results',resultFileName+'.html')
	write_csv_to_html(resultFilePath,html_result_path)
