#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 20:59
# @Author  : chenb
# @Site    : 
# @File    : MyShejian.py
# @Software: PyCharm

"""
Title = 获取豆瓣舌尖上的中国短评
"""
# 导入模块

import  requests

import re  # 自带的模块，不需要安装
cookie = { 'cookie':'aa'} # cookie值
for m in range(0,100,20):

    # 网址 统一资源定位符

    url = 'https://movie.douban.com/subject/25875034/comments?start={page}&limit=20&sort=new_score&status=P&percent_type='.format(page=m)

    # 打开目录 并获取里面的内容

    html = requests.get(url)

    # print(html)  # 返回200 状态码

    # print(html.text)

    # 筛选数据 bs4 re

    data = re.findall('<p class="">(.*?)\n        </p>', html.text)

    print(data)


    with open(r'C:\Users\chenb\Desktop\shejian.txt','a',encoding='utf-8') as f:
        for n in range(len(data)):
            f.write(data[n] +'\n')