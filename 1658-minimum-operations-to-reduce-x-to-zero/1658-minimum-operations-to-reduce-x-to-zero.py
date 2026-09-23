class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x
        
        if target < 0:
            return -1

        if target == 0:
            return n
        
        l = 0
        curr_sum = 0
        max_len = -1

        for r in range(n):
            curr_sum += nums[r]
            
            while curr_sum > target and l <= r:
                curr_sum -= nums[l]
                l += 1

            if curr_sum == target:
                max_len = max(max_len, r - l + 1)
            
        
        return -1 if max_len == -1 else n - max_len