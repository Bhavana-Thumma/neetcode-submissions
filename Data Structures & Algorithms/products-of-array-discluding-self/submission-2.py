class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suff = [1]*len(nums)
        for i in range(len(nums)):            
            if(i>0):
                prefix[i] = prefix[i-1]*nums[i-1]
        for j in range(len(nums)-1, -1, -1):
            if(j<len(nums)-1):
                suff[j] = suff[j+1]*nums[j+1]
        for k in range(len(nums)):
            prefix[k] = prefix[k]*suff[k]           

        return prefix

# 1 2 3 4 5

# 2 3 4 5 - 0
# 3 4 5 1 - 1
# 4 5 1 2 - 2
# 5 1 2 3 - 3
# 1 2 3 4 - 4
