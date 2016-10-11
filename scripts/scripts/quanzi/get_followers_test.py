# -*- coding: utf-8 -*-
import sys
import os
import requests
from utils.get_lottery_session_id import get_lottery_session_id
import json
from utils.get_lottery_user_id import get_lottery_user_id
from utils.utils import tylan_assert,tylan_assert_include
from utils.get_lottery_followers import get_lottery_followers,get_lottery_userid_follow

def get_followers_test(accountId,_type):
	s = requests.Session()
	url = 'http://quanzi.caipiao.163.com/circle_getFollowers.html'
	data = {
		'vUserId':get_lottery_user_id(accountId),
		'userId':get_lottery_user_id(accountId),
		'userToken':get_lottery_session_id(accountId),
		'lastFollowId':'',
		'type':_type
	}
	userId = get_lottery_user_id(accountId)
	r = s.post(url, data = data)
	#print r.content
	return r,userId

def basic_assert_followers_0(r,followers):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"成功")
	tylan_assert(jsonResult['result'],100)
	tylan_assert_include(jsonResult,'followers')
	#Assert the count of the ones user follow.
	if(tylan_assert(len(jsonResult['followers']),len(followers))=='passed' and len(followers)!=0):
		#Assert each of the followers.
		ids=[]
		for followerFromJson in jsonResult['followers']:
			ids.append(str(followerFromJson['id']))
		for follower in followers:
			tylan_assert_include(ids,str(follower[1]))

def basic_assert_followers_1(r,userid_follow):
	jsonResult = json.loads(r.content)
	tylan_assert(jsonResult['resultDesc'],u"成功")
	tylan_assert(jsonResult['result'],100)
	tylan_assert_include(jsonResult,'followers')
	#Assert the count of the ones follow user.
	if(tylan_assert(len(jsonResult['followers']),len(userid_follow))=='passed' and len(userid_follow)!=0):
		#Assert each of the followers.
		ids=[]
		for followerFromJson in jsonResult['followers']:
			ids.append(str(followerFromJson['id']))
		for follower in userid_follow:
			tylan_assert_include(ids,str(follower[1]))

if __name__ == '__main__':
	r,userId = get_followers_test('runcheck5@163.com','0')
	followers = get_lottery_followers(userId)
	basic_assert_followers_0(r,followers)

	r,userId = get_followers_test('runcheck5@163.com','1')
	userid_follow = get_lottery_userid_follow(userId)
	basic_assert_followers_1(r,userid_follow)