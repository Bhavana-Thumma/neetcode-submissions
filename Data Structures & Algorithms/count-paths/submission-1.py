class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            r = dfs(i+1,j)
            l = dfs(i,j+1)
            dp[(i,j)] = r+l
            return r+l
        return dfs(0,0)