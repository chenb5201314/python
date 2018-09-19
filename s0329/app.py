#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 22:16
# @Author  : chenb
# @Site    : 
# @File    : app.py
# @Software: PyCharm

from flask import Flask
from flask import render_template
import requests as request
import pymysql


app = Flask(__name__)


# 装饰器

@app.route('/')
def index():
    #return 'hello world'
    return render_template('index.html')

'''
@app.route('/search')
def search():
    keyword = request.args.get('kw')
    count = requset.args.get('count')
    cursor.execute("select * from images where name like")

'''

if __name__ == '__main__':
    '''
    conn =  pymysql.connect(host = ',mysql.litianqiang.com', port = 7150,
                            db = 'xinlan', user = 'xinlan,',
                            passwd = 'A123456', charset = 'utf8', cursorclass='pymysql.cursors.DictCursor')
    '''
    app.run()
