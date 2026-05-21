class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)): #O(n)
            sn = target - nums[i]
            if (sn in d):
                return [d[sn], i]
            d[nums[i]] = i
            





        