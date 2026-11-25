class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            g[prerequisite].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            
            for neighbor in g[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return res if len(res) == numCourses else []