class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for course, prerequisite in prerequisites:
            d[course].append(prerequisite)

        visiting = set()
        visited = set()

        def dfs(node):
            visiting.add(node)

            for neighbor in d[node]:
                if neighbor in visiting:
                    return True
                elif neighbor in visited:
                    continue
                else:
                    if dfs(neighbor):
                        return True

            visiting.remove(node)
            visited.add(node)
            return False

        for node in range(numCourses):
            if node not in visited:
                if dfs(node):
                    return False
        
        return True