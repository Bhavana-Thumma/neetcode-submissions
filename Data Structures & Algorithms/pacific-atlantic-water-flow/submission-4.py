from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        pacific_visited, arabic_visited = set(),set()

        def bfs(starts,visited):
            q = deque(starts)
            for (r,c) in starts:
                visited.add((r,c))
            while(q):
                r,c = deque.popleft(q)
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = r+dr,c+dc
                    if(0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr,nc))
                        q.append((nr,nc))       
        

        pacific_starts = [(r,0) for r in range(rows)] + [(0,c) for c in range(cols)]
        arabic_starts = [(rows-1,c) for c in range(cols)] + [(r,cols-1) for r in range(rows)]
        bfs(pacific_starts,pacific_visited)
        bfs(arabic_starts,arabic_visited)
        result  = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_visited and (r,c) in arabic_visited:
                    result.append([r,c])
        return result
               