import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        heap = []
        
        for t in workerTimes:
            heapq.heappush(heap, (t, t, 1))
        
        ans = 0
        
        for _ in range(mountainHeight):
            finish, t, k = heapq.heappop(heap)
            
            ans = max(ans, finish)
            
            k += 1
            next_finish = finish + k * t
            
            heapq.heappush(heap, (next_finish, t, k))
        
        return ans