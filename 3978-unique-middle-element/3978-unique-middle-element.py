class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        m = len(nums) // 2
        if nums.count(nums[m]) > 1:
            return False
        else:
            return True 