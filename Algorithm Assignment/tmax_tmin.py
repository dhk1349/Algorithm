# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:12:55 2020

@author: dhk1349

Possible errors:
    string as input (o)
    negative number as input (o)
    Non-integer as input  (o)
    when m is larger than n (o)
    n must be 3 or bigger than 3 (o)
    
"""
import random
import sys

print("==Type Two Integers!==",end="")
error=""
try:
    n=int(input("Type n:"))
    m=int(input("Type m:"))
    """
    if (type(n)!=int or type(m)!=int):
        error+="M or N should be integer format"
        raise Exception(error)
    """
    if (n<m):
        error+="Error: N must be same or bigger than M.\n"
    if (n<0 or m<0):
        error+="Error: Both M and N should not be negative number.\n"
    if(n<3):
        error+="Error: N must be 3 or bigger than 3.\n"
    if(error!=""):
        raise Exception(error)
            
except ValueError:
    print("Error: You must type numbers.")
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()
    
container=[None]*n
for i in range(n):
    container[i]=random.randint(1,10)

tmax=-1
tmin=sum(container)

for i in range(n-m+1):
    tmp=0
    for j in range(m):
        tmp+=container[i+j]
    if(tmp>tmax):
        tmax=tmp
    if(tmp<tmin):
        tmin=tmp

print(container)
print("tmax: ", tmax)
print("tmin: ", tmin)