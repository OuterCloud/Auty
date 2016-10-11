# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include

def get_notice_count_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getNoticeCount.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId)
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['resultDesc'],u'成功')
	tylan_assert_include(jsonResult,'newFollowerCount')
	tylan_assert_include(jsonResult,'msgCount')

if __name__ == '__main__':
	r = get_notice_count_test('runcheck5@163.com')
	basic_assert(r)