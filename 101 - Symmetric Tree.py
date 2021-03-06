# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(p,q):
            if (q==None or p==None):
                if p ==q:
                    return True
                else:
                    return False
            if p.val!=q.val:
                return False
            else:
                return recur(p.left,q.right) and recur(p.right,q.left)
        return recur(root.left,root.right)