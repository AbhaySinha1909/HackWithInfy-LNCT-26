class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        n = len(colors)
        for j in range(n-1, -1, -1):
            if colors[j] != colors[0]:
                max_distance = max(max_distance, j)
                break
        
        for i in range(n):
            if colors[i] != colors[n-1]:
                max_distance = max(max_distance, n-1 - i)
                break
        return max_distance