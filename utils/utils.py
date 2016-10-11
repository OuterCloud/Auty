# -*- coding: utf-8 -*-
import time
import datetime
import os

def str_2_tuple(*str):
	return str

def get_local_time():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def get_specific_time():
	return datetime.datetime.now()

def tylan_assert(actual,expected):
	if actual != expected:
		result = 'failed'
		print result
	else:
		result = 'passed'
		print result
	return result

def tylan_assert_include(actual,expected):
	if expected not in actual:
		result = 'failed'
		print result
	else:
		result = 'passed'
		print result
	return result