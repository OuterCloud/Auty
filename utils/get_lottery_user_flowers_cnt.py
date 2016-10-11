# -*- coding: utf-8 -*-
from .execute_sql_mysql import exec_sql
from .sql_info import qz_host,qz_user,qz_pwd,qz_db_name

def get_lottery_user_flowers_cnt(userId):
	#Get userId from mysql db ts_user_info.
	sql = 'select * from ts_user_flower where user_id = \''+str(userId)+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	return r[0][3]