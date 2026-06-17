# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre =  0
        def dfs(inorder_l):
            nonlocal pre
            if not inorder_l:
                return None
            rv = preorder[pre]
            pre+=1
            root = TreeNode(rv)
            mid = inorder_l.index(rv)
            root.left = dfs(inorder_l[:mid])
            root.right = dfs(inorder_l[mid+1:])
            return root
        return dfs(inorder)