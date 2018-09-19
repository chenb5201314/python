#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 21:58
# @Author  : chenb
# @Site    : 
# @File    : ciyun.py
# @Software: PyCharm

import requests
import re
import time
import random
import pandas as pd #数据操作
import numpy as np
import matplotlib.pyplot as plt # 绘图
import jieba
from wordcloud import WordClod # 词云可视化
import matplotlib as mpl # 配置字体
from pyecharts import Geo # 地理图
