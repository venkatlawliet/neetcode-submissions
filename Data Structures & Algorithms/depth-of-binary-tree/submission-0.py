# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def countdep(root):
            if not root:
                return 0
            left_depth=countdep(root.left)
            right_depth=countdep(root.right)
            return 1+max(left_depth, right_depth)
        return countdep(root)