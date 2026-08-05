class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]**2
        
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
        
        def gcd_li(nums):
            result = nums[0]
            for num in nums[1:]:
                result = gcd(result, num)
            return result
        
        def lcm(x, y):
            if x == 0 or y == 0:
                return 0
            
            return abs(x*y)//gcd(x,y)
        
        def lcm_li(nums):
            result = nums[0]
            for num in nums[1:]:
                result = lcm(result, num)
            return result

        prefix_gcd = [0] * (n + 1)
        prefix_lcm = [1] * (n + 1)
        for i in range(n):
            prefix_gcd[i+1] = gcd(prefix_gcd[i], nums[i]) if i > 0 else nums[i]
            prefix_lcm[i+1] = lcm(prefix_lcm[i], nums[i])

        suffix_gcd = [0] * (n + 1)
        suffix_lcm = [1] * (n + 1)
        for i in range(n-1, -1, -1):
            suffix_gcd[i] = gcd(suffix_gcd[i+1], nums[i]) if i < n-1 else nums[i]
            suffix_lcm[i] = lcm(suffix_lcm[i+1], nums[i])

        best = gcd_li(nums) * lcm_li(nums)

        for i in range(n):
            g = gcd(prefix_gcd[i], suffix_gcd[i+1])
            l = lcm(prefix_lcm[i], suffix_lcm[i+1])
            best = max(best, g * l)

        return best