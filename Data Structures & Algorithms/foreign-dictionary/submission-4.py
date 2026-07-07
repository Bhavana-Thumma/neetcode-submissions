from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            if(len(w1)>len(w2) and w1.startswith(w2)):
                return ""
            for c1,c2 in zip(w1,w2):
                if c1!=c2:
                    graph[c1].add(c2)
                    break
        visited={}
        result =[]
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c]=True
            for nei in graph[c]:
                if dfs(nei):
                    return True
            visited[c]=False
            result.append(c)
            return False
        for c in graph:
            if dfs(c):
                return ""
        return "".join(result[::-1])
        


        
        