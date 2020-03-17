# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:42:54 2020

@author: dhk1349
"""
import time
def fib1(n):
    #recursive
    if(n<=1):
        return n
    else:
        return fib1(n-1)+fib1(n-2)
    
def fib2(n):
    #iterative
    result=[0]*(n+1)
    result[0]=0
    if(n>0):
        result[1]=1;
        for i in range(2,n+1):
            result[i]=result[i-1]+result[i-2]
            
    return result[n]

"""
for i in range(0,10):
    print('{} {} {}'.format(i, fib1(i), fib2(i)))
"""
print("Recursive fibonacci")
for i in range(30,36):
    stime=time.time()
    fib1(i)
    ftime=time.time()
    print("{}: {}".format(i, ftime-stime))
    
print("\nIterative fibonacci")
for i in range(30,36):
    stime=time.time()
    fib2(i)
    ftime=time.time()
    print("{}: {}".format(i, ftime-stime))