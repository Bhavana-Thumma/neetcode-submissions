class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #O(n)
            sn = target - nums[i]
            try:
                indx = nums.index(sn, i+1, len(nums))
            except:
                continue

            if(indx != i):
                return [i, indx]
                



        