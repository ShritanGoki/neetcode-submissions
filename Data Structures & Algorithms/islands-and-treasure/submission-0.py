class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        def addCell(r, c):
            if (0 <= r < rows and 0 <= c < cols
                and (r,c) not in visited and grid[r][c] == (2147483647)):
                q.append((r,c))
                visited.add((r,c))

        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r, c+1)
                addCell(r, c-1)
            dist += 1

            

                        
                    
            
