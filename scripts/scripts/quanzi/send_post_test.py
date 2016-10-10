# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert

def send_post_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_sendPosts.html'
	#sql = 'select column_name from information_schema.columns where table_name = \'ts_user_info\''
	data = {
		'userId':get_lottery_user_id(accountId),
		'category':'4',
		'text':'Tylan python send_post_test',
		'postType':'1',
		'userToken':get_lottery_session_id(accountId),
		'boardId':'12'
	}
	r = s.post(url, data = data)
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"发帖成功!")
	tylan_assert(jsonResult['result'],100)

if __name__ == '__main__':
    basic_assert(send_post_test('runcheck5@163.com'))