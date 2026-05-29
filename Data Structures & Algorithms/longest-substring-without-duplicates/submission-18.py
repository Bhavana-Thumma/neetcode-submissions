class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        mc = 0
        seen = set()
        l=0
        for r in range(len(s)):
            while(s[r] in seen):
                seen.remove(s[l])
                l+=1                         
            seen.add(s[r])
            print(seen)     
            mc = max(mc,r-l+1)
        return mc




        