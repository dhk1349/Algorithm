# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:29:50 2020

@author: dhk13
"""
import time
import random
n=7
A=[3,1,6,2,4,9,5]


def alg1(n, A):
    stime=time.time()
    M=[None]*n
    M[0]=A[0]
    for i in range(1,n):
        maxnum=A[0]
        for j in range(1,i+1):
            if (maxnum<A[j]):   
                maxnum=A[j]
        M[i]=maxnum
    etime=time.time()
    print ("size: ",len(M))
    print("# of basic operation: ", int((n*n-n)/2))
    print("alg1 Operating time: ", etime-stime)
    return

def alg2(n,A):
    stime=time.time()
    M=[None]*n
    maxnum=A[0]
    M[0]=maxnum
    for i in range(1,n):
        maxnum=max(maxnum, A[i])
        M[i]=maxnum
    etime=time.time()
    print ("size: ",len(M))
    print("# of basic operation: ", n-1)
    print("alg2 Operating time: ", etime-stime,"\n")
    return


#alg1(n,A)
#alg2(n,A)


for i in range(2):
    if i==0:
        size=1000
    else:
        size=10000
    for j in range(5):
        box=[]
        for i in range(size*(j+1)):
            box.append(random.randrange(1,100))
        alg1(size*(j+1),box)
        alg2(size*(j+1),box)
