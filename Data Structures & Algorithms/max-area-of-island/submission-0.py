class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            area = 1
            
            while q:
                row, col = q.popleft()
                directions = [[0,-1],[0,1],[1,0],[-1,0]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (0<=r<rows and 0<=c<cols 
                        and (r, c) not in visited
                        and grid[r][c] == 1):
                        q.append((r,c))
                        visited.add((r,c))
                        area += 1

            return area
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c)
                    maxArea = max(area, maxArea)
        
        return maxArea
