# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include

def get_user_informs_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/getUserInforms.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"success")
	tylan_assert(jsonResult['result'],100)
	tylan_assert_include(jsonResult,'informList')

if __name__ == '__main__':
    basic_assert(get_user_informs_test('runcheck5@163.com'))