class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        result.extend(matrix[0])
        result.append(matrix[1][2])
        result.append(matrix[2][2])
        result.append(matrix[2][1])
        result.append(matrix[2][0])
        result.append(matrix[1][0])
        result.append(matrix[1][1])
        return result 