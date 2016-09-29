# -*- coding: utf-8 -*-
import requests
import time

def login_g(s,login_data):
    login_url = 'http://reg.163.com/login.jsp'
    r = s.post(login_url,data = login_data)
    r = s.get("http://g.caipiao.163.com/t/settingsFtl.html")
    print r.content
    if "当前登录账号：" in r.content:
        print u"登录g.caipiao.163.com成功！当前登录账户：%s" % login_data.get('username')
    else:
        print u"登录g.caipiao.163.com失败！"
    return s
