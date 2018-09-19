#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 20:54
# @Author  : chenb
# @Site    : 
# @File    : zhihu.py
# @Software: PyCharm

#知乎粉丝抓取
#导入模块
import requests

#创建一个类
class ZhiHu:

    #初始化函数，实例化类的时候会运行init
    def __init__(self):
        self.url = 'https://pic2.zhimg.com/e5af96ed7cbab70cdced83afeb21aa54_b.jpg'
        self.headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        print('hello python')
    #创建一个方法
    def get_FenSi(self,param):

        self.html =  requests.get(self.url,params=param,headers=self.headers)

        for n in range(20):
            hash =self.html.json()[n]['hash']
            self.data2file(hash)
    def data2file(self,datas):
        with open(r'C:\Users\chenb\Desktop\hash.txt','a') as f:
            f.write(datas+'\n'*2)
        #print(self.html)

        #print(self.html.json())

        #print('hello python3')

if __name__ == '__main__': #判断条件

    zhihu = ZhiHu()  # 隐式调用

    #实现翻页
    for m in range(0,60,20):
        data = {'limit':20,
                'offset':m}
        zhihu.get_FenSi(data) #显式调用

