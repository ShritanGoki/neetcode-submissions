class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minH = [[grid[0][0], 0, 0]] #time, r, c
        visited.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while minH:
            time, r, c = heapq.heappop(minH)
            if r == (n-1) and c == (n-1):
                return time

            for dr, dc in directions:
                dr, dc = dr + r, dc + c
                if 0<= dr < n and 0<= dc < n and (dr, dc) not in visited:
                    heapq.heappush(minH, [max(time,grid[dr][dc]), dr, dc])
                    visited.add((dr,dc))
            


        
            

        


