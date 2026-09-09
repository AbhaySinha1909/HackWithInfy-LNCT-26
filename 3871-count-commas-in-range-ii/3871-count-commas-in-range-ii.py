class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        k = 1 
        while 10**(3*k) <= n:
            start = 10**(3*k)
            end = min(n, 10**(3*k+3) - 1)
            count = end - start + 1
            total += count * k
            k += 1
        return total