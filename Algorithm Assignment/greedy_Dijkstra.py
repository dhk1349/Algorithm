# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:48:15 2020

@author: dhk1349
"""
inf=1000
w=[[0,7,4,6,1],[inf,0,inf,inf,inf],
   [inf,2,0,5,inf], [inf,3,inf,0,inf], [inf,inf,inf,1,0]]
n=5
f=set()
touch=n*[0]
length=n*[0]
save_length=n*[0]

for i in range(1,n):
    length[i]=w[0][i]

for i in range(n-1):
    mindist=inf

    for j in range(1, n):
        if (length[j]<mindist and 0<=length[j]):
            mindist=length[j]
            vnear=j
    save_length[vnear]=length[vnear]
    edge=(touch[vnear], vnear)
    f.add(edge)
    for j in range(1, n):
        if(length[vnear]+w[vnear][j]<length[j]):
            length[j]=length[vnear]+w[vnear][j]
            touch[j]=vnear
    length[vnear]=-1



print(f)
print(save_length)