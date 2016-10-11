# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include

def get_user_header_test(accountId):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getUserHeader.html'
	data = {
		'vUserId':get_lottery_user_id(accountId),
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
	}
	r = s.post(url, data = data)
	#print r.content
	return r

def basic_assert(r):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"成功")
	tylan_assert(jsonResult['result'],100)
	tylan_assert_include(jsonResult,'nickName')
	tylan_assert_include(jsonResult,'avatarUrl')
	tylan_assert_include(jsonResult,'userId')
	tylan_assert_include(jsonResult,'ifHasInform')
	tylan_assert_include(jsonResult,'followState')
	tylan_assert_include(jsonResult,'postCnt')
	tylan_assert_include(jsonResult,'msgCnt')
	tylan_assert_include(jsonResult,'followedCnt')
	tylan_assert_include(jsonResult,'followerCnt')
	tylan_assert_include(jsonResult,'collectPostCnt')
	tylan_assert_include(jsonResult,'bigAvatarUrl')
	tylan_assert_include(jsonResult,'flowerCnt')
	tylan_assert_include(jsonResult,'ifHasNewFlower')

if __name__ == '__main__':
    basic_assert(get_user_header_test('runcheck5@163.com'))