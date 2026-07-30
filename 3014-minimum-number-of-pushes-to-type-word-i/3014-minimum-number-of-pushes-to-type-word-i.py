class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        siu = 0
        for i in range(n):
            siu += (i//8) + 1
        return siu