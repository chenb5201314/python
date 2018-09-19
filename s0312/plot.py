#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 20:54
# @Author  : chenb
# @Site    : 
# @File    : plot.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

# 指定图表的字体
plt.rcParams['font.sans-serif'] = ['fangsong']

#创建数据集，返回数据，group和labels
def creatDataSet():
    # 创建数组
    group = np.array([[1,101],[5,90],[108,5],[115,9]])
    #标签
    lables = ['爱情片','爱情片','动作片','动作片']
    #返回变量
    return group,lables

    # dataTest [1,100] [50,400]
def KNN(dataTest,dataSet,labels,k):
    #计算欧式距离
    # 计算行数
    dataSetSize = dataSet.shape[0]
    #创建块矩阵
    diffMat = np.tile(dataTest,(dataSetSize,1))-dataSet

    # 平方 每个元素平方
    sqDiffMat = diffMat**2
    #按行相加
    sqDistance = sqDiffMat.sum(1)

    # 根号，开方
    distance = sqDistance**0.5

    # 排序
    sortedDistance = distance.argsort()
    print(sortedDistance)
    # 字典
    classCounts = {}
    for m in range(k):
        # 前K个的类别
        votaLabel = labels[sortedDistance[m]]
        # 计数  get方法，查找字典对象，若有返回键值，若没有返回0，
        classCounts[votaLabel] = classCounts.get(votaLabel,0)+1
        # 对classCounts 字典排序

        sortedclassCount = sorted(classCounts.items(),key=lambda X:X[1],reverse=True)

    # print(classCounts)
    # print(sortedDistance)
    return sortedclassCount[0][0]

if __name__ == '__main__':

    group,labels = creatDataSet()
    # k 值可能改变结果
    print(KNN([100,5],group,labels,2))

    # 3429275949



