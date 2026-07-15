class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v,w))

        minHeap = [(0,k)]
        visited = set()
        t = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            t = weight

            for neighbor, weight2 in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight2 + weight, neighbor))
        
        return t if len(visited) == n else -1
        


            


        
