#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 21:40
# @Author  : chenb
# @Site    : 
# @File    : MyThread1.py
# @Software: PyCharm

import time
import threading
num  = 0

# 创建一把锁
mutex = threading.Lock()

class MyThread(threading.Thread):
    def run(self):
        global num
        # 上锁
        mutexFlag = mutex.acquire() # 上锁
        print('线程（%s）的锁状态为%d'%(self.name,mutexFlag))
        # 判断是否上锁成功
        if mutexFlag:
            num = num +1
            time.sleep(1)
            msg = self.name +'set num to'+str(num)
            print(msg)
            mutex.release() # 解锁

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()

"""


"""