class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                p = s[i:j+1]
                n = Counter(p)
                b = [x for x in n.values()]
                if max(b) <= 2:
                    max_length = max(max_length, sum(b))
        
        return max_length