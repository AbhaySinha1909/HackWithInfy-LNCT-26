class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        mp = defaultdict(list)
        for r, c in reservedSeats:
            mp[r-1].append(c-1)
        
        seen_row = 0
        for k in mp:
            seen_row += 1
            valid1 = all(not j in mp[k] for j in range(1, 5))
            valid2 = all(not j in mp[k] for j in range(3, 7))
            valid3 = all(not j in mp[k] for j in range(5, 9))
            res += max(valid2, valid1+valid3)
        
        return res + (n - seen_row) * 2