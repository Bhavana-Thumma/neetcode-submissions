#O(1) extra space solution using 1st row and 1st col as marker
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        firstrowzero = False
        for c in range(n):
            if matrix[0][c] ==0:
                firstrowzero =True
                break
        for r in range(1,m):
            for c in range(n):
                if matrix[r][c]==0:
                    matrix[r][0]=0
                    matrix[0][c]=0
        for r in range(1,m):
            for c in range(1,n):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        if matrix[0][0]==0:
            for r in range(m):
                matrix[r][0]=0    
        if firstrowzero:
            for c in range(n):
                matrix[0][c]=0
    
        