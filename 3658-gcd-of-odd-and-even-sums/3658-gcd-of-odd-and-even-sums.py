class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        sum_even = n*(n+1)
        sum_odd = n**2
        result = math.gcd(sum_even, sum_odd)
        return result