from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        bc = Counter(c for r in board for c in r)
        wc = Counter(word)
        if any(wc[ch] > bc[ch] for ch in wc):
            return False
        def backtrack(r, c, i):
            if(i==len(word)):
                return True
            elif(r<0 or r>=len(board) or c<0 or c >= len(board[0]) or
            board[r][c] != word[i]):
                return False
            temp = board[r][c]
            board[r][c] = '#'
            found = (backtrack(r+1,c,i+1)
            or backtrack(r-1,c,i+1)
            or backtrack(r,c+1,i+1)
            or backtrack(r,c-1,i+1))
            board[r][c] = temp
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if(backtrack(r,c,0)):
                    return True
        return False