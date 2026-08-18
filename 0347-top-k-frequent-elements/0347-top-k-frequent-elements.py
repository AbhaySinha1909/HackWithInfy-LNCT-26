class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        heap = []
        counter = Counter(nums)
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        result = []
        
        while k > 0:
            freq, num = heapq.heappop(heap)
            result.append(num)
            k -= 1
        return result