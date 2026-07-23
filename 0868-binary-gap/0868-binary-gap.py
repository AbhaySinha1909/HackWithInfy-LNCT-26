class Solution:
    def binaryGap(self, n: int) -> int:
        import re
        s = format(n, 'b')
        pattern = r'(?=(10*1))'
        matches = re.findall(pattern, s)
        max_p = 0
        for i in matches:
            p = i.count('0') + 1
            max_p = max(max_p, p)
        return max_p