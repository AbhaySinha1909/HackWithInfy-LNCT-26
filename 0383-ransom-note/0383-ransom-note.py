class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        d = Counter(magazine)
        e = Counter(ransomNote)
        for key in e:
            if e[key] > d[key]:
                return False
        return True