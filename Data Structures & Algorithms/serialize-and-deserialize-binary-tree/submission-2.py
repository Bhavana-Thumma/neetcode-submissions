# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'
        result = []
        q = deque([root])
        while(q):
            node = deque.popleft(q)
            if not node:
                result.append("#")
                continue
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)         
        return ",".join(result)        
     
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        if(vals[0]=='#'):
            return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i=1
        while(q):
            node = deque.popleft(q)
            if vals[i] != '#':                
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i+=1
            if vals[i] != '#':
                node.right = TreeNode(vals[i])
                q.append(node.right)
                
            i+=1

        return root
