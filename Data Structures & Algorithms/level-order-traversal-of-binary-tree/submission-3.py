# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        curr_lvl =[root]
        r = []
        while(curr_lvl):
            lvl_l = []
            nxt = []
            for node in curr_lvl:
                lvl_l.append(node.val)
                if(node.left):
                    nxt.append(node.left)
                if(node.right):
                    nxt.append(node.right)
            r.append(lvl_l)
            curr_lvl = nxt
        return r




        