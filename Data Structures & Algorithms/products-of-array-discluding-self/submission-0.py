class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1] * len(nums)
        output = [1]*len(nums)
        for i in range(len(nums)):
            for k in nums[i+1:]+nums[:i]:
                op[i] = op[i] * k
        return op

# 1 2 3 4 5

# 2 3 4 5 - 0
# 3 4 5 1 - 1
# 4 5 1 2 - 2
# 5 1 2 3 - 3
# 1 2 3 4 - 4
