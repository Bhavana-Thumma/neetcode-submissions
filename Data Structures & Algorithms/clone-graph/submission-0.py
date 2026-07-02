"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        def dfs(node):
            if not node:
                return None
            if node in clone:
                return clone[node]
            newnode = Node(node.val)
            clone[node] = newnode
            for n in node.neighbors:
                newnode.neighbors.append(dfs(n))
            return newnode        
        return dfs(node)