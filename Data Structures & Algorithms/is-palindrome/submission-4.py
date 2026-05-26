class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for ch in s.lower():
            if ch.isalnum():
                chars.append(ch)

        seen = ''.join(chars)

        return seen == seen[::-1]
            
                


        