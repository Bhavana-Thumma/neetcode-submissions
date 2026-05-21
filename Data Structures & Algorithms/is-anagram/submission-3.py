class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # d = {}
        # if(len(s) != len(t)):
        #     return False
        # for i in range(len(s)):
        #     d[t[i]] = d.get(t[i], 0) + 1
        #     d[s[i]] = d.get(s[i], 0) - 1
        # return all(v == 0 for v in d.values())
        c = [0]*26
        for i in s:
            c[ord(i) - ord('a')] +=1
        for i in t:
            c[ord(i) - ord('a')] -=1
        return all(k == 0 for k in c)
        


            

        # s = sorted(s)
        # t = sorted(t)
        # return True if(s ==  t) else False
        # .......................
        # s.split()
        # t.split()
        # s1 = set(s+t)
        # print(s1)
        # for i in s1:
        #     if t.count(i) != s.count(i):            
        #         return False
        # return True
        #..............
        # for i in set(s+t):
        #     if(s.count(i) != t.count(i)):
        #         return False
        # return True
        