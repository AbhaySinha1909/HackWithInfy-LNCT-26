class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        if k == 1:
            key_arr = [x for x in freq.keys() if freq[x] == 1]
            if len(key_arr) > 0:
                if len(key_arr) == 1:
                    return key_arr[0]
                return max(key_arr)
            else:
                return -1
        
        if k == n:
            return max(nums)
        
        if freq[nums[0]] > 1 and freq[nums[n-1]] == 1:
            return nums[n-1]
        elif freq[nums[0]] == 1 and freq[nums[n-1]] > 1:
            return nums[0]
        elif freq[nums[0]] > 1 and freq[nums[n-1]] > 1:
            return -1
        else:
            return max(nums[0], nums[n-1])