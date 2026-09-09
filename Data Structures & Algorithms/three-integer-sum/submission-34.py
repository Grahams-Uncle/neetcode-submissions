class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        count = Counter(nums)

        for i, a in enumerate(nums):
            if a > 0:
                # Remaining numbers are >= a 
                break
            
            if i and nums[i] == nums[i - 1]:
                continue 
            l, r = i + 1, len(nums) - 1
            while l < r: 
                three = a + nums[l] + nums[r]
                if three > 0:
                    r -= 1
                elif three < 0:
                    l += 1
                else:
                    res.append((a, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                
            