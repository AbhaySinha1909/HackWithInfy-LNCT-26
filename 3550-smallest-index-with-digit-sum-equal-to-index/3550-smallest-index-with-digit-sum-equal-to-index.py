class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)

        def sum_of_digits(x):
            summ = 0
            while x > 0:
                summ += x % 10
                x //= 10
            return summ
        
        for i in range(n):
            if i == sum_of_digits(nums[i]):
                return i

        return -1