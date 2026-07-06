class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        components = n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for u,v in edges:
            pu = find(u)
            pv = find(v)
            if(pu != pv):
                parent[pu] = pv
                components -=1
        return components




        