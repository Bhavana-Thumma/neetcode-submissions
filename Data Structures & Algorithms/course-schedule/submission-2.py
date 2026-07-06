from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0]*numCourses
        graph = defaultdict(list)
        for c,p in prerequisites:
            graph[c].append(p)
        def dfs(c):
            if state[c] == 1:
                return False
            if state[c] == 2:
                return True
            state[c] = 1
            for p in graph[c]:
                if not dfs(p):
                    return False
            state[c] = 2
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
# 3 states solutions