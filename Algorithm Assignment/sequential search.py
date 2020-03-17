# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 23:44:07 2020

@author: dhk1349
"""

def seqsearch(s, x):
    for i in range(len(s)):
        if x==s[i]:
            return i
    return -1
    
    
    return
s=[3,5,2,1,7,9]
loc=seqsearch(s,4)
print(loc)