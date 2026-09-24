# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root,False)]
        heights = {}
        res = 0
        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))

            else:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)
                heights[node] = 1 + max(left, right)
                res = max(res, left + right)
        return res 

