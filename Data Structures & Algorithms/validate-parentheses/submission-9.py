class Solution:
    def isValid(self, s: str) -> bool:
            d = {'}':'{', ')':'(', ']':'['}
            filo = []
            for i in range(len(s)):                             
                if(s[i] in d):          
                    if(not filo or d[s[i]] != filo.pop()):
                        return False    
                else:
                    filo.append(s[i])                    
            return not filo


