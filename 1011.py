# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:20:07 2021

@author: dhk13
"""
import math
def solve(x, y):
    half=math.floor((y-x)/2)
    other_half=math.ceil((y-x)/2)
    cnt=0
    
    #print("half: ", half)
    
    s=math.floor(math.sqrt(half*2))-1 #y-x==5  half==2
    #print("s: ",s)
    #first half
    while(half!=0):
        if half>=s*(s+1)/2 and half<(s+1)*(s+2)/2:
            other_half+=(half-s*(s+1)/2)
            cnt+=s
            break
        else:
            s+=1
    
    
    #print("other half: ", other_half)
    #print("s: ", s)
    #print("cnt: ", cnt)
    #other half
    s+=1
    while(other_half!=0):
        if(other_half>=s*(s+1)/2 and other_half<(s+1)*(s+2)/2):
            #print("case1: ",s, s*(s+1)/2, (s+1)*(s+2)/2)
            other_half-=(s*(s+1)/2)
            cnt+=s
            
            #print("cnt: ", cnt)
            break
        elif(other_half<=(s)*(s+1)/2): #원래는 s+1, s+2였
            s-=1
        elif(other_half>(s)*(s-1)/2):
            s+=1
    
    #print("remaining: ", other_half)
    
    if other_half!=0:
        cnt+=1
    return cnt

tc=int(input())

for _ in range(tc):
    x, y = (map(int, input().split()))
    print(solve(x,y))