# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:12:55 2020

@author: dhk1349

Possible errors:
    string as input (o)
    negative number as input (o)
    Non-integer as input  (o)
    when m is larger than n
    
"""
import random
import sys

print("==Type Two Integers!==",end="")
error=""
try:
    n=input("Type n:")
    m=input("Type m:")
    if (n<m):
        error+="N must be same or bigger than M.\n"
    if (n<0 or m<0):
        error+="Both M and N should not be negative number."
    if (type(n)!=int or type(m)!=int):
        error+="M or N should be interger format"
    if(error!=""):
        raise usererror
            
except ValueError:
    print("You must type numbers.")
    sys.exit()
except usererror:
    print(error)
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