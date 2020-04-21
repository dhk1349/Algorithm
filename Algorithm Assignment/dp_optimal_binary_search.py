# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:29:49 2020

@author: dhk1349
"""

class Node:
    def __init__(self, data):
        self.l_child=None
        self.r_child=None
        self.data=data
    
def tree(key, r, i, j):     
    k=r[i][j]
        
    if (k==0):
        return 
    else:
        p=Node(key[k])
        p.l_child=tree(key, r, i, k-1)
        p.r_child=tree(key, r,k+1, j)
        return p
    
   
    
def printMatrix(d):
    m=len(d)
    n=len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" %d[i][j], end=" ")
    
def printMatrixF(d):
    m=len(d)
    n=len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%4f" %d[i][j], end=" ")

#presetting the variables
key=[' ', 'A', 'B', 'C', 'D']
p=[0, 0.375, 0.375, 0.125, 0.125]
n=len(p)-1
a=[[0 for j in range(0, n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0, n+2)] for i in range(0,n+2)]

for i in range(1, n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
    
a[n+1][n]=0
r[n+1][n]=0

for diagonal in range(2, len(p)):
    for column in range(len(p)-diagonal):
        for k in range(diagonal, column+1):
            a[diagonal][column]=min(a[diagonal][column],a[diagonal][k-1]+a[k][column]+)