# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id

def post_info_test(accountId,postId,apiLevel):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_postInfo.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
		'postId':postId,
		'apiLevel':apiLevel
	}
	r = s.post(url, data = data)
	#print r.content
	basic_assert(r)

def basic_assert(r):
	jsonResult = json.loads(r.content)
	assert jsonResult['resultDesc'] == u"获取帖子信息成功"
	assert jsonResult['result'] == 100

if __name__ == '__main__':
    post_info_test('runcheck5@163.com','1132635','27')