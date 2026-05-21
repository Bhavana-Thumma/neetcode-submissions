class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i, word in enumerate(strs):
            key = "".join(sorted(word))
            if(key not in d):
                d[key] = []
            d[key].append(word)
        return list(d.values())

        


