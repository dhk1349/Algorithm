# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:00:41 2021

@author: dhk1349
"""
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        ans=""
        loc=0
        cursor=[0, 0]     #r, c
        while loc<len(target):
            r, c = self.find(target[loc], board)
            rowtomove = r - cursor[0]
            coltomove = c - cursor[1]
            if coltomove < 0:
                for i in range(abs(coltomove)):
                    ans+="L"
            
            if rowtomove > 0:
                for i in range(abs(rowtomove)):
                    ans+="D"
            elif rowtomove < 0:
                for i in range(abs(rowtomove)):
                    ans+="U"
            if coltomove > 0:
                for i in range(abs(coltomove)):
                    ans+="R"
            cursor = [r, c]
            ans+="!"
            loc+=1
        return ans
    
    def find(self, a, board):
        for r, row in enumerate(board):
            for c, k in enumerate(row):
                if a==k:
                    return r, c
        return None, None
        
        