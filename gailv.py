#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 22:37
# @Author  : chenb
# @Site    : 
# @File    : gailv.py
# @Software: PyCharm

import random

"""
rand_number = random.randint(0,9)

print(rand_number)

for i in range(3): #生成器，返回值得同时可以暂停
    user_number = int(input('请输入你猜的数字：'))

    if rand_number == user_number:
        print('猜对了')
        break
    else:
        print('猜错了')

"""
user_number_list = []

rand_number = random.randint(0, 9)

for i in range(9):  # 生成器，返回值得同时可以暂停
    user_number = int(input('请输入你猜的数字：'))
    user_number_list.append(user_number)
    print('猜错了')

print(user_number_list)

# rand_number = random.randint(0,9)
# if rand_number not in user_number_list:
#    print('正确答案是%s' %rand_number)
while rand_number in user_number_list:
    rand_number = random.randint(0, 9)
    print(rand_number)

print('正确答案是%s' % rand_number)
