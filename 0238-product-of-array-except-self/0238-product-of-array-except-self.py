import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        Prod_L = 1
        for i in range(len(nums)):
            ans[i] = Prod_L
            Prod_L *= nums[i]
        Prod_R = 1
        for i in range(n-1, -1, -1):
            ans[i] *= Prod_R
            Prod_R *= nums[i]           
        return ans