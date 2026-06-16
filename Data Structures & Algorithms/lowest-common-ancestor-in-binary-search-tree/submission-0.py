# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # task1: iterate over the tree
        # task2: check if node == p or ==q then check node.left or right ==q or p:
        #     if true return node.val
        # task 3: if node.val is not p or q
        #  if(node.left == p and node.right==q or (node.left == q and node.right==p ):
        #     return node.val
        # if not node:
        #     return None
        def dfs(node):
            if not node:
                return None
            if(p.val<node.val and q.val<node.val):
                return dfs(node.left)
            elif(p.val>node.val and q.val>node.val):
                return dfs(node.right)
            return node
            
        return dfs(root)
            

            
        

            
        