class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        minHeap = []
        currentPassengers = 0

        for i in range(len(trips)):
            while minHeap and minHeap[0][0] <= trips[i][1]:
                currentPassengers -= heapq.heappop(minHeap)[1]
            if currentPassengers + trips[i][0] > capacity:
                return False
            else:
                currentPassengers += trips[i][0]
                heapq.heappush(minHeap, [trips[i][2], trips[i][0]])
        
        return True
            