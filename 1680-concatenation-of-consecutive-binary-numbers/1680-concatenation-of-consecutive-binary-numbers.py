class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        p = ""
        for num in range(n + 1):
            p += format(num, 'b')

        ans = int(p, 2) % mod

        return ans