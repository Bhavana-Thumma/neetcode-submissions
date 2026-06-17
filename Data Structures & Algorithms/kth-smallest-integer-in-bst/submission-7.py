# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1

class Solution:
    def size(self,node):
        if not node:
            return 0
        left = self.size(node.left)
        right = self.size(node.right)
        node.size = left+right+1
        return node.size
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Augumented binary search tree implementation
        self.size(root)
        while(root):
            leftsize = root.left.size if root.left else 0 
            if(k == leftsize+1):
                return root.val
            elif(k<=leftsize):
                root = root.left
            else:
                k-= leftsize+1
                root=root.right
                        
            
            