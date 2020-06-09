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
        


    def siftUp(self, i):
        while(i>=2):
            
             #구현
    def siftDown(self,i):
        siftkey=self.data[i]
        parent=i
        spotfound=False
        while(2*parent<self.data.n and !spotfound):
            if(2*parent<self.data.n and self.data[2*parent]<self.data[2*parent+1]):
                largerparent=2*parent+1
            else:
                largerparent=2*parent
            if(siftkey<self.data[largerparent]):
                self.data[parent]=self.data[largerparent]
                #swap으로 해야하지 않을까 
            else:
                spotfound=True
        self.data[parent]=siftkey
        

    def makeHeap2(self):  
        
     #구현

    def root(self):
        out=self.data[1]
        self.data[1]=self.data[self.n]
        self.n-=1
        siftdown(1)
        return out

        #if(self.n>0):
# 추가 하였음. 힙 이 더 이상없을 때는 down 없음
             
              #구현
        #return keyout
    
    def removeKeys(self):

          #구현
    
    def heapSort(a):

          #구현
          
# 인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가    
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort(a)
print(s)
