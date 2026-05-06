from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        for row in boxGrid:
            emptyPos = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    emptyPos = j - 1
                elif row[j] == '#':
                    row[j], row[emptyPos] = '.', '#'
                    emptyPos -= 1
        
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]
        
        return rotated
