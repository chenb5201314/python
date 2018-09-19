#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 20:53
# @Author  : chenb
# @Site    : 
# @File    : newspider.py
# @Software: PyCharm


import requests,xlwt,matplotlib
import re
import json
import time
#import draw
DATA = []

url = 'https://s.taobao.com/search?q=python&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'

# 下载数据
response = requests.get(url)

html = response.text
# print(response.text)
# 处理数据
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html,re.S)[0].strip() #
# 格式化
content = content[:-1]

print(content)
# 清洗 回车换行
content = json.loads(content)

print(content)

data_list = content['mods']['itemlist']['data']['auctions']

# 筛选出所需要的数据

for item in data_list:
    temp = {
        'title':item['title'],
        'view_price':item['view_price'],
        'view_sales':item['view_sales'],
        'view_fee':'否' if float(item['view_fee']),

    }
    print(item['title'])


url2 = 'https://s.taobao.com/api?_ksTS=1519997205487_238&callback=jsonp239&ajax=true&m=customized&sourceId=tb.index&q=python&spm=a21bo.2017.201856-taobao-item.1&s=36&imgfile=&initiative_id=tbindexz_20170306&bcoffset=0&commend=all&ie=utf8&rn=ae788b8ed5816e6b282485e8024053eb&ssid=s5-e&search_type=item' \

response2 = requests.get(url2)
html2 = response2.text

data_list  = json.loads(re.findall(r'{.*}'))
# 翻页
for i in range(1,10):
    data_value = 44*i
    t = time.time()
    ksTs = "%s_%s" %(int(t*1000),str(t)[-3:])
    callback = "jsonp%s" %(int(str(t)[-3:])+1)
    url = 'https://gm.mmstat.com/search?cache=502d9f8&gmkey=&gokey=vers%3Dj%26list_model%3Dgrid%26searchurl%3D1%26cat%3D%26direct_cat%3D33%26at_lflog%3D4-1-0-0-2-23653-0-all%7C%26at_bucketid%3D1%26multi_bucket%3D7_1_2_0_0_0_0_0%26at_colo%3Dst3%26at_host%3Dhippo.11.178.237.61.st3%26alitrackid%3Dwww.taobao.com%26at_alitrackid%3Dwww.taobao.com%26last_alitrackid%3Dwww.taobao.com%26stats_show%3Drs%253Apv%253Buser_group%253AClusterMergeInfo%253Aexcellent%253A0.8%253Blunbo%253A0.2%253Bmd_QueryIntentionType%253A%253Bbandit%253AGongYingLianDists%25253ACN%252BHZ%252BMIDDLE%252BQDHEWL-0036%252BSTORE_1228938%252BSXHZ%252B0%253Bzf_sort%253A87%253Bhas_p4p%253A1%253Btopcatpredict_flag%253A1%253Bhas_sku_pic%253A0%253Btab_type%253Aall%253Bsn_hide%253A0%253Bs%253Amainsearch%253Beval%253A1%253Bqinfo%253A1%252C10%252C20%252C30%252C40%252C50%252C60%252C65%252C70%252C100%252C110%252C120%252C130%252C140%252C177%252C203%252C220%252C230%252C240%252C600%252C1245%252C9109%252C100000033%252C150512007%252C1000000000%253Bapass%253A0%253B%26rn%3D04935e69d074c5875f98d7705e4f9800%26nick%3D%26multivariate%3Dmain_alg%253A263' \
      '%253Bzhutisoufe%253A6181%253Bpc_topic_sort%253A6019%253Bmain_fe_extend%253A4539%253Bpfourp_test%253A256%253Bpfourp_mbox%253A4762%253Bpc_to_wireless_suggest_fix%253A10769%253Bmain_fe%253A299%253Bpricefixbts%253A8921%253Btoufang_taobao%253A5195%26srppage%3D2%26s_query%3Dpython&cna=R%2F1PEsk6i1QCAd3oulyHn1Vq&spm-cnt=a230r.1.0.0.1' \
      'ba21dd8AZ8NJw&logtype=2 '.format(data_value,ksTs,callback)

    print(url)


# 持久化
f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet('sheet1',)
#写标题

# 写内容
f.save(u'搜索python的结果.xls')