# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:54:49 2020

@author: dhk1349
"""

def bs(data, item, low, high):
    
    if(low>high):
        return -1
    else:
        mid=int((low+high)/2)
        if(item==data[mid]):
            return mid
        elif(item>data[mid]):
            return bs(data, item, mid, high)
        else:
            return bs(data, item, low, mid)
        
    
data=[1,3,5,6,7,9,10,14,17,19]
n=10
location=bs(data, 17, 0, n-1)
print(location)