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
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if(pu == pv):
                return False
            parent[pu] = pv
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return False
        return True
