# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, depth):
            if not node:
                return
            self.ans = max(self.ans, depth)
            dfs(node.left, 1+depth)
            dfs(node.right, 1+depth)
        dfs(root,1)
        return self.ans