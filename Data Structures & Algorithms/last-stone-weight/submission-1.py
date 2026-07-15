class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-w for w in stones]

        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            else:
                x = x-y
                heapq.heappush(stones, -x)
        
        return -stones[0] if stones else 0
