#DP State
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd,minProd,ans = nums[0],nums[0],nums[0]
        for num in nums[1:]:
            tempMax = max(num, maxProd*num, minProd*num)
            minProd = min(num, maxProd*num, minProd*num)
            maxProd = tempMax
            ans = max(ans,maxProd)
        return ans
                   