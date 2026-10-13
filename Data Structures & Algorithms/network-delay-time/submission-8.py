class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[k - 1] = 0
        for _ in range(n - 1): # there are only n-1 edges in times if we do not have negative cycle
            for u, v, w in times:
                if dist[u - 1] + w < dist[v - 1]:
                    # found a better route
                    dist[v-1] = dist[u - 1] + w
        max_dist = max(dist)
        return max_dist if max_dist < float("inf") else -1