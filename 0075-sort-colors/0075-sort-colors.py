class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_val = max(nums)
        count = [0] * (max_val + 1)

        for num in nums:
            count[num] += 1
        
        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[index] = i
                index += 1
                count[i] -= 1