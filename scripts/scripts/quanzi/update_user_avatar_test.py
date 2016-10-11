# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include

def update_user_avatar_test(accountId,avatarUrl):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/updateUserAvatar.html'
	userId = get_lottery_user_id(accountId)
	data = {
		'userId':userId,
		'userToken':get_lottery_session_id(accountId),
		'avatarUrl':avatarUrl
	}
	r = s.post(url, data = data)
	#print r.content
	#print userId
	return r,userId

def basic_assert(r,avatarUrl):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['result'],100)
	tylan_assert(jsonResult['resultDesc'],u'成功')
	tylan_assert(jsonResult['avatarUrl'],avatarUrl)

if __name__ == '__main__':
	avatarUrl = 'http://img2.imgtn.bdimg.com/it/u=1160161467,1922703035&fm=21&gp=0.jpg'
	r,userId = update_user_avatar_test('runcheck5@163.com',avatarUrl)
	basic_assert(r,avatarUrl)