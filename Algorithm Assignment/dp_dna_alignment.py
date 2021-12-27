# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 02:05:27 2020

@author: dhk1349
"""
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%4d" %matrix[i][j], end=" ")
        print()

def _printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

#a=['A','A','C','A','G','T','T','A','C','C']
#b=['T','A','A','G','G','T','C','A']
        
#데이터1
a=['A', 'G', 'G', 'T', 'A']
#데이터2
b=['A', 'T', 'G', 'C', 'A']

m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]

for j in range(n-1,-1,-1):
    table[m][j] =table[m][j+1]+2

for i in range(m-1,-1,-1):
    table[i][n] =table[i+1][n]+2

for diagonal in range(m+n-2,-1,-1):
    for j in range(min(diagonal,n-1),max(diagonal-m,-1),-1):
        #print(diagonal-j,", ", j," ", end=" ")
        if(a[diagonal-j]==b[j]):
            panelty=0
        else:
            panelty=1
        #table[diagonal-j][j]=min(table[diagonal-j+1][j+1]+panelty, min(table[diagonal-j+1][j]+2,table[diagonal-j][j+1]+2))
        if(table[diagonal-j+1][j]+2>table[diagonal-j][j+1]+2):
            if(table[diagonal-j][j+1]+2>table[diagonal-j+1][j+1]+panelty):
                #대각이 선행 원소
                table[diagonal-j][j]=table[diagonal-j+1][j+1]+panelty
                minindex[diagonal-j][j]=(diagonal-j+1,j+1)
            else:
                table[diagonal-j][j]=table[diagonal-j][j+1]+2
                minindex[diagonal-j][j]=(diagonal-j,j+1)
        else:
            if(table[diagonal-j+1][j]+2>table[diagonal-j+1][j+1]+panelty):
                table[diagonal-j][j]=table[diagonal-j+1][j+1]+panelty
                minindex[diagonal-j][j]=(diagonal-j+1,j+1)
            else:
                table[diagonal-j][j]=table[diagonal-j+1][j]+2
                minindex[diagonal-j][j]=(diagonal-j+1,j)
    #print()
        

#print matrix

printMatrix(table)

#_printMatrix(minindex)

x=0
y=0

while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ",  b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")
