class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for le in range(1, n + 1):
            for left in range(n - le + 1):
                right = left + le - 1
                is_pal[left][right] = s[left] == s[right] and (le <=2 or is_pal[left+1][right-1])
        
        dp = [0] * n

        for i in range(n):
            if i > 0:
                dp[i] = dp[i-1]
            
            for j in range(i-k+2):
                if is_pal[j][i]:
                    prev = dp[j-1] if j-1 >= 0 else 0
                    dp[i] = max(dp[i], prev+1)

        return dp[n-1]