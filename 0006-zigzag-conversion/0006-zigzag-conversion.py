class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if numRows == 1 or numRows >= n:
            return s

        row = [""] * numRows
        i = 0
        going_down = False
        
        for ch in s:
            row[i] += ch
            if i == 0 or i == numRows - 1 :
                going_down = not going_down 
            if going_down:
                i += 1
            else:
                i -= 1

        ans = "".join(map(str,row))
        return ans