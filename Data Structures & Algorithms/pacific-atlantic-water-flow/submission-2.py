class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        pacific_result = set()
        arabic_result =set()
        def dfs(r,c,result, prev):
            if(r<0 or r>=rows or c<0 or c>=cols or (r,c) in result or heights[r][c]<prev):
                return
            result.add((r,c))
            for rc,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+rc,c+cc
                dfs(nr,nc, result,heights[r][c])

        for r in range(rows):
            dfs(r,0,pacific_result,0)
            dfs(r,cols-1,arabic_result,0)
        for c in range(cols):
            dfs(0,c,pacific_result,0)
            dfs(rows-1,c,arabic_result,0)
        return [[r, c] for r, c in pacific_result if (r, c) in arabic_result]


        