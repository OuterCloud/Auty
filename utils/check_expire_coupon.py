# -*- coding: utf-8 -*-
from execute_sql import exec_sql
from datetime import *
import time
from sql_info import dbStr,duobaoUser,couponUser,lotteryUser,historyUser

def check_expire_coupon(coupon_id_or_name):
    coupon_id_or_name = unicode(coupon_id_or_name, "utf-8")
    #查询红包是否过期
    coupSql = 'select * from tb_duobao_coupon_scheme where coupon_scheme_id = \''+coupon_id_or_name+'\' or coupon_name = \''+coupon_id_or_name+'\''
    r = exec_sql(couponUser,dbStr,coupSql)
    expire_time = r[0][29]
    #print expire_time
    #print datetime.today()
    if expire_time<datetime.today():
        tip = '红包已过期，红包id或name：'+str(coupon_id_or_name)
    else:
        tip = '红包未过期，红包id或name：'+str(coupon_id_or_name)
    print tip
    return tip
        
if __name__ == '__main__':
  check_expire_coupon('2016050521CS00658580')
