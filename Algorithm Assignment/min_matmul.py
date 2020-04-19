# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:45:23 2020

@author: dhk13
"""

def minmul(d, ):
    M=[[None]*(len(d)-1) for i in range(len(d)-1)]
    #d-1 is number of matrix
    #iterates through matrix M
    for i in range(len(d)-1):
        M[i][i]=0
    # i means diff between row and column
    for i in range(1,len(d)-1):
        # (j,j+i) is starting matrix
        for j in range():
            for k in range(i, i+j+1):
                M[i][i+j]=
    
    return path, M

def order(p, i, j):
    