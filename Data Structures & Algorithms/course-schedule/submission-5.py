class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [ [] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        available = deque()
        taken = 0
        for n in range(numCourses):
            if indegree[n] == 0:
                available.append(n)

        while available:
            crs = available.popleft()
            taken += 1
            for c in adj[crs]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    available.append(c)

        #print(taken, numCourses)
        return taken == numCourses
