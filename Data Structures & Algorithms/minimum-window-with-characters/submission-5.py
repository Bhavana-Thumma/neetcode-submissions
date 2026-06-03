from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(s)<len(t)):
            return ''
        t_dic = Counter(t)
        s_dic = {}
        ch_needed = len(t_dic)
        ch_had = 0
        l = 0 
        shortest_len = float('inf')
        shortest_window = (0,0)
        for r in range(len(s)):
            ch = s[r]
            s_dic[ch] = s_dic.get(ch, 0) + 1
            if(ch in t_dic and s_dic[ch] == t_dic[ch]):
                ch_had+=1
            print(l,r)
            while(ch_had == ch_needed):
                if(shortest_len > r-l+1):
                    shortest_len = r-l+1
                    shortest_window = (l,r)
                s_dic[s[l]] = s_dic.get(s[l], 0)-1
                if(s[l] in t_dic and s_dic[s[l]]<t_dic[s[l]]):
                    ch_had -=1
                l+=1

        return "" if shortest_len == float('inf') else s[shortest_window[0]:(shortest_window[1]+1)]
                     


 


            


            

            


        