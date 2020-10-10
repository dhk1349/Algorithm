# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:59:52 2020

@author: dhk13
"""

import random

tc1=[random.randint(0,1000) for i in range(0,10)]


def SelectionSort(lst):
    for i in range(0, len(lst)-1):
        smallest=lst[i]
        idx=i
        for j in range(i+1, len(lst)):
            if smallest>lst[j]:
                smallest=lst[j]
                idx=j
        lst[idx]=lst[i]
        lst[i]=smallest
    return lst
print(SelectionSort(tc1))