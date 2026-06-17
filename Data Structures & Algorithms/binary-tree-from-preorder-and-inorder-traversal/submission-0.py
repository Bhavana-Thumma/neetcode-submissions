# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={v:i for i,v in enumerate(inorder)}
        print(d)
        pre = 0 
        def dfs(left, right):
            nonlocal pre
            if(left>right):
                return
            rv = preorder[pre]
            pre+=1
            root = TreeNode(rv)
            indx = d[rv]
            root.left = dfs(left,indx-1)
            root.right = dfs(indx+1,right)
            return root
        return dfs(0, len(preorder)-1)


            