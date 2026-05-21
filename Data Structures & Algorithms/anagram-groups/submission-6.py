class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        fd = {}
        for i, word in enumerate(strs):
            count = [0]*26
            for w in word:
                count[ord(w) - ord('a')]+=1
            key = tuple(count)
            if(key not in fd):
                fd[key]  = []
            fd[key].append(word)
        return list(fd.values())
            


        


