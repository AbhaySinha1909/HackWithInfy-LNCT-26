class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse_n = int(str(n)[::-1])
        ans = abs(n - reverse_n)
        return ans