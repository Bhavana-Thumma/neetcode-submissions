class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = float('inf')
        l = 0
        r = len(nums)-1
        while(l<=r):
            if(min(nums[l], nums[r]) < smallest):
                smallest = min(nums[l], nums[r])
            l+=1
            r-=1
        return smallest
        