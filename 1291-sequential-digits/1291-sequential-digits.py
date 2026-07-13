class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        n = len(str(low))
        m = len(str(high))
        result = []
        for length in range(n, m+1):
            for i in range(len(s) - length + 1):
                num = int(s[i:i+length])
                if low <= num <= high:
                    result.append(num)
        return sorted(result)