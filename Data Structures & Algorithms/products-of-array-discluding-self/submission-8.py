class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]

        suff = 1
        for j in range(n-1, -1, -1):
            res[j] *= suff
            suff *= nums[j]
    
        return res 