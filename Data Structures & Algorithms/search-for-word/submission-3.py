class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set() # (r,c)
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        def backtrack(r, c, i):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited):
                return False

            if board[r][c] != word[i]:
                return False 
            if i == len(word) - 1:
                return True
            visited.add((r,c))
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            visited.remove((r,c))
            return False 


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False 
