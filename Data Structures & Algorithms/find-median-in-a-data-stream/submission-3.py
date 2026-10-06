class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        if self.right_min and self.right_min[0] < num:
            heapq.heappush(self.right_min, num)
        else:
            heapq.heappush(self.left_max, -1 * num)

        if len(self.right_min) > len(self.left_max) + 1:
            val = -1 * heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, val)
        if len(self.left_max) > len(self.right_min) + 1:
            val = -1 * heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, val)

    def findMedian(self) -> float:
        if len(self.right_min) > len(self.left_max):
            return self.right_min[0]
        elif len(self.right_min) < len(self.left_max):
            return -self.left_max[0]
        else:
            return (self.right_min[0] - self.left_max[0]) / 2.0
        