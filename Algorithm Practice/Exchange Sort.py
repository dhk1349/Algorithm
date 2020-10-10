# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:10:49 2020

@author: dhk13
"""

import random

tc1=[random.randint(0,100) for _ in range(50)]

def ExchangeSort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if (lst[i]>lst[j]):
                x=lst[i]
                lst[i]=lst[j]
                lst[j]=x
    return lst

print(ExchangeSort(tc1))