# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 01:42:59 2020

@author: dhk1349
"""

import math
class Heap(object):
    n=0
    
    def __init__(self, data):
        self.data=data
# heap size를 하나 줄여야 한다. 인덱스는 1부터. 인덱스의 2* 연산 가능하도록.
        self.n=len(self.data)-1
        
    def addElt(self,elt):
        self.data.append(elt)
        self.n+=1
        self.siftUp(self.n)


    def siftUp(self, i):
        cursor=i
        elem=self.data[i]
        while(cursor>=2):
            if(self.data[math.floor(cursor/2)]<elem):
                self.data[cursor]=self.data[math.floor(cursor/2)]
            else: 
                break
            cursor=math.floor(cursor/2)
        self.data[cursor]=elem
             
    def siftDown(self,i):
        siftkey=self.data[i]
        parent=i
        spotfound=False
        while(2*parent<=self.n and not spotfound):
            if(2*parent<self.n and self.data[2*parent]<self.data[2*parent+1]):
                largerparent=2*parent+1
            else:
                largerparent=2*parent
            if(siftkey<self.data[largerparent]):
                #temp=self.data[parent]
                self.data[parent]=self.data[largerparent]
                #self.data[largerparent]=temp
                parent=largerparent
            else:
                spotfound=True
        self.data[parent]=siftkey
        

    def makeHeap2(self):  
        for i in range(math.floor(self.n/2), 0, -1):
            self.siftDown(i)
        
    def root(self):
        if(self.n>0):
            out=self.data[1]
            self.data[1]=self.data[self.n]
            self.data[self.n]=-1
            self.n-=1
            self.siftDown(1)
            return out
        return -1

        #if(self.n>0):
# 추가 하였음. 힙 이 더 이상없을 때는 down 없음
             
              #구현
        #return keyout
    
    def removeKeys(self):
        s=[]
        for i in range(self.n, 0,-1):
            s.append(self.root())
        return s
    
def heapSort(a):
    _heap=Heap(a)
    _heap.makeHeap2()
    sort=_heap.removeKeys()
    return sort
          
# 인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가    
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort(a)
print(s)
