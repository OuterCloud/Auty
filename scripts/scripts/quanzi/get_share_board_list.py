# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include

def get_followers_test(accountId,_type):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getShareBoardList.html'
	r = s.post(url)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"获取小组列表成功")
	tylan_assert(jsonResult['result'],100)
	tylan_assert_include(jsonResult,'boards')

if __name__ == '__main__':
    basic_assert(get_followers_test('runcheck5@163.com','0'))