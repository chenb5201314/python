#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 21:12
# @Author  : chenb
# @Site    : 
# @File    : alien_invasion.py
# @Software: PyCharm

import  pygame
import game_function as gf
from setting import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    screen = pygame.display.set_mode((1280,800))

    pygame.display.set_caption('Alien_Invasion')

    # 设置背景颜色
    #bg_color = (230,230,230)
    #加载背景
    ai_setting = Settings()
    ship = Ship(ai_setting,screen)
    bullets = Group()
    # 开始游戏的主循环

    while True:
        gf.check_event(ai_setting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting,screen,ship,bullets)


run_game()