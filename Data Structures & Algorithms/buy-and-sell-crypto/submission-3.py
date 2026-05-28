class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        mp = 0
        for i in range(len(prices)):
            b = min(b, prices[i])
            mp = max(mp, prices[i]-b)
        return mp
        