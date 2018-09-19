#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 21:01
# @Author  : chenb
# @Site    : 
# @File    : neihan.py
# @Software: PyCharm

import requests
import time
url = 'https://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1520945114.0'
# https://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1520944918
response = requests.get(url)

print(response.status_code) # 返回状态码

# 提取时间戳
print(response.json()['data']['max_time'])

timestamp = response.json()['data']['max_time']
header = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Cookie':'uuid="w:893a7c07245f4a8e9e4cf6f7b50a4907"; __guid=101886750.2822254755138153500.1520944886424.5906; tt_webid=6532408589544801805; csrftoken=a8e0d8f61bb0341f20aaedc33d6eec76; monitor_count=2; _ga=GA1.2.1142451107.1520944887; _gid=GA1.2.565891062.1520944887',
'Host':'neihanshequ.com',
'Referer':'https://neihanshequ.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'X-CSRFToken':'a8e0d8f61bb0341f20aaedc33d6eec76',
'X-Requested-With':'XMLHttpRequest}'}

while type(timestamp)== float or type(timestamp)== int :
    time.sleep(3)
    url = 'https://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='+str(timestamp)

    response = requests.get(url,headers=header)

    with open(r'C:\Users\chenb\Desktop\test.txt', 'a', encoding='utf-8') as f:
        for m in range(len(response.json()['data']['data'])):
            data = response.json()['data']['data'][m]['group']['content']
            f.write(data + '\n')

    timestamp = response.json()['data']['max_time']
    print(timestamp)

# response.encoding = 'utf-8'

# print(response.text) # 没有编码的文本信息
# print(response.json()['data']['data'][0]['group']['content']) # 打印json文件；json 与dict

# 如何批量提取内涵段子

