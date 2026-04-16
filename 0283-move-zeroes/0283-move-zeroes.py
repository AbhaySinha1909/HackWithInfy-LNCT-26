class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        nums.extend([0] * count_zero)
        return nums