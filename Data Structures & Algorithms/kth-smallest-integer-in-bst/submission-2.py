# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=k
        self.res=root.val
        def cal(root):
            if not root:
                return
            cal(root.left)
            self.count-=1
            if self.count==0:
                self.res=root.val
                return
            cal(root.right)
        cal(root)
        return self.res
        #     if count==k:
        #         break
        #     if not root:
        #         return
        #     cal(root.left)
        #     count+=1
        #     arr.append(root.val)
        #     count+=1
        #     cal(root.right)
        #     count+=1
        # cal(root)
        # return arr[k-1]
        