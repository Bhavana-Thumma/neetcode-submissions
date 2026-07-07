from collections import defaultdict,deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        components = 0
        def bfs(node):
            q = deque([node])
            visited.add(node)
            while(q):
                nd = q.popleft()
                if nd not in visited:
                    visited.add(nd)
                for nei in graph[nd]:
                    if nei not in visited:
                        q.append(nei)
                    
        for node in range(n):
            if node not in visited:
                components+=1
                bfs(node)
        return components

        