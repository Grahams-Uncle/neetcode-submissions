class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[x**2 + y**2, (x,y)] for x, y in points]
        def partition(l, r):
            pivot = r
            i = l
            for j in range(l, r):
                if dist[j] <= dist[r]:
                    dist[i], dist[j] = dist[j], dist[i]
                    i += 1
            dist[r], dist[i] = dist[i], dist[r]
            return i
                

        L, R = 0, len(points) - 1
        pivot = len(points)
        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return [p[1] for p in dist[:pivot]]
            
