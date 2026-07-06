from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        processing =set()
        for c,p in prerequisites:
            graph[c].append(p)
        def dfs(course):
            if graph[course] == []:
                return True
            if course in processing:
                return False
            processing.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            processing.remove(course)
            graph[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True