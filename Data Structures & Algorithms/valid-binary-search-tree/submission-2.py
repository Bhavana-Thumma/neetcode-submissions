# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        prev = None
        node = root
        stack =[]
        while stack or node:    
            while(node):
                stack.append(node)
                node = node.left
        
            node = stack.pop()
            print('2',node.val)
            if prev != None and node.val <= prev:
                return False
            prev = node.val
            node = node.right
        return True
            
        