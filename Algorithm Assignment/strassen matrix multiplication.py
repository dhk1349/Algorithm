# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:21:39 2020

@author: dhk13
"""

#THis is normal version of matrix multiplication
def matmul(a, b):
    result=a.copy()
    #suppose inputs are n*n(square shape)
    for i in range(len(a)):
        for j in range(len(a)):
            tmp=0
            for k in range(len(a)):
                tmp+=a[i][k]*b[k][j]
            result[i][j]=tmp
    return result
    
a=[[1,2],[3,4]]
b=[[2,0],[0,2]]

print(matmul(a,b))

def strassen(a,b):
    n=len(a)
    th=2
    if(n<=th):
        matmul(a,b)
    else:
        
    
def strassen_rev(a,b):