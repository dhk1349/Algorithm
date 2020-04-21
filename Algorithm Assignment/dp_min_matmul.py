# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:45:23 2020

@author: dhk13
"""
from functools import reduce #required in python3
import operator
from copy import deepcopy

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print('%5s'%m[i][j],end="")
        print()



def minmul(d,M,P):
    INF=prod(d)
    # i means diff between row and column
    for i in range(1, len(d)):
        # (j,j+i) is starting matrix
        #(j=row number)
        for j in range(1, len(d)-i):
            M[j][j+i]=INF
            for k in range(j, j+i):
                if(M[j][j+i]> M[j][k]+M[k+1][j+i]+(d[j-1])*(d[k])*(d[j+i])):
                    M[j][j+i]=M[j][k]+M[k+1][j+i]+(d[j-1])*(d[k])*(d[j+i])
                    P[j][j+i]=k
    
    return M,P

def order(p, i, j):
    if(i==j):
        print("A",i, sep="", end="")
    else:
        k=p[i][j]
        print("(", sep="", end="")
        order(p, i, k)
        order(p,k+1, j)
        print(")", sep="",end="")
    return

d=[5, 2, 3, 4, 6, 7, 8]
n=len(d)-1
m=[[0 for j in range(1, n+2)] for i in range(1,n+2)] 
p=[[0 for j in range(1, n+2)] for i in range(1,n+2)] 
m,p=minmul(d, m,p)
printMatrix(m)
print()
printMatrix(p)

order(p, 1, 6)