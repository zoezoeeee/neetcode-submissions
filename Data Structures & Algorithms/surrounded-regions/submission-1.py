class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        q = deque()

        for c in range(n):
            for r in (0, m-1):
                if board[r][c] == 'O' and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))

        for r in range(m):
            for c in (0, n-1):
                if board[r][c] == 'O' and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))               

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    board[nr][nc] == 'O' and
                    (nr, nc) not in visited
                ):
                    q.append((nr, nc))
                    visited.add((nr, nc))

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'