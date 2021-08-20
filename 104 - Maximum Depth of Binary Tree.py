# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(root):
            if root==None:
                return 0
            else:
                return 1+max(recur(root.left),recur(root.right))
        return recur(root)