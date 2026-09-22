class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and q[0] <= r - k:
                q.popleft()

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r + 1 >= k:
                res.append(nums[q[0]])

            r += 1
        return res 

            