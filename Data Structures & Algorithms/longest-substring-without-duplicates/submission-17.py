class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        mc = 0
        seen = dict()
        l=0
        for r in range(len(s)):
            if(s[r] in seen and seen[s[r]] >= l):
                l = seen[s[r]]+1            
            seen[s[r]]=r       
            mc = max(mc,r-l+1)
        return mc




        