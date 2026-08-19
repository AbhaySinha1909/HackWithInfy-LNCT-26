class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        n = len(points)
        cost = 0
        seen = set()
        heap = [(0, 0)]

        while len(seen) < n:
            dis, i = heapq.heappop(heap)
            
            if i in seen:
                continue
            seen.add(i)
            cost += dis

            x, y = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    dis = abs(x-xj) + abs(y - yj)
                    heapq.heappush(heap, (dis, j))
                
        return cost

