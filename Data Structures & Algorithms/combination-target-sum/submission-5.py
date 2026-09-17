class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, cur, curSum):
            if curSum == target:
                res.append(cur.copy())
                return 
            if i > n - 1 or curSum > target:
                return 
            cur.append(nums[i])
            dfs(i, cur, curSum + nums[i])
            cur.pop()
            dfs(i + 1, cur, curSum)
        dfs(0,[],0)
        return res




