class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # Init with a empty board
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(board[r]) for r in range(n)])
                return
            for col in range(n):
                if self.isSafe(row, col, board):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
        backtrack(0)
        return res

    def isSafe(self, row, col, board):
        # Check cols
        # iterate through 0 to (r-1), to check placed Queens
        for r in range(row):
            if board[r][col] == "Q":
                return False

        # Check upper left
        r, c = row - 1, col - 1
        while min(r,c) >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # Check upper right
        r, c = row - 1, col + 1
        while r >=0 and c < len(board[0]):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True