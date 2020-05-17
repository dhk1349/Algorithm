# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:43:41 2020

@author: dhk13
"""
class Container:
    def __init__(self):
        self.SetCont=[]

class SetType:
    def __init__(self):
        self.Nodes=[]
        self.EdgeContainter=[]
        
    def find(Edge):
        cnt=0
        for i in range(1,len(Egde)+1):
            if i in self.Nodes:
                cnt+=1
        return cnt        
        
    def eq(otherSet):
        for i in otherSet.Nodes:
            if i in self.Nodes:
                return 0
        return 1
    
    def union(self):
        

def kruskal(graph):
    #initializing parent and rank.
    MST=set()
    cnt=0
    for i in graph['vertices']:
        make_singleton_set(i)
    
    #Edge를 비내림차순으로 정렬 
    Ordered=list(graph['edges'])
    Ordered.sort()
    #Iteration
    while(len(graph['vertices'])-1>cnt):
        if(len(Ordered)==0):
            break
        else:
            r1=find(Ordered[0][1])
            r2=find(Ordered[0][2])
            if(r1!=r2):
                #print(Ordered[0], "ADDED")
                MST.add(Ordered[0])
                if rank[r1] >= rank[r2]:
                    parent[r2] = r1
                    rank[r1] += rank[r2]
                elif rank[r1]<rank[r2]:
                    parent[r1] = r2
                    rank[r2] += rank[r1]   
            #else:
                #print(Ordered[0], "NOT ADDED")
            Ordered.remove(Ordered[0])
    return MST
            
        
        
graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
            (1, 'A', 'B'),
            (3, 'A', 'C'),
            (3, 'B', 'C'),
            (6, 'B', 'D'),
            (4, 'C', 'D'),
            (2, 'C', 'E'),
            (5, 'D', 'E'),
            ])
        }
mst=kruskal(graph)
print(mst)