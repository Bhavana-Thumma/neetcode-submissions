class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return nums[0]
        def dfs(nms):
            next1,next2 =0,0
            for i in range(len(nms)-1,-1,-1):
                current = max(next1, nms[i]+next2)
                next2 = next1
                next1 = current
            return current
        return max(dfs(nums[0:n-1]), dfs(nums[1:n]))
        