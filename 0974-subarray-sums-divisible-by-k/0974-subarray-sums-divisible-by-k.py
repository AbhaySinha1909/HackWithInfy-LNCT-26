class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        summ = 0
        count = 0

        freq_map = {0 : 1}

        for i in range(n):
            summ += nums[i]
            rem = summ % k
            if rem < 0: # checking for negative remainder 
                rem = rem + k 
            if rem in freq_map:
                count += freq_map[rem]
                freq_map[rem] += 1
            else:
                freq_map[rem] = 1
        
        return count