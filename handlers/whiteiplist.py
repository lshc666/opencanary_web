#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 获取白名单ip
  Site: http://pirogue.org 
  Created: 2018-08-27 15:35:43
"""


import tornado
from base import BaseHandler
from util.auth import jwtauth
from service.whiteipservice import whiteips,add_white_ip,delete_white_ip,Update_white_ip
# from dbs.dal.LogOperate import LogOp
import datetime
import json


@jwtauth
class WhiteiplistHandler(BaseHandler):
    """ 获取白名单ip列表 """

    def get(self):
        res = whiteips(1)
        # json.dumps(line_res)
        self.write(json.dumps(res))

    def write_error(self,status_code,**kwargs):
        self.write("Unable to parse JSON.")


    """ 添加白名单ip """
    def post(self):
        # 接收提交过来的port
        if self.request.headers["Content-Type"].startswith("application/json"):
            json_args = json.loads(self.request.body.decode('utf-8'))
            # 删除白名单IP
            if "delete_id" in json_args:
                delete_id = json_args["delete_id"]
                delete_white_ip(delete_id)
                self.write("OK")
            elif json_args["id"] == None: #添加白名单IP
                white_ip = json_args["ip"]
                white_ip_describe = json_args["describe"]
                if white_ip:
                    add_white_ip(white_ip, white_ip_describe)
                self.write("OK")
            else: #更新白名单IP
                white_ip_id = json_args["id"]
                update_white_ip = json_args["ip"]
                update_white_ip_describe = json_args["describe"]
                if white_ip_id:
                    Update_white_ip(white_ip_id,update_white_ip,update_white_ip_describe)
                self.write("OK")
        else:
            self.json_args = None
            message = 'Unable to parse JSON.'
            self.send_error(status_code=400) # 向浏览器发送错误状态码，会调用write_error
