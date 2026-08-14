class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        freq = defaultdict(int)
        result = 0
        for j in range(n):
            freq[s[j]] += 1

            while i < j and freq[s[j]] > 2:
                freq[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
        
        return result