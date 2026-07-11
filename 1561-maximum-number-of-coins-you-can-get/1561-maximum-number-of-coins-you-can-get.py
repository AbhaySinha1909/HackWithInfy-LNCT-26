class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        if n == 3:
            return piles[1]
        
        i, j = 0, n-1
        max_coin = 0
        while n >= 3:
            temp = [piles[i], piles[j-1], piles[j]]
            max_coin += temp[1]
            i += 1
            j -= 2
            n -= 3
        return max_coin