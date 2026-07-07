# Space Optimized DP
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2=1
        prev1=1
        answer =1
        for i in range(2, n+1):
            answer = prev2+prev1
            prev2=prev1
            prev1=answer
        return answer
        