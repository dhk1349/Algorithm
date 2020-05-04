# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:00:09 2020

@author: dhk13

Finding minimum spannig tree though prim algorithm.
"""

def printMatrix(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print("%7d"%x[i][j], end="")
        print()

inf = 1000
w=[[0,  1,  3,inf, inf],
   [1,  0,  3,6,   inf],
   [3,  3,  0,4,   2],
   [inf,6,  4,0,   5],
   [inf,inf,2,5,   0]]

F=set()
n=len(w)
nearest=n*[0]
distance=n*[0]

#v1을 시작점으로 초기
for i in range(1,n):
    nearest[i]=0
    distance[i]=w[0][i]

def prim(n, W, F):
    for i in range(1,n):
        mindist=inf
        for j in range(1, n):
            if(0<=distance[j] and distance[j]<mindist):
                mindist=distance[j]
                vnear=j
        edge=(vnear, nearest[vnear])
        F.add(edge)

        distance[vnear]=-1
        for j in range(1,n):
            if(W[j][vnear]<distance[j]):
                distance[j]=W[j][vnear]
                nearest[j]=vnear
printMatrix(w)
prim(n,w, F) 
print(F)
        
    