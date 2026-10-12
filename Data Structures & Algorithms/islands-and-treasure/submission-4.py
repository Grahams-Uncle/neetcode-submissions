class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()

        # add treasure cells into queue
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF:
                    continue 
                grid[nr][nc] = 1 + grid[r][c]
                q.append((nr,nc))
                        

                
