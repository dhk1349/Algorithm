# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:58:39 2020

@author: dhk13
"""

def promising(i,weight, total):
    return (weight+total>=W)and(weight==W or weight+w[i+1]<=W)

def s_s(i, weight, total, include):
    if (promising(i, weight, total)):
        if(weight==W):
            print("sol [", end="")
            for i in range(len(include)-1):
                print(include[i],", ", end="")
            print(include[-1],"]")
                
        else:
            #include
            include[i+1]=1
            s_s(i+1,weight+w[i+1],total-w[i+1], include)
            #not include
            include[i+1]=0
            s_s(i+1,weight,total-w[i+1], include)
    return


n=4
w=[1,4,2,6]

W=6
print("items =",w, "W =", W)
include = n*[0]
total=0
for k in w:
    total+=k
s_s(-1,0,total,include)
"""
n=100
w=[]
for i in range(1,101):
    w.append(i)
W=365
total=0
include=n*[0]
total=sum(w)

s_s(-1,0,total, include)
"""
