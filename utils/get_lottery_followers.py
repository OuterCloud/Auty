# -*- coding: utf-8 -*-
from .execute_sql_mysql import exec_sql
from .sql_info import qz_host,qz_user,qz_pwd,qz_db_name

def get_lottery_followers(userId):
	#Get ones the userid follow.
	sql = 'select * from ts_user_follow where userid = \''+str(userId)+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	return r

def get_lottery_userid_follow(userId):
	#Get ones follow the userid.
	sql = 'select * from ts_user_follow where userid_follow = \''+str(userId)+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	return r