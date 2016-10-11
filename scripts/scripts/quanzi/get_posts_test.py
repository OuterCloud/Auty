# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert

def get_post_test(accountId,boardId,sort,apiLevel):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getPosts.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
		'sort':sort,
		'boardId':boardId,
		'apiLevel':apiLevel
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['board']['boardId'],'12')
	tylan_assert(jsonResult['board']['boardName'],u'测试圈子')
	tylan_assert(jsonResult['board']['circle'],'1')

if __name__ == '__main__':
	r = get_post_test('runcheck5@163.com','12','follow','27')
	basic_assert(r)