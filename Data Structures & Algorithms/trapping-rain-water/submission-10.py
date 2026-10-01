class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        pref = [0] * n
        pref[0] = height[0]
        for i in range(1, n):
            pref[i] = max(pref[i - 1], height[i])
        
        suff = [0] * n
        suff[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(pref[i], suff[i]) - height[i]
        return res 
            


