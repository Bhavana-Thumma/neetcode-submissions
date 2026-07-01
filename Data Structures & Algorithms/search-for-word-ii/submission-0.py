class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        rows,cols = len(board),len(board[0])
        result = []
        def dfs(r:int, c:int, node:TrieNode):
            ch = board[r][c]
            if ch not in node.children:
                return
            nextnode = node.children[ch]


            if(nextnode.word):
                result.append(nextnode.word)
                nextnode.word = None
            board[r][c] = '#'
            for rc,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+rc,c+cc
                if(0 <= nr < rows and 0 <= nc < cols and board[nr][nc]!='#'):
                    dfs(nr,nc,nextnode)
            board[r][c] = ch
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root)
        return result

        