class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        mp = 0
        for i in range(len(prices)):
            s = prices[i]
            b = min(b, prices[i])
            print(s, b)
            p = s-b
            mp = max(mp, p)
        return mp
        