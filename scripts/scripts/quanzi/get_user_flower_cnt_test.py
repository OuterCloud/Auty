# -*- coding: utf-8 -*-
import sys
import os
import requests
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include
from utils.get_lottery_user_flowers_cnt import get_lottery_user_flowers_cnt

def get_user_flower_cnt_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getUserFlowerCnt.html'
	userId = get_lottery_user_id(accountId)
	data = {
		'userId':userId,
	}
	r = s.post(url, data = data)
	flowerCnt = get_lottery_user_flowers_cnt(userId)
	#print flowerCnt
	#print r.content
	return r,flowerCnt

def basic_assert(r,flowerCnt):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"成功！")
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['usableFlowerCnt'],str(flowerCnt))

if __name__ == '__main__':
	r,flowerCnt = get_user_flower_cnt_test('runcheck5@163.com')
	basic_assert(r,flowerCnt)