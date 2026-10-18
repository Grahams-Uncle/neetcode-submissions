class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue 
                if dfs(nei, node):
                    return True
            return False 


        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if dfs(u, 0):
                return [u, v]
        return []