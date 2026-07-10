class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        s_di = Counter(s)
        pi = list(s_di.values())
        if len(set(pi)) == 1:
            return True
        else:
            return False