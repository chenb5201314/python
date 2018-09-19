#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 11:42
# @Author  : chenb
# @Site    : 
# @File    : anzhike.py
# @Software: PyCharm


# pip3 install requests
import requests
import json
import re

Url = 'https://mp.weixin.qq.com/mp/homepage?__biz=MzI1Mjg2NjkwOQ==&hid=1&sn=3ee240d35991f7ed6dbe13c8f9582652&scene=18'

result = requests.get(Url)
#print(result)
#print(result.text)

urladdr = re.findall('<a class="list_item js_post" href="(.*?)">',result.text)

name = re.findall('<h2 class="title js_title">(.*?)</h2>', result.text)

#print(name)

result2 = requests.get(urladdr[0])

print(result2.text)
