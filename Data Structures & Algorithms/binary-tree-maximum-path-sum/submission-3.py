# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def gain(node):
            nonlocal max_sum
            if not node:
                return 0
            leftgain = max(gain(node.left), 0)
            rightgain = max(gain(node.right), 0)
            path_through = node.val+leftgain+rightgain
            max_sum = max(max_sum, path_through)
            return node.val + max(leftgain, rightgain, 0)
        gain(root)
        return max_sum

        