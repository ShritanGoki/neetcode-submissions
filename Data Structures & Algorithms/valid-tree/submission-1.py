class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        connections = {i:[] for i in range(n)}
        for node1, node2 in edges:
            connections[node1].append(node2)
            connections[node2].append(node1)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbors in connections[node]:
                if prev != neighbors:
                    if not dfs(neighbors, node):
                        return False
            return True
        if not dfs(0, -1):
            return False
        
        return True if len(visited) == n else False

            