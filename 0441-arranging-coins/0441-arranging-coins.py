class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            coin = mid * (mid + 1) // 2 
            if coin == n :
                return mid
            elif coin < n:
                low = mid + 1
            else:
                high = mid - 1
        return high