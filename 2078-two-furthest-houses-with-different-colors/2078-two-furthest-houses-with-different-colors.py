class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        n = len(colors)
        for i in range(n):
            for j in range(n):
                distance = 0
                if colors[i] != colors[j]:
                    distance = abs(i-j)
                    max_distance = max(max_distance, distance)
        return max_distance