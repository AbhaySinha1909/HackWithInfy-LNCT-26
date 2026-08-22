class Solution:
    def checkDivisibility(self, n: int) -> bool:
        li = list(str(n))

        summ = 0
        prod = 1

        for i in range(len(li)):
            summ += int(li[i])
            prod *= int(li[i])

        return n % (summ + prod) == 0