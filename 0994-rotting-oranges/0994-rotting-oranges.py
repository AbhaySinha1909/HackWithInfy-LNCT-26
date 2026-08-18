class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten_que = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_que.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        rotten= 2
        minutes = 0

        while rotten_que:
            i, j, minutes = rotten_que.popleft()
            for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    grid[r][c] = rotten
                    fresh -= 1
                    rotten_que.append((r, c, minutes + 1))
        
        return minutes if fresh == 0 else -1