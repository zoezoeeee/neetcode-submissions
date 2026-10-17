class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate rows
        for r in range(9):
            seen = set()
            for c in range(9):
                item = board[r][c]
                if item in seen:
                    return False
                if item != '.':
                    seen.add(item)

        # Validate cols
        for c in range(9):
            seen = set()
            for r in range(9):
                item = board[r][c]
                if item in seen:
                    return False
                if item != '.':
                    seen.add(item)

        # Validate boxes
        starts = (
            [0, 0], [0, 3], [0, 6],
            [3, 0], [3, 3], [3, 6],
            [6, 0], [6, 3], [6, 6]
        )
        
        for r_start, c_start in starts:
            seen = set()
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    item = board[r][c]
                    if item in seen:
                        return False
                    if item != '.':
                        seen.add(item)

        return True