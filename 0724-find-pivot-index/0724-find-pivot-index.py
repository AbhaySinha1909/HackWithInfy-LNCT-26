class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i+1]
        
        for i in range(0, len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1