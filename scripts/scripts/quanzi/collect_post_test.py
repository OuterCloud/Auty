# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert

def collect_post_test(accountId,postId,collection):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/client_collectPost.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
		'postId':postId,
		'collection':collection
	}
	r = s.post(url, data = data)
	print r.content
	return r

def collect_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"成功")
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['collectStatus'],'1')

def  uncollect_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"成功")
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['collectStatus'],'0')

if __name__ == '__main__':
    collect_assert(collect_post_test('runcheck5@163.com','1132664','1'))
    uncollect_assert(collect_post_test('runcheck5@163.com','1132664','0'))