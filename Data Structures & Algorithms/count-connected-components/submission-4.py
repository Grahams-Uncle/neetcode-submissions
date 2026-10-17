class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return False
            
            if rank[px] < rank[py]:
                px, py = py, px
            
            parent[py] = px
            rank[px] += rank[py]
            return True
        
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        return res 
