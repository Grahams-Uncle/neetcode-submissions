class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total_sum):
            if total_sum == target:
                res.append(cur.copy())
                return 
            if i >= len(nums) or total_sum > target:
                return
            # With nums[i]
            cur.append(nums[i])
            dfs(i, cur, total_sum + nums[i])
            # Without nums[i]
            cur.pop()
            dfs(i+1, cur, total_sum)
        dfs(0, [], 0)
        return res 
