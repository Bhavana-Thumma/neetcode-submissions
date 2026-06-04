class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while(l<r):
            mid=(l+r)//2
            # print(nums[mid], l, r)
            if(nums[mid] > nums[r]):
                l = mid+1
            elif(nums[mid] < nums[r]):
                r=mid
        # print(nums[mid], l, r)    
        return nums[l]