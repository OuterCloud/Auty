# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.execute_sql_mysql import exec_sql
from utils.sql_info import qz_host,qz_user,qz_pwd,qz_db_name
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.root_path import autyPath
import mimetypes
from requests_toolbelt import MultipartEncoder
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include

def upload_images_test(accountId,picPath):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_upLoadImages.html'
	data = {
		'userId':get_lottery_user_id(accountId),
		'head':'1',
		'userToken':get_lottery_session_id(accountId)
	}
	f = {'uploadfile':(open(picPath,'rb'),'application/octet-stream')}
	r = s.post(url, data = data, files = f)
	#print r.content
	assert_wrong(r)

def assert_wrong(r):
	jsonResult = json.loads(r.content)
	tylan_assert_include(jsonResult['resultDesc'],u'不支持该类型图片')
	tylan_assert(jsonResult['result'],500)

if __name__ == '__main__':
	accountId = 'runcheck5@163.com'
	picPath = os.path.join(autyPath,'data','testpic.jpg')
	#print picPath
	upload_images_test(accountId,picPath)