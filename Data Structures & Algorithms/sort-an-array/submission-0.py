class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums):
            if len(nums) <= 1:
                return nums
            pivot = nums[len(nums) // 2]

            left = []
            middle = []
            right = []

            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    middle.append(num)
            return quick_sort(left) + middle + quick_sort(right)
        
        return quick_sort(nums)