class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq

        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))

        min_time = {}
        heap = [(0, k)]

        while heap:
            time_i, i = heapq.heappop(heap)
            if i in min_time:
                continue
            min_time[i] = time_i
        
            for nei, nei_time in graph[i]:
                if nei not in min_time:
                    heapq.heappush(heap, (nei_time + time_i, nei))
            
        if len(min_time) == n:
            return max(min_time.values())
        else:
            return -1