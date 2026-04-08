# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls=[]
        q=collections.deque()
        q.append(root)
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                n=q.popleft()
                if n:
                    level.append(n.val)                     
                    q.append(n.left)
                    q.append(n.right)
            if level:
                ls.append(level)
        return ls
        # if not root:
        #     return ls
        # if root:
        #     ls.append([root.val])
        # while root:
        #     if root.left and root.right:
        #         ls.append([root.left.val,root.right.val])
        #     root=root.left
        #     root=root.right
        # return ls