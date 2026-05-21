class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}    
        for i, word in enumerate(strs):
            ch_count = [0] * 26
            for c in word:
                ch_count[ord(c) - ord('a')] += 1
            key = tuple(ch_count)
            if(key not in d):
                d[key] = []
            d[key].append(word)
        return list(d.values())
            


        


