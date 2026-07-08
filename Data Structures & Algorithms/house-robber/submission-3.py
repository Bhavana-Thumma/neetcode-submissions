class Solution:
    def rob(self, nums: List[int]) -> int:
        next1 = 0
        next2 = 0
        n=len(nums)
        for i in range(len(nums)-1,-1,-1):
            current = max(nums[i]+next2, next1)
            next2 = next1
            next1=current
        return next1