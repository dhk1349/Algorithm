# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:09:46 2020

@author: dhk1349
"""
import copy
def matrix_multiplication(dim,a,b):
    result=copy.deepcopy(a)
    
    for i in range(dim):
        for j in range(dim):
            result[i][j]=0
            for k in range(dim):
                result[i][j]+=(a[i][k]*b[k][j])
    return result

a=[[1,2],[3,4]]
b=[[1,0],[0,1]]

print(matrix_multiplication(2,a,b))