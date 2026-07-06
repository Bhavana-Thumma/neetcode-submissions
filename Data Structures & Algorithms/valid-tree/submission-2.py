# A tree with n nodes must have exactly n - 1 edges.
# A graph is a tree if and only if:

# No cycles
# All nodes are connectedA graph is a tree if and only if:

# No cycles
# All nodes are connected
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) != n-1):
            return False
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        print(graph)
        visited = set()
        q = deque([(0,-1)])
        while(q):
            node,parent = deque.popleft(q)
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei != parent:
                    q.append((nei,node))
       
        return len(visited) == n

        