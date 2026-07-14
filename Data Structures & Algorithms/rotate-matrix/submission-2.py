class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #clockwise 90 = reverse rows(top <-> down) + transpose
        #anti-clockwise 90 = transpose + reverse rows(top <-> down)
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]