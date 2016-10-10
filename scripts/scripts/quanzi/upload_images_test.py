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

def upload_images_test(accountId,picPath):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_upLoadImages.html'
	#Get userId from mysql db ts_user_info.
	sql = 'select userid from ts_user_info where email = \''+accountId+'\''
	r = exec_sql(sql,qz_host,qz_user,qz_pwd,qz_db_name)
	userId = r[0][0]
	#print userId
	#print get_lottery_session_id(accountId)
	data = {
		'userId':userId,
		'head':'1',
		'userToken':get_lottery_session_id(accountId)
	}
	f = {'uploadfile':(open(picPath,'rb'),'application/octet-stream')}
	r = s.post(url, data = data, files = f)
	#print r.content
	assert_wrong(r)

def assert_wrong(r):
	jsonResult = json.loads(r.content)
	assert u'不支持该类型图片' in jsonResult['resultDesc']
	assert jsonResult['result'] == 500

if __name__ == '__main__':
	accountId = 'runcheck5@163.com'
	picPath = os.path.join(autyPath,'data','testpic.jpg')
	#print picPath
	upload_images_test(accountId,picPath)