class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        n = len(nums)
        
        for i in range(n):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        answer = -heapq.heappop(nums)
        return answer