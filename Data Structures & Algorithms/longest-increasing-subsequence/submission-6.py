#Bottom up dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]* (n)
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis = max(dp[i], 1+dp[j])
                    dp[i] =lis
        return max(dp)