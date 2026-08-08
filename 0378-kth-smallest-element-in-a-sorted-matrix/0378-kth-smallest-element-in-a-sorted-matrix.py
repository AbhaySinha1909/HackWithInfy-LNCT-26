class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mat = []
        for i in matrix:
            mat.extend(i)
        mat.sort()
        return mat[k-1]