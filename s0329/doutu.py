#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 21:03
# @Author  : chenb
# @Site    : 
# @File    : doutu.py
# @Software: PyCharm

import requests
import re
import pymysql

db = pymysql.connect(host = ',mysql.litianqiang.com',port = 7150,
                     db = 'xinlan',user = 'xinlan,',passwd = 'A123456',charset = '')

cursor = db.cursor()
cursor.execute('select * from auth_user')

print(cursor.fetchall())


# 创建一个方法，获取斗图网图片

urlBase = 'https://www.doutula.com/photo/list/?page=2'
# 获取图片列表
def getImageList(page):
    html = requests.get('https://www.doutula.com/photo/list/?page={}'.format(page)).text
    # 正则表达式
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    reg = re.compile(reg,re.S)
    imageList = re.findall(reg,html)

    for i in imageList:
        # 新增一个
        cursor.execute("insert into image(`name`,`imageurl`) values('{}','{}')".format(i[1],i[0]))
        print('正在保存 %s' %i[1])
        db.commit()

for m in range(1,1001):
    print('第{}页'.format(m))
    getImageList(m)
