# Sum without + or -; using XOR
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b !=0:
            swc = (a^b) & mask
            carry = (a & b) << 1
            a = swc
            b = carry
        if a > 0x7FFFFFFF:
            return ~(a^mask)
        return a  