class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        fd = {}   
        for i, word in enumerate(strs):
            d = {}
            for w in word:
                d[w] = d.get(w, 0)+1
            if(tuple(sorted(d.items())) not in fd):
                fd[tuple(sorted(d.items()))] = []
            fd[tuple(sorted(d.items()))].append(word)
        return list(fd.values())
            


        


