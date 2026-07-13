#Greedy Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        longest_jump = 0
        for i in range(len(nums)):
            if i>longest_jump:
                return False
            longest_jump = max(longest_jump, i+nums[i])
        return True
    
        