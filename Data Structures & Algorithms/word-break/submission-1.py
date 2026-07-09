class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp ={}
        def dfs(i):
            if(i in dp):
                return dp[i]
            ans =False
            if i==len(s): #reaching the end
                return True
            for word in wordDict:
                if s.startswith(word,i):
                    if dfs(i+len(word)):
                        ans = True
            dp[i]=ans     
            return ans
        return dfs(0)