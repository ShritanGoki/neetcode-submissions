class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            preReq[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for course, reqs in enumerate(indegree):
            if reqs == 0:
                q.append(course)
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)

            for neighbors in preReq[course]:
                indegree[neighbors] -= 1
                
                if indegree[neighbors] == 0:
                    q.append(neighbors)

        return len(res) == numCourses



