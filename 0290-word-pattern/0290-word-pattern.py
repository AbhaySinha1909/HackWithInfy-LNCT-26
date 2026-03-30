class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import Counter
        q = Counter(pattern)
        p = Counter(s.split())
        a = list(q.values())
        b = list(p.values())

        return a == b