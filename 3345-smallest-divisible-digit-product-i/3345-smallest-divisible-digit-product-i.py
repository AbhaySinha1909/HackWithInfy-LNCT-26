class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(a):
            prod = 1
            while a > 0:
                prod *= a%10
                a //= 10
            return prod

        for i in range(n, n+11):
            if digit_product(i) % t == 0:
                return i
        return -1