# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id

def login_test(accountId,caipiaoUserId,deviceId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_login.html'
	data = '?caipiaoUserId='+caipiaoUserId+'userToken='+get_lottery_session_id(accountId)+'deviceId='+deviceId
	r = s.get(url+data)
	print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	assert jsonResult['resultDesc'] == u"成功"
	assert jsonResult['result'] == 100
	assert jsonResult['userId'] == get_lottery_user_id(accountId)

if __name__ == '__main__':
	print 'No login interface.'
    #basic_assert(login_test('runcheck5@163.com',u'瑞安5','08:00:27:b8:32:f1'))