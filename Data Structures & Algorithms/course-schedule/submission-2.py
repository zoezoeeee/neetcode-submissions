class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for course, prerequisite in prerequisites:
            d[course].append(prerequisite)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def hasCycle(node):
            states[node] = VISITING

            for neighbor in d[node]:
                if states[neighbor] == VISITING:
                    return True
                elif states[neighbor] == UNVISITED and hasCycle(neighbor):
                    return True
            
            states[node] = VISITED
            return False
                    
        for node in range(numCourses):
            if states[node] == UNVISITED:
                if hasCycle(node):
                    return False
        return True
