class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        n, m = len(heights), len(heights[0])

        for i in range(n):
            p_que.append((i, 0))
            p_seen.add((i, 0))
        
        for j in range(m):
            p_que.append((0, j))
            p_seen.add((0, j))

        for i in range(n):
            a_que.append((i, m-1))
            a_seen.add((i, m-1))
        
        for j in range(m):
            a_que.append((n-1, j))
            a_seen.add((n-1, j))

        def getCoords(que, seen):
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i+i_off, j+j_off
                    if 0<=r<n and 0<=c<m and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))
            return seen
        
        p_coords = getCoords(p_que, p_seen)
        a_coords = getCoords(a_que, a_seen)

        ans = list(p_coords.intersection(a_coords))
        
        return ans