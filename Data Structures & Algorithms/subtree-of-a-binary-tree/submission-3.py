# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self,node, subroot):
        if not node and not subroot:
            return True
        if not node or not subroot:
            return False
        if node.val != subroot.val:
            return False
        return self.isSame(node.left, subroot.left) and self.isSame(node.right, subroot.right)   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        size ={}
        height = {}
        def getSize(node):
            if not node:
                return 0
            size[node]= 1+getSize(node.left)+getSize(node.right)
            return size[node]
        def getHeight(node):
            if not node:
                return 0
            height[node]= 1+max((getHeight(node.left),getHeight(node.right)))
            return height[node]
        getSize(root)
        getHeight(root)
        subrootsize = getSize(subRoot)
        subrootheight = getHeight(subRoot)
        def dfs(node):
            if not node:
                return False
            if(size[node] == subrootsize and height[node] == subrootheight and self.isSame(node, subRoot)):           
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
        