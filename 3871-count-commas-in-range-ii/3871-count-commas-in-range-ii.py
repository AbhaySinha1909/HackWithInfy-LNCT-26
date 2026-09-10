class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        total_no_of_commas = 0
        k = 1
        while 10**(3*k) <= n:
            start = 10**(3*k)
            end = min(n, 10**(3*k+3) - 1)
            count = end - start + 1
            total_no_of_commas += count * k
            k += 1
        
        return total_no_of_commas