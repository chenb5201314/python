#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 20:56
# @Author  : cc
# @Site    : 
# @File    : qkl.py
# @Software: PyCharm

import hashlib as hasher
import datetime as date
#首先定义我们的区块链将会是个什么样子，有哪些功能，比如每个块链的索引位置，时间戳，每个块链中的数据，以及上一个块链的哈希值

class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        #用sha256进行加密
        sha = hasher.sha256()
        sha.update((str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)).encode("utf-8"))
        #返回给我们一个16进制的加密结果
        return sha.hexdigest()


#创建一个起源块
def create_genesis_block():
    #手动构造块链，索引为0或者任意先前块链的散列
    return Block(0,date.datetime.now(),'Genesis Block','0')


#起源块后续的块链都会以何种方式陆续创建，怎么去创建
def next_block(last_block):
        this_index = last_block.index+1
        this_timestamp = date.datetime.now()
        this_data = 'hey 我是区块链'+str(this_index)
        this_previous_hash = last_block.hash
        return Block(this_index,this_timestamp,this_data,this_previous_hash)

#创建块链并添加起源块
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

#在起源块之后，我们应该在后续加多少个块链

num_of_block_to_add = 20

#添加块到链上
for i in range(0,num_of_block_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print('add block #',block_to_add.index)
    print(block_to_add.previous_hash)

#blockchain.append(next_block(blockchain[i]))
