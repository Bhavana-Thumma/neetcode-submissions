class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #LIS largest increasing subsequence
        # i : current index, j: prev index
        n = len(nums)
        dp = [[0]*n for i in range(n)]
        def dfs(i, j):
            if i==n:
                return 0
            if dp[i][j]:
                return dp[i][j]
            lis = dfs(i+1, j)
            if j==-1 or nums[i]>nums[j]:
                lis = max(lis, 1+dfs(i+1,i))
            dp[i][j] = lis
            return lis
        return dfs(0,-1)