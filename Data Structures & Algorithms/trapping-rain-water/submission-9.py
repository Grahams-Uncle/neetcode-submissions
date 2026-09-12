class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        pref = [0] * n
        pref[0] = height[0]
        for i in range(1,n):
            pref[i] = max(pref[i - 1], height[i])
        suff = [0] * n
        suff[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suff[i] = max(suff[i + 1], height[i])
        
        for i, h in enumerate(height):
            res += min(pref[i], suff[i]) - h
        return res 


