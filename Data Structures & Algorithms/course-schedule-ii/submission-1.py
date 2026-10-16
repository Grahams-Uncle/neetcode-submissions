class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)] # crs -> downstream courses
        indegree = [0] * numCourses # number of prereq for crs

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        res = []
        while q:
            crs = q.popleft()
            if crs in res:
                return []
            
            res.append(crs)
            for nei in adj[crs]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)

        return res if len(res) == numCourses else []
