class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            speed = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            if time <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        return res





            