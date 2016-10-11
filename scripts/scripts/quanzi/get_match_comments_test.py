# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
import json
from utils.utils import tylan_assert

def get_match_comments_test(postId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getMatchComments.html'
	data = {
		'postId':postId
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['resultDesc'],u'成功')
	tylan_assert(jsonResult['num'],0)

if __name__ == '__main__':
	#Need match post supported.
	r = get_match_comments_test('1132660')
	basic_assert(r)