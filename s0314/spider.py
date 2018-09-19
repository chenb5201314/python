#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 22:01
# @Author  : chenb
# @Site    : 
# @File    : spider.py
# @Software: PyCharm

import requests

sURL = 'https://www.baidu.com/s?wd=python'


# 驼峰命名法
# 方法名：getBdMsg
# 获取百度搜索的结果
def getBdMsg(keyword):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    html = requests.get('https://www.baidu.com/s?wd={}'.format(keyword), headers= headers)
    # print(html.text)
    return html.text

if __name__ == '__main__':
    getBdMsg('python')
