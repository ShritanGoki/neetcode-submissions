class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visited = set()
        minHeap = [[0, 0]]

        while len(visited) < n:
            weight, node = heapq.heappop(minHeap)
            if node not in visited:
                visited.add(node)
                res += weight
                for weight2, neighbors in adj[node]:
                    if neighbors not in visited:
                        heapq.heappush(minHeap, [weight2, neighbors])

        return res

        


