class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        # We use XOR because of two important properties:
        # 1. A number XOR itself becomes 0:
        #       a ^ a = 0
        # 2. A number XOR 0 remains unchanged:
        #       a ^ 0 = a
        #
        # If we XOR all numbers from 0 to n and all numbers in nums,
        # every number that exists in the array will appear twice:
        #
        # Example:
        # Range:  0 ^ 1 ^ 2 ^ 3
        # Array:        0 ^ 1 ^ 3
        #
        # The duplicate numbers cancel each other:
        # (0^0) ^ (1^1) ^ (3^3)
        #
        # Only the missing number remains.
        #
        # We initialize xor with n because the loop below only covers
        # numbers from 0 to n-1. Starting with n includes the entire
        # expected range [0, n].
        xor = n

        for i in range(n):

            # XOR the current index (represents numbers 0 to n-1)
            # with the current array element.
            #
            # Existing numbers will eventually cancel because they appear
            # once from the range and once from nums.
            xor ^= i
            xor ^= nums[i]

        # The only number that does not have a duplicate is the missing number.
        return xor