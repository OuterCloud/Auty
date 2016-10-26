# -*- coding: utf-8 -*-
import csv,os

def write_csv_to_html(csv_path,save_path):
	print os.getcwd()
	csvfile = file(csv_path, 'rb')
	reader = csv.reader(csvfile)
	html = open(save_path, 'w')
	html.write("""
	<html>
	<head>
  	<title>Auty test result</title>
  	<h1>Auty test result</h1>
  	<h3>Result file path:"""+csv_path+"""</h3>
  	<style>img{float:left;margin:5px;}</style>
	</head>
	<body">
	<table border="1">
	""")
	for line in reader:
		if(('failed' in line) or ('No exception' not in line)):
			html.write('<tr bgcolor="#8B2323">')
		else:
			html.write('<tr bgcolor="#00FF7F">')
		for each in line:
			html.write('<td>'+each+'</td>')
		html.write('</tr>')
	html.write("""
	</table>
	</body>
	""")

if __name__ == '__main__':
	#write_csv_to_html('D:\\Auty\\results\\2016-10-25 15_20_17 test_result.csv')
	pass