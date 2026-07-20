class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        li = [x for x in range(n+1)]
        p = ""
        for num in li:
            ch = format(num, 'b')
            p += ch

        ans = int(p, 2) % mod

        return ans