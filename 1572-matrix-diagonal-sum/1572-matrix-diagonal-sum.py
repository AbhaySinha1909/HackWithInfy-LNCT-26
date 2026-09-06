class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        dia_sum = 0

        for i in range(n):
            dia_sum += mat[i][i]
            dia_sum += mat[i][n-1-i]
        
        if n%2 == 1:
            dia_sum -= mat[n//2][n//2]
        
        return dia_sum