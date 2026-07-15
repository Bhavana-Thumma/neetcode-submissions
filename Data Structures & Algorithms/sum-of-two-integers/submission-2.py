class Solution:
    def getSum(self, a: int, b: int) -> int:

        # Mask to keep numbers within 32 bits
        # Python integers do not overflow automatically like C/Java,
        # so we simulate 32-bit behavior.
        mask = 0xFFFFFFFF

        while b != 0:

            # XOR gives addition without considering carry
            sum_without_carry = (a ^ b) & mask

            # AND finds positions where both bits are 1.
            # Those positions generate carry.
            carry = ((a & b) << 1) & mask

            # Update values for next iteration
            a = sum_without_carry
            b = carry

        # If a is larger than the maximum signed 32-bit integer,
        # it represents a negative number in two's complement.
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a