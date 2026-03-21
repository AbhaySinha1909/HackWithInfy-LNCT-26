class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.strip()
        l1 = s1.split()
        s2 = l1[::-1]
        l = " ".join(map(str, s2))
        return l