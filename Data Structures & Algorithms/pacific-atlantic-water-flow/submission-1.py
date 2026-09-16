class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        atl, pac = set(), set()

        def dfs(r,c,visited):
            if ((r,c) in visited or 0 > r or r >= rows
                or 0 > c or c >= cols):
                return
            
            visited.add((r,c))
            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                if 0<=newR<rows and 0<=newC<cols and heights[r][c] <= heights[newR][newC]:
                    dfs(newR,newC,visited)
            
            return
        
        for r in range(0, rows):
            dfs(r, 0, pac)
            dfs(rows - r - 1, cols-1, atl)

        for c in range(0, cols):
            dfs(0, c, pac)
            dfs(rows-1, cols - c - 1, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
            
        return res

