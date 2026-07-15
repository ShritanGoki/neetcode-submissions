class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if preReq[crs] == []:
                return True
            
            cycle.add(crs)
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
