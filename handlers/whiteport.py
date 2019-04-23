#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 获取白名单port
  Site: http://pirogue.org 
  Created: 2018-08-27 15:35:43
"""


import tornado
from base import BaseHandler
from util.auth import jwtauth
from service.whiteportservice import updateports
# from dbs.dal.LogOperate import LogOp
import datetime
import json


@jwtauth
class WhiteportHandler(BaseHandler):
    """ 获取白名单port列表 """

    def get(self):
        # res = ''
        res = ','.join('%s' % p for p in whiteports())
        # json.dumps(line_res)
        self.write(res)

    
    def write_error(self,status_code,**kwargs):
        self.write("Unable to parse JSON.")

    def post(self):
        # 接收提交过来的port
        if self.request.headers["Content-Type"].startswith("application/json"):
            json_args = json.loads(self.request.body.decode('utf-8'))
            port_str = json_args["port"]
            port_agent = json_args["address"]
            updateports(port_agent,port_str)
            self.write(json_args)
        else:
            self.json_args = None
            message = 'Unable to parse JSON.'
            self.send_error(status_code=400) # 向浏览器发送错误状态码，会调用write_error