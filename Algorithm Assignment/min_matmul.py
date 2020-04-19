# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:45:23 2020

@author: dhk13
"""

INF=99999

def minmul(d):
    M=[[None]*(len(d)) for i in range(len(d))]
    #d-1 is number of matrix
    #iterates through matrix M
    for i in range(len(d)):
        M[i][i]=0
    # i means diff between row and column
    for i in range(1, len(d)):
        # (j,j+i) is starting matrix
        #(j=row number)
        for j in range(1, len(d)-i):
            M[j][j+i]=INF
            for k in range(len(d),1,-1):
                M[j][j+i]=min(M[j][j+i], M[j][k]+M[k+1][j+i]+(d[j]-1)*(d[k])*(d[j+i]))
            print(j, ", ", j+i)   
    
    #return path, M

def order(p, i, j):
    return

d=[1,1,1,1,1,1,1]
minmul(d)