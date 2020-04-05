# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:53:41 2020

@author: dhk13
"""
import math

def prod2(a,b):
    #구현
    n=max(len(str(a)),len(str(b)))
    th=4
    if(a==0 or b==0):
        return 0
    elif (n<th):
        return a*b
    else:
        m=math.floor(n/2)
        x=a//pow(10,m)
        y=a%pow(10,m)
        w=b//pow(10,m)
        z=b%pow(10,m)
        r=prod2(x+y, w+z)
        p=prod2(x,w)
        q=prod2(y,z)
        return p*pow(10,2*m)+(r-p-q)*pow(10,m)+q
    
    
a=1234567812345678
b=2345678923456789

print(prod2(a,b))
print(a*b)