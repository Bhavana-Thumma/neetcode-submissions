class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxf = 0
        l =0
        d = {}
        for r in range(len(s)):
            d[s[r]]=d.get(s[r], 0)+1
            # maxf = max(maxf, d[s[r]])
            while((r-l+1-max(d.values()))>k):                
                d[s[l]]-=1
                l+=1
            print(r-l+1, maxf, s[l:r+1])
            longest = max(longest, r-l+1)
        return longest
            
                



        