class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        stable_index = float('inf')
        n = len(nums)
        for i in range(n):
            a = max(nums[:i+1])
            b = min(nums[i:])

            instability_score = a - b

            if instability_score <= k:
                return i
            
    
        return -1