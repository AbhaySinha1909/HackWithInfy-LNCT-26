class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
        
        ans = gcd(min(nums), max(nums))
        return ans