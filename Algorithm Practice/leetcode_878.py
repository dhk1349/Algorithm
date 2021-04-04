# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:47:32 2021

@author: dhk1349
"""
from math import gcd, pow
def getlcm(x, y): return x * y // gcd(x,y)


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm=getlcm(a, b)
        numa=int(lcm/a-1)
        numb=int(lcm/b-1)
        #one cycle=numa+numb+1(lcm)
        order=[]
        idxs={a:0, b:0}
        for i in range(numa+numb+1):
            if (idxs[a]+1)*a>(idxs[b]+1)*b:
                order.append(b)
                idxs[b]+=1
            elif (idxs[a]+1)*a<(idxs[b]+1)*b:
                order.append(a)
                idxs[a]+=1
            else: #when equal
                order.append(a)
                idxs[a]+=1
                idxs[b]+=1
        numcycle=n//(numa+numb+1)
        remain=n%(numa+numb+1)
        
        iternum=0
        aorb=order[remain-1]
        for i in range(remain):
            if order[i]==aorb:
                iternum+=1
        if a==b:
            idxs[aorb]/=2
        return int((aorb*numcycle*idxs[aorb] + aorb*iternum)%(pow(10,9)+7))
