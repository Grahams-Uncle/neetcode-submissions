class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parents = list(range(n))
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
            
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False 
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parents[py] = px
        self.rank[px] += self.rank[py]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((dist, i, j))
        edges.sort()

        dsu = DSU(len(points))
        res = 0

        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res 
        
                