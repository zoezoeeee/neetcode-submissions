class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = ([0, 1], [0, -1], [1, 0], [-1, 0])
        num_fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                elif grid[r][c] == FRESH:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        num_minutes = 0
        while q:
            q_size = len(q)
            for _ in range(q_size):
                r_rotten, c_rotten = q.popleft()
                for r_offset, c_offset in directions:
                    r = r_rotten + r_offset
                    c = c_rotten + c_offset

                    if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        q.append((r, c))
        
            if q:
                num_minutes += 1

        return num_minutes if num_fresh == 0 else -1



        