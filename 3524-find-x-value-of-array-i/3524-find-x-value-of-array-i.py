class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        dp = [[0]*k for _ in range(n)]

        for i in range(n):
            dp[i][nums[i]%k] += 1
        
            if i == 0:
                continue
            
            for r in range(k):
                dp[i][(r * nums[i]) % k] += dp[i - 1][r]

        for i in range(n):
            for r in range(k):
                result[r] += dp[i][r]
            
        return result