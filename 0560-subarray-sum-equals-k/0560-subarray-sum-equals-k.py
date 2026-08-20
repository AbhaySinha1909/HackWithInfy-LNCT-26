class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        summ = 0
        count = 0
        
        freq_map = defaultdict(int)
        freq_map[0] = 1

        for i in range(n):
            summ += nums[i]
            count += freq_map[summ - k]
            freq_map[summ] += 1
        
        return count