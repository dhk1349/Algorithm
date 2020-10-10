# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:32:25 2020

@author: dhk13
"""

import random

tc1=[random.randint(0,1000) for _ in range(0,20)]


def BubbleSort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if(lst[j]>lst[j+1]):
                x=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=x
    return lst

print(BubbleSort(tc1))