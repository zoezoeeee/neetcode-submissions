class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        distance = 0

        while queue:
            distance += 1
            level_size = len(queue)
            for _ in range(level_size):
                current_r, current_c = queue.popleft()

                for r_offset, c_offset in directions:
                    nr, nc = current_r + r_offset, current_c + c_offset
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = distance
                        queue.append((nr, nc))