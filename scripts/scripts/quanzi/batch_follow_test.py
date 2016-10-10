# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.sql_info import qz_host,qz_user,qz_pwd,qz_db_name
from utils.get_lottery_session_id import get_lottery_session_id
import json

def batch_follow_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/client_batchFollow.html'
	#Get userId from mysql db ts_user_info.
	sql = 'select userid from ts_user_info where email = \''+accountId+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	userId = r[0][0]
	data = {
		'userId':userId,
		'userToken':get_lottery_session_id(accountId),
		'followedUserIds':'10105,10104'
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def batch_follow_basic_assert(r):
	jsonResult = json.loads(r.content)
	assert jsonResult['result'] == 100
	assert jsonResult['resultDesc'] == u'成功'

if __name__ == '__main__':
	batch_follow_basic_assert(batch_follow_test('runcheck5@163.com'))