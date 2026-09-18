class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n < r * c or m * n > r * c:
            return mat
        
        new_mat = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                new_mat[n * i + j] = mat[i][j]
        
        re_mat = [[0] * c for _ in range(r)]
        for i in range(len(new_mat)):
            re_mat[i//c][i%c] = new_mat[i]
        
        return re_mat