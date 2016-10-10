# -*- coding: utf-8 -*-
from .execute_sql_mysql import exec_sql
from .sql_info import qz_host,qz_user,qz_pwd,qz_db_name

def get_lottery_user_id(accountId):
	#Get userId from mysql db ts_user_info.
	sql = 'select userid from ts_user_info where email = \''+accountId+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	userId = r[0][0]
	return userId