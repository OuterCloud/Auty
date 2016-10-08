# -*- coding: utf-8 -*-
import sys
import os
import requests

def test():
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_sendPosts.html'
	login_data = {
		'userId':'10919',
		'category':'4',
		'text':'sdfsdfsdf',
		'postType':'1',
		'userToken':'64E5BFF48C6A53532EE16C51164EB5F6',
		'boardId':'12'
	}
	r = s.post(url, data = login_data)
	print r.content

#执行该文件的主过程
if __name__ == '__main__':
    test()