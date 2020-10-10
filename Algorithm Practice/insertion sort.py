# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:25:11 2020

@author: dhk13
"""

import random

tc=[10,1,4,2,11,5,7]

tc1=[random.randrange(0,1000) for _ in range(50)]

#print(tc1)



def InsertionSort(lst):
    for i in range(1, len(lst)):
        x=lst[i]
        for j in range(i-1, -1, -1):
            if(x<lst[j]):
                lst[j+1]=lst[j]
                lst[j]=x
            
            else:
                #lst[j+1]=x
                break
            
        #print(lst)
    return lst
        
    
print(InsertionSort(tc1))
