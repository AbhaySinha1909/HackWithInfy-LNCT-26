class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sum = 0
        result = inf
        dp = [inf] * n

        l = 0
        
        for r in range(n):
            prefix_sum += arr[r]
            while prefix_sum > target:
                prefix_sum -= arr[l]
                l += 1
            
            dp[r] = dp[r-1] if r-1 >= 0 else inf

            if prefix_sum == target:
                result = min(result, r - l + 1 + (dp[l-1] if l - 1 >= 0 else inf))
                dp[r] = min(dp[r], r - l + 1)
            
        return -1 if result == inf else result