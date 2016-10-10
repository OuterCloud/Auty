# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.sql_info import qz_host,qz_user,qz_pwd,qz_db_name
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert

def follow_test(accountId,followAction):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/client_follow.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
		'followedUserId':'10105',
		'followAction':followAction
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def follow_basic_assert(r):
	jsonResult = json.loads(r.content)
	assert jsonResult['result'] == 100
	assert jsonResult['resultDesc'] == u'成功'
	assert jsonResult['followState'] == '1'

def unfollow_basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['resultDesc'],u'成功')
	tylan_assert(jsonResult['followState'],'0')

if __name__ == '__main__':
	follow_basic_assert(follow_test('runcheck5@163.com','0'))
	unfollow_basic_assert(follow_test('runcheck5@163.com','1'))