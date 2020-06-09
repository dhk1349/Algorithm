# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:24:52 2020

@author: dhk13
"""

import queue
import copy

def cmp(a, b):
    return (a > b) - (a < b) 

class Node:
    def __init__(self,level,weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include
    def __lt__(self, other):
        return self.bound<other.bound
    def __cmp__(self, other):
        return cmp(self.bound, other.bound)


def bound(u):
    bound=-u.profit
    j=u.level+1
    totweight=u.weight
    while(j<len(w) and totweight+w[j]<W):
        totweight=totweight+w[j]
        bound=bound+p[j]        
        j+=1
    if(j<len(w)):
        #w 공간이 꽉 차진 않은 경우 
        bound=bound+(W-totweight)*(p[j]/w[j])
    return -bound

def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n*[0]
    v = Node(-1,0,0, 0.0,temp)
    u = Node(-1,0,0, 0.0,temp)
    maxProfit=-v.profit
    v.bound=bound(u)
    PQ=queue.PriorityQueue()
    PQ.put(v)
    while(not PQ.empty()):
        v=PQ.get()
        if(v.bound<maxProfit and v.level<2):
            u.level=v.level+1
            u.weight=v.weight+w[u.level]
            u.profit=v.profit-p[u.level]
            u.include=v.include
            u.include[u.level]=1
            
            if(u.weight <= W and u.profit < maxProfit):
                maxProfit=u.profit
                bestset=copy.deepcopy(u.include)
                
            u.bound=bound(u)
            if(u.bound<maxProfit and u.weight<=W):
                PQ.put(copy.deepcopy(u))
                
            u.weight = v.weight
            u.profit = v.profit
            u.bound = bound(u)
            u.include[u.level]=0
            if(u.bound<maxProfit and u.weight<=W):
                PQ.put(copy.deepcopy(u))


def compBound(u):
    if u.weight >=W:
        return 0
    else:
        #bound와 totweight을 구해서 maxp와 비교해야한다. 
        bound=u.profit
        j=u.level+1
        totweight=u.weight
        while(j<len(w) and totweight+w[j]<W):
            totweight=totweight+w[j]
            bound=bound+p[j]        
            j+=1
        if(j<len(w)):
            #w 공간이 꽉 차진 않은 경우 
            bound=bound+(W-totweight)*(p[j]/w[j])
        return bound>maxProfit     




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
