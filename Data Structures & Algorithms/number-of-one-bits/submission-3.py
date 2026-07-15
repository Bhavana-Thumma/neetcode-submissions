# n & n-1 => removes one 1 bit
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while(n):
            n = n & n-1
            c+=1
        return c
        