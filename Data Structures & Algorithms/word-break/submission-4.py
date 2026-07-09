class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp ={}
        def dfs(i):
            if(i in dp):
                return dp[i]
            if i==len(s): #reaching the end
                return True
            ans =False
            for word in wordDict:
                if s.startswith(word,i):
                    ans = dfs(i+len(word))
                    if ans:
                        break # to avoid checking all words
            dp[i]=ans 
            return ans
        return dfs(0)