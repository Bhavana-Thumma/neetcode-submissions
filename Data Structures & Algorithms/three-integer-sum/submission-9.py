class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i=0
        while(i < len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                i+=1
                continue
            target = -nums[i]
            j=i+1
            k=len(nums)-1
            while(j<k):

                if(j<k and nums[j]+nums[k] < target):
                    j+=1
                elif(j<k and nums[j]+nums[k] > target):
                    k-=1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                    j+=1
                    k-=1

            i+=1
        return result