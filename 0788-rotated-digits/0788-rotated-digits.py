class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0':'0','1':'1','8':'8','2':'5','5':'2','6':'9', '9':'6'}
        count = 0
        
        for num in range(1, n+1):
            s = str(num)
            rotated = []
            changed = False
            for ch in s:
                if ch not in valid:
                    break
                rotated.append(valid[ch])
                if valid[ch] != ch:
                    changed = True
            else:  # only executes if no break
                if changed:
                    count += 1
        return count