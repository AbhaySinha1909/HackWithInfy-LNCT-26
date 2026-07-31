class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        t = Counter(word)
        f = sorted(t.values(), reverse=True)
        total = 0

        for i, fr in enumerate(f):
            total += fr * (i // 8 + 1) 
        
        return total