class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # union-find solution
        if len(edges) != n-1:
            return False
        parent = list(range(n))
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for u,v in edges:
            pu = find(u)
            pv = find(v)
            if(pu == pv):
                return False
            parent[pu] = pv
        return True
