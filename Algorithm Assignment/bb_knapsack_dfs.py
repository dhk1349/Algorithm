# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:21:01 2020

@author: dhk13
"""

def kp(i, profit, weight):
        global bestset
        global maxp
        
        #최댓 값 갱신 
        if( weight <= W and profit >maxp):
            maxp = profit
            bestset = include[:]
            # best = include는 best를 include의 reference로 만든다.
            # 한 번 동일한 값을 가진 후 그 이후는 계속 동일함.
        if(promising(i, weight, profit)):
            include[i+1]=1
            kp(i+1, profit+p[i+1], weight+w[i+1])
            
            include[i+1]=0
            kp(i+1, profit, weight)
   
def promising(i,weight,profit):
    global maxp
    if(weight>=W):
        #꽉 차서 못 넣는 경
        return False
    else:
        #bound와 totweight을 구해서 maxp와 비교해야한다. 
        bound=profit
        j=i+1
        totweight=weight
        while(j<len(w) and totweight+w[j]<W):
            totweight=totweight+w[j]
            bound=bound+p[j]        
            j+=1
        if(j<len(w)):
            #w 공간이 꽉 차진 않은 경우 
            bound=bound+(W-totweight)*(p[j]/w[j])
        return bound>maxp
n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
maxp=0
include =[0,0,0,0]
bestset = [0,0,0,0]
kp(-1,0,0)
print(maxp)
print(bestset)
