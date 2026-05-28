class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        
        m =0
        for l in range(len(prices)):
            r = len(prices)-1
            while(l<r):
                print(prices[r]-prices[l])
                m=max(m, prices[r]-prices[l])
                r-=1
        return m
        