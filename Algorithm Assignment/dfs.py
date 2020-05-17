# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:17:43 2020

@author: dhk13
"""

def PrintMatrix(a):
    for i in range (len(a)):
        for j in range(len(a[i])):
            print("%4d" %a[i][j], end="")
        print()

e={0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6],4:[6,7]}
n=8
a = [ [0 for j in range(0,n)] for i in range(0,n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        if i in e:
           if j in e[i]:
              a[i][j]=1
              a[j][i]=1
PrintMatrix(a)

visited =n*[0]

def DFS(a,v):
    #v가 현재 노드 
    if (visited[v]==1):
        return 
    visited[v]=1
    print (v)
    for i in range(len(a[v])):
        if (a[v][i]==1):
            DFS(a, i)

            
DFS(a,0)
