# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:32:05 2021

@author: dhk1349
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        q=[]
        out=[]
        out=self.recursive(root, out)
        return out
    
    def recursive(self, root, out):
        if root.val==None:
            return out
        out.append(root.val)
        if root.left!=None:
            out=self.recursive(root.left, out)
        if root.right!=None:
            out=self.recursive(root.right, out)
        
        return out