# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:32:10 2020

@author: dhk1349

빠른 정렬은  quickSort()함수로,
큰 정수 곱셈은 prod2()함수를 통해 실행합니다.
prod2함수에서 threshold 값은 4이다.
"""

import math

def quickSort(s, low, high):
    #구현
    pivotpoint=0
    if(high>low):
        pivotpoint=partition(s, low, high)
        quickSort(s, low, pivotpoint-1)
        quickSort(s, pivotpoint+1, high) 
    
def partition(s,low, high):
    #구현
    pivotitem=s[low]
    j=low
    for i in range(low+1, high+1):
        if(pivotitem>s[i]):
            j+=1
            #exchange
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
    #j는 pivotpoint이다.
    temp=s[low]
    s[low]=s[j]
    s[j]=temp
    #pivotpoint인 j를 리
    return j 
    

s=[3, 5, 2, 9, 10, 14, 4, 8]
#quickSort(s, 0, 7)
#print(s)


def prod2(a,b):
    #구현
    n=max(len(str(a)),len(str(b)))
    th=4
    if(a==0 or b==0):
        return 0
    elif (n<th):
        return a*b
    else:
        m=math.floor(n/2)
        x=a//pow(10,m)
        y=a%pow(10,m)
        w=b//pow(10,m)
        z=b%pow(10,m)
        r=prod2(x+y, w+z)
        p=prod2(x,w)
        q=prod2(y,z)
        return p*pow(10,2*m)+(r-p-q)*pow(10,m)+q
    
    
a=1234567812345678
b=2345678923456789

#print(prod2(a,b))
#print(a*b)
while True:
    print("#1 빠른 정렬 알고리즘\n#2 큰 정수 곱셈 알고리즘\n1,2 이외의 숫자로 EXIT")
    opt=input("Input: ")

    if(opt=='1'):
        opt=input("\t1: 주어진 예시 사용\n\t2: 직접 예시 입력\n\t")
        if(opt=='1'):
            print("list: ", s)
            quickSort(s, 0, 7)
            print("result: ", s,"\n")
        
        elif(opt=='2'):
            n=int(input("리스트의 길이를 입력하세요: "))
            s=[]
            print("원소를 하나씩 입력해주세요.")
            for i in range(n):
                elem=int(input("정수 원소 입력: "))
                s.append(elem)
            quickSort(s, 0, n-1)
            print("result", s, "\n")
        else:
            print("Illegal Input\n")
    
    
    elif (opt=='2'):
        opt=input("\t1: 주어진 예시 사용\n\t2: 직접 예시 입력\n\t")
        if(opt=='1'):
            print("Input1: ", a, "\nInput2: ",b)
            print(prod2(a,b),"\n")
        
        elif(opt=='2'):
            input1=int(input("큰 정수 1: "))
            input2=int(input("큰 정수 2: "))
            print("result: ", prod2(input1, input2),"\n")
        
        else:
            print("Illegal Input\n")
    
    else:
        print("EXITING PROGRAM...")
        break

