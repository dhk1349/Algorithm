# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:52:44 2020

@author: dhk1349
"""

def sum1(s):
    result=0
    for i in s:
        result+=i
    return result

def sum2(s):
    result=0
    for i in range(len(s)):
        result+=s[i]
    return result

s=[3,5,2,1,7,9]
answer=sum1(s)
print(answer)
answer=sum2(s)
print(answer)