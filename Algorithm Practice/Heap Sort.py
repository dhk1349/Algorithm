# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:16:04 2020

@author: dhk13
"""

import random
from copy import deepcopy
tc1=[random.randint(0,1000) for _ in range(20)]


def siftup(lst, idx):
    cursor=idx
    
    while (True):
        #print(cursor)
        if(cursor==1): # most upper node
            break
        elif(cursor%2==0):
            parent=int(cursor/2)
            if(lst[parent]>lst[cursor]):
                x=lst[cursor]
                lst[cursor]=lst[parent]
                lst[parent]=x
                cursor=parent
            else:
                break
        elif(cursor%2==1):
            parent=int((cursor-1)/2)
            if(lst[parent]>lst[cursor]):
                x=lst[cursor]
                lst[cursor]=lst[parent]
                lst[parent]=x
                cursor=parent
            else:
                break
        
    return lst

def siftdown(lst):
    cursor=1
    while(True):

        if(cursor*2>len(lst)-1):
            break
        elif(cursor*2+1<=len(lst)-1):

            if(lst[cursor]>lst[cursor*2] and lst[cursor*2]<lst[cursor*2+1]):
                x=lst[cursor]
                lst[cursor]=lst[cursor*2]
                lst[cursor*2]=x
                cursor=cursor*2
            elif(lst[cursor]>lst[cursor*2+1] and lst[cursor*2]>=lst[cursor*2+1]):
                x=lst[cursor]
                lst[cursor]=lst[cursor*2+1]
                lst[cursor*2+1]=x
                cursor=cursor*2+1
            else: 
                break
        elif(cursor*2<=len(lst)-1):
            if(lst[cursor]>lst[cursor*2]):
                x=lst[cursor]
                lst[cursor]=lst[cursor*2]
                lst[cursor*2]=x
                cursor=cursor*2
            
            else: 
                break
            
            
    
    return lst

def MakeHeap(lst):
    lst.insert(0, "NONE")
    for i in range(2, len(lst)):
        siftup(lst, i)
        
    #del lst[0]
    return lst

def EmptyHeap(lst): 
    returnlst=deepcopy(lst)
    returnlst=returnlst[:-1]
    for i in range(len(returnlst)):
        returnlst[i]=lst[1]
        lst[1]=lst[-1]
        del lst[-1]
        siftdown(lst)
        
    return returnlst

def HeapSort(lst):
    lst=MakeHeap(lst)
    lst=EmptyHeap(lst)
    
    return lst
print(HeapSort(tc1))