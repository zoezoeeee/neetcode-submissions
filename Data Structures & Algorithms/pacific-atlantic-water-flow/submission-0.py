class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        for c in range(n):
            p_que.append((0, c))
            p_seen.add((0, c))
        
        for r in range(1, m):
            p_que.append((r, 0))
            p_seen.add((r, 0))

        for r in range(m):
            a_que.append((r, n-1))
            a_seen.add((r, n-1))
        
        for c in range(n-1):
            a_que.append((m-1, c))
            a_seen.add((m-1, c))
                        
        def bfs(que: deque, seen: set):
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

            while que:
                cur_r, cur_c = que.popleft()

                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in seen:
                        continue

                    if heights[nr][nc] >= heights[cur_r][cur_c]:
                        seen.add((nr, nc))
                        que.append((nr, nc))
            
            return seen

        p_seen = bfs(p_que, p_seen)
        a_seen = bfs(a_que, a_seen)

        return [list(cell) for cell in p_seen.intersection(a_seen)]