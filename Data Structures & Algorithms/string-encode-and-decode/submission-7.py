class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        if(len(strs) == 0):
            return ''
        for i in (strs):
            e+=i+'✨'

        print(e)
        return e

    def decode(self, s: str) -> List[str]:
        if(len(s) == 0):
            return []
        d = s[:-1].split('✨')
        return d

