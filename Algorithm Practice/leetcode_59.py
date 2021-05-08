# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:33:06 2021

@author: dhk1349
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        condition=["right", "down", "left", "up"]# or left up down
        mode=0
        out=[]
        cursor=[0, 0]  # r, c
        
        # though inefficient, make null matrix first.
        for _ in range(n):
            row=[]
            for _ in range(n):
                row.append(0)
            out.append(row)
        for i in range(n**2):
            # print(f"{mode}: {cursor[0]}, {cursor[1]}-> {i+1}")
            out[cursor[0]][cursor[1]] = i+1
            if mode==0:
                cursor[1]+=1    
            elif mode==1:
                cursor[0]+=1
            elif mode==2:
                cursor[1]-=1
            elif mode==3:
                cursor[0]-=1
            
            if -1>=cursor[0] or cursor[0] == n or -1>=cursor[1] or cursor[1] == n or out[cursor[0]][cursor[1]]!=0:
                if mode==0:
                    cursor[1]-=1
                    cursor[0]+=1
                elif mode==1:
                    cursor[0]-=1
                    cursor[1]-=1
                elif mode==2:
                    cursor[1]+=1
                    cursor[0]-=1
                elif mode==3:
                    cursor[0]+=1
                    cursor[1]+=1
                mode+=1
                mode%=4
                
                

        # print(out)
        return out
            