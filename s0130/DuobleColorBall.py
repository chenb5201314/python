#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 22:26
# @Author  : chenb
# @Site    : 
# @File    : DuobleColorBall.py
# @Software: PyCharm

import random

red_ball_list = []


'''
loopNums = 6
for i in range(loopNums):
    red_ball = random.randint(1, 33)
    if red_ball not in red_ball_list:
        red_ball_list.append(red_ball)
    else:
        print(red_ball)
        loopNums += 1

'''

while len(red_ball_list) < 6:
    red_ball = random.randint(1, 33)
    if red_ball not in red_ball_list:
        red_ball_list.append(red_ball)
    else:
        print(red_ball)


print(red_ball_list)


blue_ball = random.randint(1,16)

ball_all = ''

for i in sorted(red_ball_list):
    # ball_all = ball_all + ' '+str(i)
    ball_all += '%02d ' %i

ball_all += '+' + '%02d' %blue_ball

print(ball_all)
