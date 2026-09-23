class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        # Check whether word[i:] can be found starting from board[r][c]
        def backtrack(r, c, i):
            if i >= len(word):
                return True

            if (
                r >= ROWS or r < 0 or 
                c >= COLS or c < 0 or
                word[i] != board[r][c] or
                (r, c) in path
            ):
                return False

            path.add((r,c))
            res = (
                backtrack(r + 1, c, i + 1) or 
                backtrack(r - 1, c, i + 1) or 
                backtrack(r, c + 1, i + 1) or 
                backtrack(r, c - 1, i + 1)
            )

            path.remove((r, c))
            return res

        # Try each cell as a potential starting point
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        
        return False