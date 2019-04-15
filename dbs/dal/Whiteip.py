#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 白名单表操作
  Site: http://pirogue.org 
  Created: 2018-08-03 17:32:54
"""


from dbs.initdb import DBSession
from dbs.models.Whiteip import Whiteip
from sqlalchemy import desc,asc
from sqlalchemy.exc import InvalidRequestError

# import sys
# sys.path.append("..")

class White:
    """增删改查"""

    def __init__(self):  
        self.session=DBSession

    # 查询白名单表ip数据
    def white_ip(self):
        try:
            white_ip_res = self.session.query(Whiteip.id,Whiteip.src_host,Whiteip.description).order_by(Whiteip.id.desc()).all()
            return white_ip_res
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print (e)
        finally:
            self.session.close()
    
    # 增加白名单
    def insert_white_ip(self, src_host,src_host_des):
        try:
            wip_insert = Whiteip(src_host=src_host,description=src_host_des)
            self.session.add(wip_insert)
            self.session.commit()
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print (e)
        finally:
            self.session.close()


    # 删除白名单
    def delete_white_ip(self, del_id):
        try:
            white_del = self.session.query(Whiteip).filter(Whiteip.id == del_id).first()
            self.session.delete(white_del)
            self.session.commit()
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print (e)
        finally:
            self.session.close()


    # 更新白名单
    def update_white_ip(self, up_id,up_ip,up_des):
        try:
            white_update = self.session.query(Whiteip).filter(Whiteip.id == up_id).first()
            white_update.src_host = up_ip
            white_update.description = up_des
            self.session.commit()
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print (e)
        finally:
            self.session.close()