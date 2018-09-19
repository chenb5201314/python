#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 21:04
# @Author  : chenb
# @Site    : 
# @File    : pvphero.py
# @Software: PyCharm

'''
作用：
    下载王者荣耀官网图片壁纸
'''

# 导入模块

import requests
import json
import urllib
with open(r'C:\\Users\\chenb\\Desktop\\herolist.json','r',encoding='utf-8') as ff:
    jsonzFile = json.load(ff)


for n in range(len(jsonzFile)):
    eName = jsonzFile[n]['ename']   # 英雄数据编号
    cName = jsonzFile[n]['cname']   # 中文名称
    skinName = jsonzFile[n]['skin_name'].split('|')    # 所有皮肤名称
    skinNumbers = len(skinName)
    print(skinNumbers)
    # print(jsonzFile[n]['ename'])
    # print(jsonzFile[n]['cname'])
    # print(jsonzFile[n]['skin_name'])
    #print(eName,cName,skinName)
    for m in range(1,skinNumbers+1):
        # 构造图片网址信息
        pictureUrl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(eName)+'/'+str(eName)+'-bigskin-'+str(m)+'.jpg'.format()
        # print(pictureUrl)
        # 下载图片
        # response = requests.get(pictureUrl)
        picture = requests.request('get',pictureUrl).content
        # content 代表是以二进制文件格式表示

        # 保存图片 图片都是二进制 第一种方式
        #with open('C:\\Users\\chenb\\Desktop\\heroPicture\\'+cName+skinName[m-1]+'.jpg','wb') as ff:
        #   ff.write(picture)
        # 保存图片 图片都是二进制 第二种方式
        urllib.request.urlretrieve(pictureUrl,'C:\\Users\\chenb\\Desktop\\heroPictures\\'+cName+skinName[m-1]+'.jpg')
