# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        d = {}
        next_id =1
        seen=set()
        def hashTree(node):
            nonlocal next_id
            if not node:
                return 0
            curr = (hashTree(node.left), node.val, hashTree(node.right))
            if(curr not in d):
                d[curr] = next_id
                next_id+=1
            currID = d[curr]
            seen.add(currID)
            return currID
        hashTree(root)
        def getHash(node):
            nonlocal next_id
            if not node:
                return 0
            curr = (hashTree(node.left), node.val, hashTree(node.right))
            if(curr not in d):
                d[curr] = next_id
                next_id+=1
            currID = d[curr]
            return currID
        target = getHash(subRoot)
        return target in seen
            


