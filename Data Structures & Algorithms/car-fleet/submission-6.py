class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        stack.append((target - cars[0][0]) / cars[0][1])
        for p, s in cars:
            time = (target - p) / s
            if stack and time > stack[-1]:
                stack.append(time)
        return len(stack)





