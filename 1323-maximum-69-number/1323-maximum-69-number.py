class Solution:
    def maximum69Number (self, num: int) -> int:
        p = list(str(num))
        if '6' not in p:
            return num
        a = p.index('6')
        p[a] = '9'
        ans = ''.join(p)
        res = int(ans)
        return res