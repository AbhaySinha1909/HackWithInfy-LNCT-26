class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
        count_1 = binary.count("1")
        return count_1