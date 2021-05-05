# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        use queue
        """
        q=[]
        ser=[]
        q.append(root)
        while len(q)!=0:
            ser, q=self.recursive_ser(ser, q)
        returnser=""
        first=True
        for e in range(len(ser)-1,-1, -1):
            if ser[e] == "null" and first==True:
                continue
            else:
                first=False
                returnser=str(ser[e])+"\t"+returnser
        return returnser
    
    def recursive_ser(self, ser, q):
        node= q[0]
        q=q[1:]
        if node != None:
            # ser=ser+str(node.val)+"\t"
            ser.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            ser.append("null")
        return ser, q

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        left right separately, recursively find children
        """
        lst=data.split("\t")
        if data=="":
            return []
        lst=lst[:-1]
        root=TreeNode(lst[0])
        level=1
        bound=2
        iter=0
        for idx, elem in enumerate(lst[1:]):
            path=str(bin(iter)[2:]).zfill(level)
            self.recursive_des(path, root, elem)
            iter+=1
            if iter==bound:
                bound*=2
                iter=0
                level+=1
        return root
    
    def recursive_des(self, path, root, data):
        # print(f"path for {data}: {path}")
        cursor=root
        for p in range(len(path)-1):
            if path[p]=='0':
                cursor=cursor.left
            elif path[p]=='1':
                cursor=cursor.right
        if path[-1]=='0':
            cursor.left=TreeNode(data)
        elif path[-1]=='1':
            cursor.right=TreeNode(data)
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
