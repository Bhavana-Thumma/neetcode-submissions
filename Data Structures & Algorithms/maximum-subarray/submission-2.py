#Bruteforce Solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        n = len(nums)
        for i in range(n):
            total =0
            for j in range(i, n):
                total+=nums[j]
                ans =max(ans,total)
        return ans
        