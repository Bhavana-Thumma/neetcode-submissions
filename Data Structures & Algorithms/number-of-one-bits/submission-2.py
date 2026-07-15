'''
Shift the number
O(32) = O(1)
O(1)
Simpler code using n & 1 and n >>= 1.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        c= 0
        while(n):
            if n & 1:
                c+=1
            n >>= 1
        return c
        