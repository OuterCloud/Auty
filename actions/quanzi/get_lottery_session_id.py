# -*- coding: utf-8 -*-
from .execute_sql_mysql import exec_sql
from .sql_info import lott_mq_host,lott_mq_user,lott_mq_user_pwd,lott_mq_db_name

def get_lottery_session_id(account_id):
	r = exec_sql('select session_id from tb_lottery_mobile_session where account_id = \''+account_id+'\'',lott_mq_host,lott_mq_user,lott_mq_user_pwd,lott_mq_db_name)
	session_id = r[0][0]
	return session_id