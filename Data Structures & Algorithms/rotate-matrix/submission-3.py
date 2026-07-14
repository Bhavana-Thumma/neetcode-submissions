class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    # 90° Clockwise:
    # 1. Reverse the order of the rows (top ↔ bottom)
    # 2. Transpose

    # 90° Counter-clockwise:
    # 1. Transpose
    # 2. Reverse the order of the rows (top ↔ bottom)
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]