# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:36:17 2021

@author: dhk1349
"""
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # 성분이 다른 두개 맞출 때 1번 - 최우선 순위
        # 성분은 같은 두 개를 맞출 때 2번
        # 다른 것의 갯수가 홀수면 불가능

        total=0
        xcnt=0
        ycnt=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                print(f"{i}th: {s1[i]}")
                if s1[i]=="x":
                    xcnt+=1
                else:
                    ycnt+=1
        if (xcnt+ycnt)%2==1:
            return -1
        # XX
        total+=(xcnt//2)
        # YY
        total+=(ycnt//2)
        # XY
        if xcnt%2==1:
            total+=2

        return total
        