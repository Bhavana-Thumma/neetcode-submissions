# Expand Around Center.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        resLen = 0
        def expand(l,r):
            nonlocal resLen,start
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1 >= resLen):
                    start = l
                    resLen = r-l+1
                l-=1
                r+=1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        return s[start:start+resLen]