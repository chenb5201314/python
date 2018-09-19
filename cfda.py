#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 21:01
# @Author  : chenb
# @Site    : 
# @File    : cfda.py
# @Software: PyCharm

"""
Title = cfda数据采集
date = 2018-03-04
"""
# 导入模块
import requests


class Cfda:
    # 初始化函数/方法，实例化的时候先执行
    def __init__(self):
        # print('hello')
        self.url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    # 普通的方法
    def getCfda(self,data):
        assert isinstance(data, object)
        self.html = requests.post(self.url,data=data)

        # print(self.html)  # 状态码 200
        # 第一种方法 批量提取信息
        for m in  range(15):
            self.data = self.html.json()['list'][m]['EPS_NAME']
            # print(self.data) # json 是一种文件格式
            self.data2File(self.data)
        # 第二种方法 函数式的提取信息
        # self.data = list(map(lambda n:self.html.json()['list'][n]['EPS_NAME'],range(15)))
        # print(self.data)

    def data2File(self,dat):
        with open(r'C:\Users\chenb\Desktop\cfda.txt','a') as ff:
            ff.write(dat+'\n')

# 如果在该文件下运行，程序会执行if判断语句下面的内容
# 如果该文件被其他文件导入，在其他文件下运行，if判断后的语句不会被调用
if __name__ == '__main__':
    # 实例化
    cfda = Cfda() # 隐式
    for n in range(1,5):
        # 实参
        data = {'applynnam':'',
                'applysn':'',
                'conditionType':'1',
                'on':'true',
                'page':n,
                'pageSiz':15,
                'productName':''}

        cfda.getCfda(data)  # 显式

