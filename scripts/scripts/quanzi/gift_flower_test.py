# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include
from utils.get_lottery_user_flowers_cnt import get_lottery_user_recv_flower_cnt

def gift_flower_test(accountId,gift_userid,giftFlowerCnt):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_giftFlower.html'
	data = {
		'vUserId':get_lottery_user_id(accountId),
		'userId':gift_userid,
		'userToken':get_lottery_session_id(accountId),
		'giftFlowerCnt':giftFlowerCnt,
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"赠送成功")
	tylan_assert(jsonResult['result'],100)

if __name__ == '__main__':
	gift_userid = '10055'
	giftFlowerCnt = '1'
	accountId = 'runcheck5@163.com'
	flowersBefore = get_lottery_user_recv_flower_cnt(gift_userid)
	#print flowersBefore
	r = gift_flower_test(accountId,gift_userid,giftFlowerCnt)
	flowersThen = get_lottery_user_recv_flower_cnt(gift_userid)
	#print flowersThen
	basic_assert(r)