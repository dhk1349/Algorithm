# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:05:14 2020

@author: dhk13

Order edges in descending order.

Add edge to minimum spanning tree if selected egde does not make cycle.
"""
parent = dict()
rank = dict()

def make_singleton_set(v):
    #시작 원소를 만드는 지정해서 v에 넣으면 된다. 
    parent[v] = v
    rank[v] = 1

def find(v):
    #Recursive function parent[v]=v일 때 까지 올라감. 
    #즉, root를 리. 
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(r1, r2):
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: rank[r2] += rank[r1]

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
