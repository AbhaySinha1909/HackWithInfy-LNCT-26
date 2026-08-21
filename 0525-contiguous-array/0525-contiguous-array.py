class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)

        a = 0 # no. of 0's
        b = 0 # no. of 1's
        
        freq_map = {}

        result = 0

        for i in range(n):
            if nums[i] == 0:
                a += 1
            else:
                b += 1
            diff = a - b
            if diff == 0:
                result = max(result, i + 1)
            else:
                if diff not in freq_map:
                    freq_map[diff] = i
                else:
                    result = max(result, i - freq_map[diff])
        
        return result