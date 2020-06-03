# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:24:52 2020

@author: dhk13
"""

import queue

class Node:
        def __init__(self,level,weight, profit, bound, include):
                self.level = level
                self.weight = weight
                self.profit = profit
                self.bound = bound
                self.include = include
        def __cmp__(self, other):
               return cmp(self.bound, other.bound)


def kp_Best_FS():
        global maxProfit
        global bestset
        temp = n*[0]
        v = Node(-1,0,0, 0.0,temp)

     구현

def compBound(u):
        if u.weight >=W:
                return 0
        else:
                 구현




# heap이 minheap이라 bound를 계산하여 -를 하여 리턴한다. 비교를 < maxProfit으로 수행한다.
n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit =0
bestset=n*[0]
kp_Best_FS()
print(bestset)
print(maxProfit)


"""
[1, 0, 1, 0]
-90
"""