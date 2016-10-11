# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert

def like_test(accountId,postId,like):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_like.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
		'postId':postId,
		'like':like
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def like_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"点赞成功!")
	tylan_assert(jsonResult['result'],100)

def unlike_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"点赞取消!")
	tylan_assert(jsonResult['result'],100)

if __name__ == '__main__':
    like_assert(like_test('runcheck5@163.com','1132664','1'))
    unlike_assert(like_test('runcheck5@163.com','1132664','0'))