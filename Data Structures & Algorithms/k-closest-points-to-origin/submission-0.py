class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
    
        heapq.heapify(minHeap)
        res = []
        while len(res)<k:
            res.append(heapq.heappop(minHeap)[1:3])
        return res
        


