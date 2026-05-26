class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        seen = ''
        for i in range(len(s)):
            if(s[i].isalnum()):
                seen += s[i]
        print(seen)
        if(len(seen)%2 == 1):
            return seen[:(len(seen)//2)+1] == seen[(len(seen)//2):][::-1]
        return seen[:len(seen)//2] == seen[len(seen)//2:][::-1]
            
                


        