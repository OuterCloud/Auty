# -*- coding: utf-8 -*-
from .execute_sql_mysql import exec_sql
from .sql_info import qz_host,qz_user,qz_pwd,qz_db_name

def get_lottery_post_info(postId):
	#Get post info from ts_group_topic.
	sql = 'select * from ts_group_topic where topicid=\''+postId+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	return r[0]