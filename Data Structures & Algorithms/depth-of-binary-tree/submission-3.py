# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root,1)])
        while(q):
            node,depth = q.popleft()
            if not node:
                return 0
            ans = max(ans, depth)
            if(node.left):
                q.append((node.left, 1+depth))
            if(node.right):
                q.append((node.right, 1+depth))

        return ans