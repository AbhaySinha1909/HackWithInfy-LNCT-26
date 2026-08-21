class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        max_len = 0
        num_zero = 0

        l = 0

        for r in range(n):
            if nums[r] == 0:
                num_zero += 1
            
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            
            lenn = r - l + 1
            max_len = max(max_len, lenn)

        return max_len
