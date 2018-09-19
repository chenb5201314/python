#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 21:10
# @Author  : chenb
# @Site    : 
# @File    : Mythread.py
# @Software: PyCharm

import time
import threading
"""
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            msg = '线程'+self.name #+str(i)
            print(msg)
if __name__ == '__main__':
    t = MyThread()
    t.start()
"""

num = 0

class MyThread(threading.Thread):
    def run(self):
        # 告诉Python解析器，我要对全局变量进行修改了
        global num
        num = num +1
        time.sleep(1)
        msg = self.name + 'set num to '+ str(num)
        print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()