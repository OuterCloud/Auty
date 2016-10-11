# -*- coding: utf-8 -*-
from .execute_sql_mysql import exec_sql
from .sql_info import qz_host,qz_user,qz_pwd,qz_db_name

def get_messages(userId):
	#Get messages.
	sql = 'select * from ts_message where userid = \''+str(userId)+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	return r