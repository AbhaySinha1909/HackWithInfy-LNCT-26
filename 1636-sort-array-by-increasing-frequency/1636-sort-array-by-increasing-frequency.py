class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: (x[1], -x[0]))
        ans = []
        for num, count in sorted_freq:
            ans.extend([num] * count)
        return ans