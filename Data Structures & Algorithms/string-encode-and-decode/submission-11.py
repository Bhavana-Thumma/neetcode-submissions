class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        if(len(strs) == 0):
            return ''
        for i in (strs):
            suffix = '0'*(3-len(str(len(i))))+str(len(i))
            e+=i+'#'+suffix
        print(e)
        return e

    def decode(self, s: str) -> List[str]:
        d = []
        if(len(s) == 0):
            return d
        new = 0
        for i in range(len(s)+1):
            if(s[i-3:i].isnumeric() and s[i-4]=='#'):
                word = s[new:new+int(s[i-3:i])]
                
                d.append(word)
                new = i
        print(d)
        return d

