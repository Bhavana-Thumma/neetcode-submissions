# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        post_order = []
        to_visit = [root]
        gain = {}
        max_sum = float('-inf')
        while(to_visit):
            n = to_visit.pop()
            post_order.append(n)
            if n.left: to_visit.append(n.left)
            if n.right: to_visit.append(n.right)
        for n in reversed(post_order):
            leftgain = max(gain.get(n.left, 0), 0)
            rightgain = max(gain.get(n.right, 0), 0)
            pathrough = n.val + leftgain+rightgain
            max_sum = max(pathrough, max_sum)
            n_gain = n.val + max(leftgain,rightgain)
            gain[n] = n_gain
        return max_sum
            


        