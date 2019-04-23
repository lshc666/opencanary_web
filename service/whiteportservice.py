#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 白名单端口过滤
  Site: http://pirogue.org 
  Created: 2018-08-17 16:15:08
"""

from dbs.dal.Host import HostOp
# import sys
# sys.path.append("..")

White_res = HostOp()


def whiteports(dst_host):
    return White_res.get_whiteport(dst_host)

def updateports(port_agent,str_port):
    White_res.update_whiteport(port_agent,str_port)
    return True


# def deleteports():
#     White_res.delete_white_port()
#     return True