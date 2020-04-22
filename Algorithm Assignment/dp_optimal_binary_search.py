# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:29:49 2020

@author: dhk1349
"""

class Node:
    def __init__(self, data):
        self.l_child=None
        self.r_child=None
        self.data=data
    
def tree(key, r, i, j):     
    k=r[i][j]
        
    if (k==0):
        return 
    else:
        p=Node(key[k])
        p.l_child=tree(key, r, i, k-1)
        p.r_child=tree(key, r,k+1, j)
        return p
    
def printMatrix(d):
    m=len(d)
    n=len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" %d[i][j], end=" ")
        print()
    
def printMatrixF(d):
    m=len(d)
    n=len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%5.2f" %d[i][j], end=" ")
        print()

def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)

#presetting the variables
key=[' ', 'A', 'B', 'C', 'D']
p=[0, 0.375, 0.375, 0.125, 0.125]

def optimal_bs_tree(key, p):
    n=len(p)-1
    a=[[0 for j in range(0, n+2)] for i in range(0,n+2)]
    r=[[0 for j in range(0, n+2)] for i in range(0,n+2)]
    
    for i in range(1, n+1):
        a[i][i-1]=0
        a[i][i]=p[i]
        r[i][i]=i
        r[i][i-1]=0

    a[n+1][n]=0
    r[n+1][n]=0
    for diagonal in range(1, n):
        for column in range(n-diagonal):
            a[column+1][column+1+diagonal]=a[column+1][column]+a[column+2][column+1+diagonal]+sum([p[n] for n in range(column+1, column+2+diagonal)])
            r[column+1][column+1+diagonal]=column+1
            #print(column+1, ", ", column+1+diagonal)
            for k in range(column+2, column+2+diagonal):
                if (a[column+1][column+1+diagonal]>a[column+1][k-1]+a[k+1][column+1+diagonal]+sum([p[n] for n in range(column+1, column+2+diagonal)])):
                    a[column+1][column+1+diagonal]=a[column+1][k-1]+a[k+1][column+1+diagonal]+sum([p[n] for n in range(column+1, column+2+diagonal)])
                    r[column+1][column+1+diagonal]=k
                
    return a, r, n
a,r, n=optimal_bs_tree(key, p)
printMatrixF(a)
print()
printMatrix(r)

root=tree(key, r, 1, n)
print_inOrder(root)
print()
print_preOrder(root)