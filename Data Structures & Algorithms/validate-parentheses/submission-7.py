class Solution:
    def isValid(self, s: str) -> bool:
            d = {'{':'}', '(':')', '[':']'}
            filo = []
            Opt = True
            for i in range(len(s)):                             
                if(s[i] in d):
                    filo.append(s[i])                
                else:                     
                    if(len(filo)>0 and s[i] == d[filo[-1]]):
                        filo.pop(-1)
                    else:
                        return False                       
            return True if filo==[] else False


