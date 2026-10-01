class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            cur = a - b
            if cur != 0:
                heapq.heappush(heap, cur)
        return -heap[0] if heap else 0


