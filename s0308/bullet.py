#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 0:51
# @Author  : chenb
# @Site    : 
# @File    : bullet.py
# @Software: PyCharm

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # 一个对飞船发射的子弹飞行的进行管理的类
    def __init__(self,ai_setting,screen ,ship):
        # 在飞船所处位置创建一个子弹对象
        super(Bullet,self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top   = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

