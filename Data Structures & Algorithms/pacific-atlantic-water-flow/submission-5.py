class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or 
                min(r, c) < 0 or 
                r >= ROWS or c >= COLS or 
                heights[r][c] < prevHeight
                ):
                # r or c out of bound
                # sea level going upwards, so prevHeight need to be smaller than height[r][c]
                return 
                
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])
            return 
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # top pac
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # bottom atl

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # left pac
            dfs(r, COLS-1, atl, heights[r][COLS-1]) #right atl

        res = [] 
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res 
