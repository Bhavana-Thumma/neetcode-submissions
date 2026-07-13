#devide and conquor
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(l,r):
            if l==r:
                return nums[l]
            mid = (l+r)//2
            leftmax= solve(l,mid)
            rightmax = solve(mid+1, r)
            mid = (l+r)//2
            leftsum = float('-inf')
            total = 0
            for i in range(mid,l-1,-1):
                total+=nums[i]
                leftsum = max(leftsum, total)
            total = 0
            rightsum = float('-inf')
            for j in range(mid+1,r+1):
                total+=nums[j]
                rightsum = max(rightsum, total)
            cross = leftsum+rightsum
            return max(leftmax,rightmax, cross)
        return solve(0, len(nums)-1)
        