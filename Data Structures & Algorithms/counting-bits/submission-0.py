# Bruteforce
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            num = i
            c =0 
            while(num):
                num &= num-1
                c+=1
            ans.append(c)
        return ans
        