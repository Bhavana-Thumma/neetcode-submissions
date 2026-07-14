# Using visited matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix), len(matrix[0])
        directions = [(0,1),(1,0), (0,-1), (-1,0)]
        direction = 0
        r, c = 0,0
        res= []
        visited = [[False]*cols for _ in range(rows)]
        for num_elements in range(rows*cols):
            visited[r][c] = True
            res.append(matrix[r][c])
            dr,dc = directions[direction]
            newr = r+dr
            newc= c+dc
            if(0<= newr<rows and 0<=newc<cols and not visited[newr][newc]):
                dr,dc = directions[direction]
                r = newr
                c= newc
            else:
                direction = (direction+1)%4
                dr,dc = directions[direction]
                r = r+dr
                c= c+dc
        return res




        