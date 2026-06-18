# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def gain(node):
            if not node:
                return 0, float('-inf')
            leftgain, left_max_sum = gain(node.left)
            rightgain, right_max_sum = gain(node.right)
            leftgain = max(leftgain,0)
            rightgain = max(rightgain, 0)
            path_through = node.val+leftgain+rightgain
            node_gain = node.val + max(leftgain, rightgain)
            max_sum = max(path_through, left_max_sum, right_max_sum)
            return node_gain, max_sum
        _, max_sum = gain(root)
        return max_sum

        