#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 20:55
# @Author  : chenb
# @Site    : 
# @File    : thread_state.py
# @Software: PyCharm

#导入所需的吗模块
import threading
import time

# 定义函数入口
# 通过继承的方式来创建一个线程

class A(threading.Thread):
        # 如果以继承的方式来创建线程的话，要重写父类的run方法
    def run(self):
        # 定义一个死循环
        while True:
            # 判断当前线程是否上锁
            if con.acquire():
                print('A thread is run')
                # 让当前线程阻塞
                con.wait()
                print('A thread 继续 run')
                # 当前线程会释放锁
                con.release()
                time.sleep(1)

class B(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                input('输入任意字符')
                # 通知其他线程做好准备，准备抢这把锁了
                con.notify()

                con.release()

                time.sleep(1)


# 创建条件变量
con = threading.Condition()

if __name__ =='__main__':
    a = A()
    a.start()

    b = B()
    b.start()
