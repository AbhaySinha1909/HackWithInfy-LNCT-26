class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        n = len(stones)
        
        if n == 1:
            return stones[0]
        
        for i in range(n):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while n >= 2:    
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a == b:
                n -= 2
            else:
                heapq.heappush(stones, -(a-b))
                n -= 1

        return -stones[0] if n == 1 else 0