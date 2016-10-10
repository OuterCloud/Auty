# -*- coding: utf-8 -*-
import pymysql

def interact_mysql(sql,dbHost,userName,pwd,dbName):
	conn = pymysql.connect(host=dbHost, user=userName, passwd=pwd, port=3309, db=dbName, charset='utf8')
	cur = conn.cursor()
	cur.execute(sql)
	r = cur.fetchall()
	cur.close()
	conn.close()
	return r

def exec_sql(sql,dbHost,userName,pwd,dbName):
	if sql.startswith('select'):
		results = interact_mysql(sql,dbHost,userName,pwd,dbName)
		return results
	else:
		interact_mysql(sql,dbHost,userName,pwd,dbName)
