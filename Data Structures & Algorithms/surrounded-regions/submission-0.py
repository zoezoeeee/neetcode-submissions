class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(r, c):
            region = []
            is_surrounded = True

            q = deque([(r, c)])

            while q:
                r, c = q.popleft()
                region.append((r, c))

                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    is_surrounded = False

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        board[nr][nc] == 'O' and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            if is_surrounded:
                for r, c in region:
                    board[r][c] = 'X'


        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    bfs(r, c)


        