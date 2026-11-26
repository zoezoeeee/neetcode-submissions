class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)

        for node1, node2 in edges:
            g[node1].append(node2)
            g[node2].append(node1)
        
        count = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbor in g[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        
        return count