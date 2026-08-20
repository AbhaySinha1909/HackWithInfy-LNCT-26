class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        summ = sum(nums)
        for i in range(n):
            right = summ - left - nums[i]
            if left == right:
                return i
            i += 1
            left += nums[i-1]

        return -1