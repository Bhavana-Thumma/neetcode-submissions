class Solution:
    def countBits(self, n: int) -> List[int]:

        # dp[i] stores the number of 1 bits in the binary representation of i
        dp = [0] * (n + 1)

        # offset represents the largest power of 2 <= current number
        # Example:
        # for numbers 4-7, offset = 4
        # for numbers 8-15, offset = 8
        offset = 1

        for i in range(1, n + 1):

            # When we reach a power of 2, update the offset
            # Example:
            # i = 4 -> offset changes from 2 to 4
            # i = 8 -> offset changes from 4 to 8
            if offset * 2 == i:
                offset = i

            # Every number can be represented as:
            # i = offset + remainder
            #
            # offset contributes exactly one '1' bit
            # remainder = i - offset has already been calculated in dp
            #
            # Example:
            # 13 = 8 + 5
            # binary:
            # 1101 = 1000 + 0101
            #
            # bits(13) = 1 + bits(5)
            dp[i] = 1 + dp[i - offset]

        return dp