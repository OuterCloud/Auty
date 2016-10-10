# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id

def report_test(userId,apiLevel,reportReson):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_report.html'
	data = '?userId='+userId+'apiLevel='+apiLevel+'reportReson='+reportReson
	r = s.get(url)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	assert jsonResult['resultDesc'] == u"举报已提交"
	assert jsonResult['result'] == 100

if __name__ == '__main__':
    basic_assert(report_test('10104','27',u'测试举报接口'))