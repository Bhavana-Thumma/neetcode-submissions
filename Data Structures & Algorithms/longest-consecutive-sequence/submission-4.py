class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prev = 0
        c = 0
        pointer  = nums[0]
        for i in range(len(nums)):
            if(nums[i] == pointer):
                c += 1
                pointer += 1
            # elif(i > 0 and ):
            #     continue
            elif(nums[i] != nums[i-1]+1 and nums[i] != nums[i-1]):
                if(prev < c):
                    prev = c
                c = 1
                pointer = nums[i]+1
        return max(prev, c)
