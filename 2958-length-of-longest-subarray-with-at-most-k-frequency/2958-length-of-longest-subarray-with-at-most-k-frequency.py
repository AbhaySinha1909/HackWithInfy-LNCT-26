class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        i = 0
        freq = defaultdict(int)
        result = 0
        for j in range(n):
            freq[nums[j]] += 1

            while i < j and freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
        return result