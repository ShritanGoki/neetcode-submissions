class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preReq[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preReq[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
