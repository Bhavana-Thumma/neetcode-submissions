# dp solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        c = 0
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if(l==1):
                    dp[i][j] = True
                elif(l==2):
                    dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])
                if(dp[i][j]):
                    c+=1
        return c      