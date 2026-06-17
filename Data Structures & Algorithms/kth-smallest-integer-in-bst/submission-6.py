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
        while(curr):
            if not curr.left:
                k-=1
                if(k==0):
                    return curr.val
                curr=curr.right
            else:
                pred = curr.left
                while(pred.right and pred.right !=curr):
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                elif(pred.right == curr):
                    pred.right = None
                    k-=1
                    if(k==0):
                        return curr.val
                    curr = curr.right
        # Time: O(n) & Space: O(1)
                   
            
            