# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:35:12 2020

@author: dhk1349
"""

def bs(data, item, low, high):
    loc=-1
    while(loc==-1 and low<=high):
        mid=int((high+low)/2)
        if(item==data[mid]):
            loc=mid
        elif(item<data[mid]):
            high=mid-1
        else:
            low=mid+1
    return  loc

data=[1,3,5,6,7,9,10,14,17,19]
n=10
location=bs(data, 17, 0, n-1)
print(location)