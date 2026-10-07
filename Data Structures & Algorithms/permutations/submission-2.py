class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        available = [True] * len(nums)

        def dfs(perm, available):
            if len(perm) == len(nums):
                self.res.append(perm.copy())
                return
            for i in range(len(nums)):
                if available[i]:
                    perm.append(nums[i])
                    available[i] = False 
                    dfs(perm, available)
                    perm.pop()
                    available[i] = True

        dfs([], available) 
        return self.res 



