class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            preReq[pre].append(course)
            indegree[course] +=1
        

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        res = []
        while q:
            course = q.popleft()
            for c in preReq[course]:
                indegree[c] -=1
                if indegree[c] == 0:
                    q.append(c)
            res.append(course)
        
        return res if len(res) == numCourses else []

                
            
