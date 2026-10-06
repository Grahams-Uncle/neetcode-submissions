# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max in the left node

        # max in the right node

        # max using the root 
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            # Use 0 (not include the path)
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            res = max(res, root.val + left + right)

            return root.val + max(left, right)
        dfs(root)
        return res 


            

