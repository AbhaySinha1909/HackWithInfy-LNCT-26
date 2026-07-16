class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        mx = []
        cur_max = float('-inf')
        for num in nums:
            cur_max = max(cur_max, num)
            mx.append(cur_max)
        
        prefix_Gcd = [0] * len(nums)
        
        for i in range(len(nums)):
            prefix_Gcd[i] = gcd(nums[i], mx[i])
        
        prefix_Gcd.sort()
        summ = 0
        x, y = 0, len(nums) - 1
        
        while x < y:
            temp = [x, y]
            summ += gcd(prefix_Gcd[x], prefix_Gcd[y])
            x += 1
            y -= 1
        return summ