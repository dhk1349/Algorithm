# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:03:41 2020

@author: dhk13
"""

def quickSort(s, low, high):
    #구현
    pivotpoint=0
    if(high>low):
        pivotpoint=partition(s, low, high)
        quickSort(s, low, pivotpoint-1)
        quickSort(s, pivotpoint+1, high) 
    
def partition(s,low, high):
    #구현
    pivotitem=s[low]
    j=low
    for i in range(low+1, high+1):
        if(pivotitem>s[i]):
            j+=1
            #exchange
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
    #j는 pivotpoint이다.
    temp=s[low]
    s[low]=s[j]
    s[j]=temp
    #pivotpoint인 j를 리
    return j 
    
s=[3, 5, 2, 9, 10, 14, 4, 8]
quickSort(s, 0, 7)
print(s)