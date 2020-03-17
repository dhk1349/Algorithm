# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:57:53 2020

@author: dhk1349
"""


s=[3,2,5,7,1,9,4,6,8]
n=len(s)
#ascending sort
for i in range(0,n-1):
    for j in range(i+1,n):
        if(s[j]<s[i]):
            tmp=s[j]
            s[j]=s[i]
            s[i]=tmp
    
print(s)