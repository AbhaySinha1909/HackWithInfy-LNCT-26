class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = moves.count('L')
        R = moves.count('R')
        underscore = moves.count('_')
        return abs(L - R) + underscore