class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)): #O(n)
            d[nums[i]] = d.get(nums[i], i)
            sn = target - nums[i]
            idx = d.get(sn, -1)
            if(idx != -1 and  idx != i):
                return [idx, i]
            





        