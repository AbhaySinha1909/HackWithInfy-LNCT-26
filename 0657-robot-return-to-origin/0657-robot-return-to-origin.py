class Solution:
    def judgeCircle(self, moves: str) -> bool:
        num = list(moves)
        result = [0, 0]
        for i in num:
            if i == 'U':
                result[0] += 1
            elif i == 'D':
                result[0] -= 1
            elif i == 'L':
                result[1] -= 1
            else:
                result[1] += 1
        
        return True if result == [0, 0] else False