class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r,c):
            if ((r,c) in visited or r < 0 or r>=rows 
                or c < 0 or c>=cols
                or grid[r][c] == "0"):
                return

            visited.add((r,c))
            grid[r][c] = "0"

            for dr, dc in directions:
                newRow = r + dr
                newCol = c + dc
                dfs(newRow, newCol)
            return
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        
        return res


        
            

            
