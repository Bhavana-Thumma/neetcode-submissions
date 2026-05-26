class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for ch in s.lower():
            if(ch.isalnum()):
                l.append(ch)
        s = "".join(l)
        return s[::-1] == s
            
                


        