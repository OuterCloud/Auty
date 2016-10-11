# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include
from utils.get_messages import get_messages

def get_messages_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getMessages.html'
	userId = get_lottery_user_id(accountId)
	data = {
		'userId':userId,
		'userToken':get_lottery_session_id(accountId)
	}
	r = s.post(url, data = data)
	#print r.content
	#print userId
	return r,userId

def basic_assert(r,userId):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['resultDesc'],u'成功')
	tylan_assert(len(jsonResult['messages']),len(get_messages(str(userId))))

if __name__ == '__main__':
	r,userId = get_messages_test('runcheck5@163.com')
	basic_assert(r,userId)