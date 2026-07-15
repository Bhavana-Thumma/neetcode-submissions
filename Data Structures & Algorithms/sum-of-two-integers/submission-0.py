# Sum without + or -; using XOR
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b !=0:
            sum_without_carry = (a^b) & mask
            carry = (a & b) << 1
            a = sum_without_carry
            b = carry
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        return a
            
        