#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'stdu.tslhw'
# activation function: relu sigmoid tanh，少层神经网络可以随意，
# 卷积神经网络用relu，循环神经网络用relu or tanh
# 转到所在目录下 tensorboard --logdir='logs/'
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_fuction=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')  # 生成随机的行列矩阵
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_fuction is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_fuction(Wx_plus_b)
        return outputs


# define placeholder for inputs to network
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')  # None 输入sample，多少个都行，1表示1个维度
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')
# 隐藏层l1 用10个神经元
# add hidden layer
l1 = add_layer(xs, 1, 10, activation_fuction=tf.nn.relu)
# add output layer
prediction = add_layer(l1, 10, 1, activation_fuction=None)
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                        reduction_indices=[1]))
with tf.name_scope('train'):
    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)
init = tf.initialize_all_variables()
sess = tf.Session()
writer = tf.summary.FileWriter('logs/', sess.graph)
sess.run(init)
