class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        time, fresh = 0, 0
        directions = [[1,0],[0,1], [-1,0],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))
                elif grid[r][c] == 1:
                        fresh += 1
            
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in directions:
                    dr, dc = dr + r, dc + c
                    if (0 <= dr < rows and 0 <= dc < cols
                    and (dr,dc) not in visited and 
                    grid[dr][dc] == 1):
                        q.append((dr,dc))
                        visited.add((dr,dc))
                        fresh -= 1
            time += 1
        
        return -1 if fresh > 0 else time

                
