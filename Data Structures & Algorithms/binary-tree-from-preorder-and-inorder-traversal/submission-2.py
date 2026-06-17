# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0
        for num in (preorder[1:]):
            node = TreeNode(num)
            if(stack[-1].val != inorder[inorder_index]):
                stack[-1].left = node
            else:
                while(stack and stack[-1].val == inorder[inorder_index]):
                    parent = stack.pop()
                    inorder_index+=1
                parent.right = node
            stack.append(node)
        return root
        