class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C': 100 , 'D':500, 'M':1000}
        s_li = list(s)
        number = 0 
        for i in range(len(s)-1):
            if symbol[s_li[i+1]] > symbol[s_li[i]]:
                number -= symbol[s_li[i]] 
            else:
                number += symbol[s[i]]
        number += symbol[s_li[-1]]
        return number