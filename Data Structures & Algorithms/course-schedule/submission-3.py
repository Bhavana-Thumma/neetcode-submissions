from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for c,p in prerequisites:
            graph[p].append(c)
            indegree[c] +=1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finished = 0
        while(q):
            c = q.popleft()
            finished+=1
            for course in graph[c]:
                indegree[course] -=1
                if(indegree[course] == 0):
                    q.append(course)

        return finished == numCourses
            
        