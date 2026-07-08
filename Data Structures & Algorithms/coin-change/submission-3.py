#memoized solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo ={}
        def check(amount):
            if(amount == 0):
                return 0
            
            if(amount in memo):
                return memo[amount]
            result = float('inf')
            for coin in coins:
                if(coin <= amount):
                    result = min(result, 1+check(amount-coin))
            memo[amount] = result
            return result
        ans = check(amount)
        return -1 if ans == float('inf') else ans
