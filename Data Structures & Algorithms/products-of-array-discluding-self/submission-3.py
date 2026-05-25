class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        suffix =1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]     

        return output

# 1 2 3 4 5

# 2 3 4 5 - 0
# 3 4 5 1 - 1
# 4 5 1 2 - 2
# 5 1 2 3 - 3
# 1 2 3 4 - 4
