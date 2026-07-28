class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        if len(s) < 2:
            return s
        
        s_di = Counter(s)
        p = dict(sorted(s_di.items()))
        left = []
        middle = ""
        for key,val in p.items():
            m = val // 2
            left.append(key * m)
            if val % 2 == 1 and middle == "":
                middle = key
        l = "".join(left)
        return l + middle + l[::-1]
