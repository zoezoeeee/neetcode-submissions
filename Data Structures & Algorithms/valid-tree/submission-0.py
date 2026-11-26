class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        g = defaultdict(list)

        for node1, node2 in edges:
            g[node1].append(node2)
            g[node2].append(node1)
        
        visited = set()
        def dfs(node):   
            visited.add(node)

            for neighbor in g[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        if len(visited) < n:
            return False

        return True