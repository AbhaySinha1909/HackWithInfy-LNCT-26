class Solution:
    def intToRoman(self, num: int) -> str:
        th = ["", "M", "MM", "MMM"]
        hd = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tt = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        on = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
        P = (th[num//1000] + hd[(num%1000)//100] + tt[(num%100)//10] + on[num%10])
        return P