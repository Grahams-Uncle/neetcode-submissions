class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        res = 1
        prev_time = (target - cars[0][0]) / cars[0][1]
        for p, s in cars:
            time = (target - p) / s
            if time > prev_time:
                prev_time = time
                res += 1
        return res 





