class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        c=0
        mc = 0
        for i in range(len(s)):
            if(s[i] in seen):
                idx = seen.index(s[i])
                if(idx == len(seen)-1):
                    seen = [s[i]]
                else:
                    seen = seen[idx+1:]
                    seen.append(s[i])
                c = len(seen)
                 
            else:
                c+=1
                seen.append(s[i])
            mc = max(mc, c)

        
        return mc



        