# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while(root):
            if root.left:
                temp=root.right
                root.right=root.left
                root.left=None
                prece=root.right
                while(prece.right):
                    prece=prece.right
                prece.right=temp
            root=root.right