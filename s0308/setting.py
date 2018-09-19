#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 0:24
# @Author  : chenb
# @Site    : 
# @File    : setting.py
# @Software: PyCharm

class Settings():
    def __init__(self):
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.

        # bullet attribute
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10

