class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        components = n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if(pu == pv):
                return False
            parent[pu] = pv
            return True
        for u,v in edges:
            if union(u,v):
                components -=1
        return components




        