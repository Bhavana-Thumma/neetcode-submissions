# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def hashTree(node, seen):

            if not node:
                return 0
            curr = (hashTree(node.left, seen), node.val, hashTree(node.right,seen))
            seen.add(curr)
            return curr
        seen=set()
        hashTree(root, seen)
        h = hashTree(subRoot, set())
        return h in seen
            


