#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 20:59
# @Author  : chenb
# @Site    : 
# @File    : signed.py
# @Software: PyCharm

'''
本节课核心
1、了解web开发流程
2、了解web原理
3、签到系统的业务逻辑
4、从整体上了解python

签到系统，本质是一个网站
搭建一个web服务器

环境： python3
模块： web框架  tornado
ide:   集成开发环境 pycharm
'''
from  tornado import web ,ioloop,httpserver
from  createCode import get_code_by_str
import time

# 文件句柄
# 全局变量
SIGN_FILE_HANDLER = open('sign.csv','a')

SIGN_FILE_HANDLER.write('%s,%s,%s,%s\n' %('姓名','工号','部门','签到时间'))

# 逻辑处理模块
class MainPageHandler(web.RequestHandler):
    def get(self,*arg,**kwargs):
        self.render('index.html')


class SignHandler(web.RequestHandler):
    def get(self,*arg,**kwargs):
        # self.write('未来的大神们！！')
        self.render('sign.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        department = self.get_argument('department')
        num = self.get_argument('num')
        curr_time = time.ctime()

        SIGN_FILE_HANDLER.write('%s,%s,%s,%s\n' % (name,num,department,curr_time))
        SIGN_FILE_HANDLER.flush()

        self.write('签到成功')

        # 收到数据了
        # 处理 安全，检测，过滤

# 生产二维码
class CodeHandler(web.RequestHandler):
    def get(self,*args,** kwargs):
        # 生成一个二维码图片
        code_img_handler = get_code_by_str('http://www.baidu.com/')
        self.write(code_img_handler.getvalue())

# 路由
application = web.Application([
    (r"/login",MainPageHandler),
    (r'/sign',SignHandler),
    (r'/code',CodeHandler)
    ])

# socket服务
if __name__ == '__main__':
    httpserver = httpserver.HTTPServer(application)
    httpserver.listen(8080)
    ioloop.IOLoop.current().start()