
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False 

        parent = list(range(n))
        rank = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x == parent_y:
                # Cycle detected
                return False 
            
            if rank[parent_x] < rank[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            parent[parent_y] = parent_x
            rank[parent_x] += rank[parent_y]
            return True

        for u,v in edges:
            if not union(u, v):
                return False 
        return True



