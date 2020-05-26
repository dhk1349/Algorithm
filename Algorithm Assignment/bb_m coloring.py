# -*- coding: utf-8 -*-
"""
Created on Wed May 27 01:06:13 2020

@author: dhk1349
"""

def color(i,vcolor):
    if(promising(i, vcolor)):
        if(n==i+1):
            print("[", end="")
            for j in range(len(vcolor)-1):
                print(vcolor[j],", ", end="")
            print(vcolor[-1],"]")
        else:
            for j in range(1,m+1):
                vcolor[i+1]=j
                color(i+1, vcolor)



def promising(I,vcolor):
    j=0
    switch=True
    while(j<I and switch):
        if(W[I][j] and vcolor[I]==vcolor[j]):
            switch=False
        j+=1
    return switch

n=4
W=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
vcolor=n*[0]
m=3
color(-1,vcolor)
