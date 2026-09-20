class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        n = len(nums)
        for num in nums:
            if not num:
                zero_cnt += 1
            else:
                prod *= num

        if zero_cnt > 1:
            return [0] * n
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if zero_cnt:
                if not nums[i]:
                    res[i] = prod
            else:
                res[i] = prod // nums[i]
        return res        