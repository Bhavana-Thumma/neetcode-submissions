from collections import defaultdict,deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        components = 0
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
            return True


        for node in range(n):
            if node not in visited:
                components+=1
                dfs(node)
        return components

        