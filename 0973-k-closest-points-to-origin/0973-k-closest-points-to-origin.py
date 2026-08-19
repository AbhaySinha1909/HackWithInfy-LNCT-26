class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        import heapq
        n = len(points)
        distance = []

        for i in range(n):
            p = points[i][0] ** 2
            q = points[i][1] ** 2
            dis = p + q
            distance.append((dis, [points[i][0], points[i][1]]))
        
        heapq.heapify(distance)

        result = []

        while k > 0:
            a = heapq.heappop(distance)
            result.append(a[1])
            k -= 1
        return result