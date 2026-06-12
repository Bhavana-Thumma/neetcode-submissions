# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if q.val != p.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)

"""
isSameTree(1,1) 
|
|---isSameTree(2,2)
||||----isSameTree(null,null) - True --- True
||||----isSameTree(null,null) - True ---
|---isSameTree(3,3)                           ---True
||||----isSameTree(null,null) - True
||||----isSameTree(null,null) - True ---True 
"""