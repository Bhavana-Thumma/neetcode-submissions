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
            left_gain, left_max_path_through = gain(node.left)
            right_gain, right_max_path_through = gain(node.right)
            left_gain = max(left_gain, 0)
            right_gain = max(right_gain, 0)
            node_gain = node.val + max(left_gain, right_gain)
            path_through = node.val + left_gain + right_gain
            max_path_through = max(path_through, left_max_path_through, right_max_path_through)
            return node_gain, max_path_through
        gain, max_path_through = gain(root)
        return max_path_through 

        