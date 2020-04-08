# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:52:46 2020

@author: dhk13
"""

def bin(n,k):
    #n, k represents nCk
    #Dvide and conquer using the concept of Pascal's triangle.
    if(k==0 or n==k):
        return 1
    else:
        return bin(n-1, k-1)+bin(n-1, k)
    

def bin2(n,k):
    #Tihs function adopted dynamic programming.
    #Uses the concept of Pascals's triangle.
    result=[[None]*(k+1) for i in range(n+1)]
    for i in range(n+1):
        for j  in range(min(k,i)+1):
            if(j==0 or j==i):
                result[i][j]=1
            else:
                result[i][j]=result[i-1][j-1]+result[i-1][j]
                
    return result[i][j]

print(bin(10,5), bin2(10,5))