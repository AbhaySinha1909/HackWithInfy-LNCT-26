class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_li = list(s)
        i, j = 0, len(s) - 1
        while i < j :
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            s_li[i], s_li[j] = s_li[j] , s_li[i]
            i += 1
            j -= 1
        return ''.join(map(str, s_li))