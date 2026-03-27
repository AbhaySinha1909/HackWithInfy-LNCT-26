class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def count_live_neighbors(r, c):
            directions = [(-1,-1), (-1,0), (-1,1),
                        (0,-1),         (0,1),
                        (1,-1),  (1,0), (1,1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                    count += 1
            return count
        
        # First pass: mark transitions
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # live → dead
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2   # dead → live
        
        # Second pass: finalize states
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
