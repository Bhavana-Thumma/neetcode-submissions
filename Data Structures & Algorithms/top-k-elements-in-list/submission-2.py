from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grps = [[] for i in range(len(nums)+1)] # indexed by freq
        d = Counter(nums)
        final = []
        for key,v in d.items():
            grps[v].append(key)
        f = []
        for i in grps[::-1]:
            if(len(i)>0 and k>0):
                f+=i
                k-=len(i)
        print(f)
        return f


