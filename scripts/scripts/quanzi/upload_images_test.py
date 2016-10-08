# -*- coding: utf-8 -*-
import sys
import os
import requests

def test():
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_upLoadImages.html'
	login_data = {
		'userId':'10919',
		'head':'1',
		'userToken':'64E5BFF48C6A53532EE16C51164EB5F6',
		'uploadfile':'200-200_1475915905347.jpg'
	}
	r = s.post(url, data = login_data)
	print r.content

#执行该文件的主过程
if __name__ == '__main__':
    test()