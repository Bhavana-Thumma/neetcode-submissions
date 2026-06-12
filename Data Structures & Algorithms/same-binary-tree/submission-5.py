# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def stringify(root):
            if not root:
                return '#'
            return str(root.val)+stringify(root.left)+stringify(root.right)
        return stringify(p) ==stringify(q)
        