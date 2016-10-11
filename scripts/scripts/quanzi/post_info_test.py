# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert
from utils.get_lottery_post_info import get_lottery_post_info

def post_info_test(accountId,postId,apiLevel):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_postInfo.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
		'postId':postId,
		'apiLevel':apiLevel
	}
	postInfo = get_lottery_post_info(postId)
	r = s.post(url, data = data)
	#print r
	#print postInfo
	return r,postInfo

def basic_assert(r,postInfo):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"获取帖子信息成功")
	tylan_assert(jsonResult['result'],100)
	tylan_assert(str(postInfo[2]),jsonResult['post']['boardId'])
	tylan_assert(str(postInfo[3]),jsonResult['post']['userId'])
	tylan_assert(str(postInfo[4]),jsonResult['post']['text'])

if __name__ == '__main__':
	r,postInfo = post_info_test('runcheck5@163.com','1132635','27')
	basic_assert(r,postInfo)