#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 23:09
# @Author  : chenb
# @Site    : 
# @File    : game_function.py
# @Software: PyCharm

import pygame
import sys
import setting
from bullet import Bullet

def check_keydown_events(event,ai_setting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_setting.bullet_allowed:
            new_bullet = Bullet(ai_setting, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event,ai_setting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_setting.bullet_allowed:
            new_bullet = Bullet(ai_setting,screen,ship)
            bullets.add(new_bullet)

def check_event(ai_setting,screen,ship,bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_setting,screen,ship,bullets)


def update_screen(ai_setting,screen,ship,bullets):
    # 更新屏幕上的图像，并切换到新屏幕
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))