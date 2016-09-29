# -*- coding: utf-8 -*-
import cx_Oracle

def interact_db(userInfo,dbStr,sql):
    connStr = userInfo + dbStr 
    conn = cx_Oracle.connect(connStr)	
    c = conn.cursor()                                       
    c.execute(sql)
    if sql.startswith('select'):
        fir=c.fetchall()
        conn.commit()             
        c.close()                                 
        conn.close()
        return fir
    else:
        conn.commit()             
        c.close()                                 
        conn.close()

def exec_sql(userInfo,dbStr,sql):
    if sql.startswith('select'):
        results = interact_db(userInfo,dbStr,sql)
        return results
    else:
        interact_db(userInfo,dbStr,sql)
