# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        container1 = []
        container2 = []
        
        if root1!=None:
            container1=self.inorder(root1, container1)
        
        if root2!=None:
            container2=self.inorder(root2, container2)
                
        out=[]
        while True:
            if len(container1)==0 or len(container2)==0:
                break
            
            if container1[0]<container2[0]:
                out.append(container1[0])
                container1=container1[1:]
            else:
                out.append(container2[0])
                container2=container2[1:]
        
        if len(container1)==0 and len(container2)!=0:
            out.extend(container2)
        elif len(container1)!=0 and len(container2)==0:
            out.extend(container1) 
        return out
        
        
    def inorder(self, node, container): #inorder
             
        #travel left
        if node.left!=None:
            container=self.inorder(node.left, container)
        
        container.append(node.val)
        
        #travel right
        if node.right!=None:
            container=self.inorder(node.right, container)
    
        
        return container
