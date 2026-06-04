from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_dic = Counter(t)
        print(t)
        needed = len(t_dic)
        smallest = float('inf')
        window = (-1,-1)
        for l in range(len(s)):
            s_dic = {}
            had = 0
            for r in range(l,len(s)):
                ch = s[r]
                s_dic[ch] = s_dic.get(ch,0)+1
                if(ch in t_dic and s_dic[ch] == t_dic[ch]):
                    had+=1
                if(had == needed and r-l+1 < smallest):
                    smallest = r-l+1
                    window = (l,r)
        print(window)
        return "" if smallest == float('inf') else s[window[0]: window[1]+1]
        