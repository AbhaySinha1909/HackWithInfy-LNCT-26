class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        L = [0] * n
        R = [0] * n
        L[0], R[n-1] = height[0], height[n-1]
        sum = 0
        for i in range(1, n):
            j = -i -1
            L[i] = max(L[i-1], height[i])
        for i in range(n-2, -1, -1):
            R[i] = max(R[i+1], height[i])
        for i in range(n):
            pot = min(L[i], R[i])
            sum += max(0, pot - height[i])
        return sum
         