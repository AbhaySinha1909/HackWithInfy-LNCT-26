class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        li = [x for x in range(1, len(s)) if len(s)%x==0]

        for l in li:
            p = s[:l]
            if p * (n//l) == s:
                return True
        return False