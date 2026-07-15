class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for letter in tasks:
            count[letter] = count.get(letter, 0) + 1
        count = [-s for s in count.values()]
        heapq.heapify(count)
        maxHeap = count
        
        time = 0
        queue = deque() #value, time

        while maxHeap or queue:
            time += 1
            if not maxHeap:
                time = queue[0][1]
            else:
                counter = 1 + heapq.heappop(maxHeap)
                if counter < 0:
                    queue.append([counter, time + n])
            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time
            
            
