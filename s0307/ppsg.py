#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 22:47
# @Author  : chenb
# @Site    : 
# @File    : ppsg.py
# @Software: PyCharm

import requests
import json
import urllib
import re
# view-source:http://papasg.feiliu.com/web/list/imgc.shtml
ppsgUrl = 'http://papasg.3333.cn/wujiang/'
indexHtml = 'http://papasg.3333.cn'
#resp = requests.get(ppsgUrl)
#print(resp.text)

class PaPa():
    def __init__(self):
        self.url = ppsgUrl
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        print('类已经初始化好了')
    def getWuJiang(self):
        self.html = requests.get(self.url, headers=self.headers)
        # 筛选数据 bs4 re
        # print(self.html.text)
        # 爬去html链接
        html = re.findall('<div class="wjtj_right_bottom_c_top"><a href="(.*?)" target=', self.html.text)

        # 遍历所有html文件
        for m in range(len(html)-1):
            #print('#:'+str(m) + html[m])
            subhtml = requests.get(html[m])
            #print(subhtml.text)
            jpgName = re.findall('<p.*src="(.*?).jpg".*</p>',subhtml.text)
            jpgFileName = re.findall('<p.*src="/.*/.*/.*/.*/(.*?).jpg".*</p>', subhtml.text)
            print(jpgName)
            if len(jpgName) != 0:
                pictureUrl = indexHtml +jpgName[0]+'.jpg'
                print(pictureUrl)
                urllib.request.urlretrieve(pictureUrl,'C:\\Users\\chenb\\Desktop\\ppsgwujiang\\' + jpgFileName[0]+'.jpg')
        #picName = re.findall('<img src="/d/file/wujiang/.*/(.*?)"/></a></div>', self.html.text)  # /d/file/wujiang/.*/
        #jpgpic = re.findall('<img src="(.*?)"/></a></div>', self.html.text)  # /d/file/wujiang/.*/
        # href = re.findall('<a href="(.*?)" target=',data)

        # print(html)

        #for m in range(len(html)):
        # subhtml = requests.get(html[0])
        #
        # print(html)
        #(jpgpic)
        #print(picName)
        #for n in range(len(jpgpic)):



if __name__ == '__main__':

    ppsg = PaPa()

    ppsg.getWuJiang()