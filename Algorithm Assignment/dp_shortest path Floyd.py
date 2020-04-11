# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:31:26 2020

@author: dhk13
"""

inf=1000
g=[[0,1,inf, 1,5],
   [9,0,3,2,inf],
   [inf,inf,0,4,inf],
   [inf,inf,2,0,3],
   [3,inf,inf,inf,0]]

def printMatrix(d):
    m = len(d)
    n=len(d[0])
    
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")

        print()
        
def _path(p,q,r):
    #경로 출력함수     
    if(p[q][r]!=0 and p[q][r]-1!=r and p[q][r]-1!=q):
        _path(p,q,p[q][r]-1)
        print("v%d"% p[q][r], end=" ")
        _path(p,p[q][r]-1, r)
        
    return
 
def path(p,q,r):
    print("v%d"% q, end=" ")
    _path(p, q-1, r-1)
    print("v%d"% r, end=" ")


def floyd1(weight, n):
    D=weight.copy()
    for k in range(n):
        for i in range(len(weight)):
            for j in range(len(weight)):
                D[i][j]=min(D[i][j], D[i][k]+D[k][j])
    
    printMatrix(D)

def floyd2(weight, n):
    D=weight.copy()
    P=[[0]*n for i in range(n)]
    for k in range(n):
        for i in range(len(weight)):
            for j in range(len(weight)):
                if(D[i][j]> D[i][k]+D[k][j]):
                    D[i][j]=D[i][k]+D[k][j]
                    P[i][j]=k+1
    return D,P
    
#floyd1(g,5)

d,p=floyd2(g,5)
print()
printMatrix(d)
print()
printMatrix(p)
print()
path(p,5,3)

