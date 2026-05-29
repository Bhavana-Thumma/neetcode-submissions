class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        mc = 0
        seen = dict()
        l=0
        r=0
        c = 0
        while(r<len(s)):
            if(s[r] in seen and seen[s[r]] >= l):
                l = seen[s[r]]+1
                if(l==r):
                    seen = {s[r]: r}
                else:
                    seen[s[r]]=r

            else:
                seen[s[r]]=r
            r+=1 
            c = r-l    
          
            mc = max(mc,c)
        return mc




        