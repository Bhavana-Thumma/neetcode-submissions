# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Morris Traversal for inorder traversal
        curr = root
        res=[]
        if not root:
            return None
        while(curr):
            if(curr.left):
                pred = curr.left
                while(pred.right and pred.right!=curr):
                    pred =pred.right
                
                if(pred.right == None):
                    pred.right = curr
                    curr = curr.left
                elif(pred.right==curr):
                    pred.right = None
                    res.append(curr)
                    curr=curr.right
            else:
                res.append(curr)
                curr = curr.right
        return res[k-1].val
            
            