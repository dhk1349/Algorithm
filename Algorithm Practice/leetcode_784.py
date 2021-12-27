# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:24:45 2021

@author: dhk1349
"""
class Solution:
    def letterCasePermutation(self, _S: str) -> List[str]:
        cont=[]
        out=[]
        for idx, l in enumerate(_S):
            if ord(l)<=ord("z") and ord(l)>=ord("A"):
                cont.append(idx)
        #2**(len(cont)+1)-1
        # print(2**(len(cont)))
        if len(cont)==0:
            return [_S]
        
        for i in range(0, 2**(len(cont))): # number of permutation
            controller = str(bin(i))[2:].zfill(len(cont))     # like 000001
            S=_S
            for idx, i in enumerate(controller):
                
                if i == "0":
                    if cont[idx]+1!=len(S):
                        S = S[:cont[idx]]+S[cont[idx]].lower()+S[cont[idx]+1:]
                    else:
                        S = S[:cont[idx]]+S[cont[idx]].lower()
                else:
                    if cont[idx]+1!=len(S):
                        S = S[:cont[idx]]+S[cont[idx]].upper()+S[cont[idx]+1:]
                    else:
                        S = S[:cont[idx]]+S[cont[idx]].upper()
            out.append(S)
            
        return out