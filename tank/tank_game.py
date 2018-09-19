#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 14:58
# @Author  : chenb
# @Site    : 
# @File    : tank_game.py
# @Software: PyCharm

"""
游戏汇总一共要设计哪些对象：
类：
    1、游戏主界面
    2、坦克
    3、炮弹
    4、隔离墙
    5、爆炸效果
这些类都是pygame中sprite的子类
"""
import pygame

from pygame.locals import *
import sys

class TankMain(object):
    """坦克大战的主窗口"""
    def __init__(self):
        pass
    # 开始游戏的方法
    def startGame(self):
        pygame.init()
        # 创建一个窗口，窗口的大小，窗口特性，
        screen = pygame.display.set_mode((600,480),0,32)
        # 设置窗口标题
        pygame.display.set_caption("坦克大战")
        myTank = Tank(screen,275,400)
        while True:
            # 设置背景颜色
            screen.fill((0,0,0))
            screen.blit(self.show_text(),(20,30))

            myTank.tankShow()
            # 刷新
            pygame.display.update()

    # 关闭游戏
    def stopGame(self):
        sys.exit()

    # 设置游戏窗口的标题
    def setTitle(self):
        pass

    def show_text(self):
        font = pygame.font.SysFont("fangsong",12)

        # text_sf = pygame.font.Font.render(font,"敌方坦克的数量为：5",True,(255,0,0))
        text_sf = font.render("敌方坦克的数量为：5", True, (255, 0, 0))
        return text_sf
    # 获取所有的事件
    def get_envnt(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()  # 程序退出
            if event.type == KEYUP:
                pass
            if event.type == KEYDOWN:
                pass
            if event.type == K_LEFT:
                pass
            if event.type == K_RIGHT:
                pass
            if event.type == K_SPACE:
                pass
            if event.type == K_ESCAPE:
                self.stopGame()


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Tank(BaseItem):
    # 定义类属性，所有坦克对象的高和宽都是一样
    width = 50
    height = 50

    def __init__(self,screen,left,top):
        super().__init__()
        self.screen = screen # 坦克在移动或者显示过程需要用到的游戏的屏幕
        self.direction = "D" # 坦克的方向，默认方向往下
        self.images = {} # 坦克的所有图片
        self.images["L"] = pygame.image.load("images/tankL.gif")
        self.images["R"] = pygame.image.load("images/tankR.gif")
        self.images["D"] = pygame.image.load("images/tankD.gif")
        self.images["U"] = pygame.image.load("images/tankU.gif")
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True  # 决定坦克是否消灭了
    def tankMove(self):
        pass
    # 把坦克显示到窗口上
    def tankShow(self):
        self.image = self.images[self.direction]
        self.screen.blit(self.image,self.rect)

if __name__ == '__main__':
    game = TankMain()
    game.startGame()