# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:11:26 2021

@author: dhk1349
"""
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        container=set()
        tmp=""
        for l in word:
            if ord(l) <=ord('9') and ord(l)>=ord('0'):
                tmp+=l
                
            else:
                if tmp=="":
                    continue
                container.add(int(tmp))
                tmp=""
        if tmp != "":
            container.add(int(tmp))
        return len(container)