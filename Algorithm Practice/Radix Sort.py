# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:40:09 2020

@author: dhk13
"""

import random
from collections import defaultdict

print("can sort numbers up to 3digit number")

tc1=[random.randint(0,1000) for _ in range(20)]

#print(tc1)


container=defaultdict(list)
def RadixSort(lst, container, num):
    
    #print(lst)
    
    for i in lst:
        container[(i//(10)**num)%10].append(i)
    #print(container)
    
    
    if num-1>=0:
        for i in container.keys():    
            subcontainer=defaultdict(list)
            container[i]=RadixSort(container[i], subcontainer, num-1)
    
    return container


result=RadixSort(tc1, container, 2)

for i in sorted(result.keys()):
    for j in sorted(result[i].keys()):
        for k in sorted(result[i][j].keys()):
            print(result[i][j][k][0], end=" ")