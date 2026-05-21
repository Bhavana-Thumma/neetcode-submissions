class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        for i in range(len(strs)):
            wl = len(strs[i])
            word = strs[i]+' '*(199-wl)+'0'*(3-len(str(wl)))+str(wl)
            e+=word
        return e

    def decode(self, s: str) -> List[str]:
        d =[]
        for i in range(0, len(s), 202):
            wl = int(s[i:i+202][-3:])
            word=s[i:i+wl]
            d.append(word)
        return d

