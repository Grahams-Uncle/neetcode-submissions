class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while n > 1:
            cur = stones.pop() - stones.pop()
            n -= 2
            if cur > 0:
                l, r = 0, n
                while l < r:
                    mid = (l + r) // 2
                    if stones[mid] < cur:
                        l = mid + 1
                    else:
                        r = mid
                n += 1
                stones.insert(l, cur)
        print(stones)
        return stones[0] if n > 0 else 0


