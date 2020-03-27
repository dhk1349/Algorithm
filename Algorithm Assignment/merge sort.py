# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:55:41 2020

@author: dhk1349
"""


n=[27, 10, 12, 20, 25, 13, 15, 22]

def merge(mid, left, right, n):
    leftcnt=0
    rightcnt=0
    while(leftcnt!=len(left) and rightcnt!=len(right)):
        if left[leftcnt]>right[rightcnt]:
            n[leftcnt+rightcnt]=right[rightcnt]
            rightcnt+=1
        else:
            n[leftcnt+rightcnt]=left[leftcnt]
            leftcnt+=1
    if (leftcnt==len(left)):
        #finish right list
        while (rightcnt!=len(right)):
            n[leftcnt+rightcnt]=right[rightcnt]
            rightcnt+=1
    else:
        while (leftcnt!=len(left)):
            n[leftcnt+rightcnt]=left[leftcnt]
            leftcnt+=1
    print("merging: ", n)
            
def merge_sort(length, n):
    mid=int(length/2)
    print(n)
    print(mid)
    print("length: ", length)
    left=[n[i] for i in range(mid)]
    right=[n[i] for i in range(mid, length)]
    
    if (length>1):
        
        merge_sort(mid, left) #left
        merge_sort(length-mid, right) #right
        merge(mid, left, right, n)
    return n

print(merge_sort(len(n), n))