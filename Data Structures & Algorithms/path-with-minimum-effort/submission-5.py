class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        Rows = len(heights)
        Cols = len(heights[0])
        visited = set()
        minHeap = [(0,0,0)]
        paths = [[1,0], [-1,0], [0,1], [0,-1]]
    

        while minHeap:
            difference, r, c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            elif (r,c) == (Rows - 1, Cols - 1):
                return difference
            visited.add((r,c))
            for row, col in paths:
                newRow = row + r
                newCol = col + c
                if newRow < 0 or newCol < 0 or (newRow, newCol) in visited or newRow == Rows or newCol == Cols:
                    continue
                diff = max(difference, abs(heights[r][c] - heights[newRow][newCol]))
                heapq.heappush(minHeap, (diff, newRow, newCol))
        



            
                
