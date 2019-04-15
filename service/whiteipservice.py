#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 白名单过滤
  Site: http://pirogue.org 
  Created: 2018-08-17 16:15:08
"""

from dbs.dal.Whiteip import White
# import sys
# sys.path.append("..")

White_res = White()


def whiteips(model):
    list_ip = []
    if model == 1:
        res_name_tuple = ('id','ip','describe')
        for ip in White_res.white_ip():
            list_ip.append(dict(zip(res_name_tuple,ip)))
        return list_ip
    elif model==2:
        for ip in White_res.white_ip():
            list_ip.append(ip[1])
        return list_ip


def add_white_ip(w_ip,w_des):
    if w_ip:
        White_res.insert_white_ip(w_ip,w_des)

def delete_white_ip(del_id):
    if del_id:
        White_res.delete_white_ip(del_id)

def Update_white_ip(up_id,up_ip,up_des):
    if up_id:
        White_res.update_white_ip(up_id,up_ip,up_des)
