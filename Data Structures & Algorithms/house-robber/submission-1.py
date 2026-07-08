class Solution:
    def rob(self, nums: List[int]) -> int:
        map ={}
        def dfs(i):
            if(i>=len(nums)):
                return 0
            if(i in map):
                return map[i]
            map[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return map[i]
        return dfs(0)