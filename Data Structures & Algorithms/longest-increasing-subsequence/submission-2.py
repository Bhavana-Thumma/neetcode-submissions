class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        def dfs(i,j):
            if i==n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            lis = dfs(i+1,j)
            if j==-1 or nums[i]>nums[j]:
                lis = max(lis, 1+dfs(i+1,i))
            dp[(i,j)] = lis
            return lis
        return dfs(0,-1)