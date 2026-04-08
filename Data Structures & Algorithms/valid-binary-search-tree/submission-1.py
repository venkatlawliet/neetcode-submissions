# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root,left,right):
            if not root:
                return True
            if not left<root.val<right:
                return False
            return check(root.left,left,root.val) and check(root.right,root.val,right)
                
        return check(root,float("-inf"),float("inf"))
        # def check(root):
        #     if not root.left and root.right:
        #         return True
        #     if root.left and root.right and root.left.val<root.val<root.right.val:
        #         left_root=check(root.left)
        #         right_root=check(root.right)
        #         if left_root and right_root:
        #             return True
        #     return False
        # return check(root)