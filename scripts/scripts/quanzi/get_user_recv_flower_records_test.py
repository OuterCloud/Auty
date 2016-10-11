# -*- coding: utf-8 -*-
import sys
import os
import requests
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include

def get_user_recv_flower_records_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getUserRecvFlowerRecords.html'
	data = {
		'userId':get_lottery_user_id(accountId),
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"成功")
	tylan_assert(jsonResult['result'],100)

if __name__ == '__main__':
    basic_assert(get_user_recv_flower_records_test('runcheck5@163.com'))