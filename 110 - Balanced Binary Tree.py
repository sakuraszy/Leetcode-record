# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            if root==None:
                return 0,True
            else:
                left,lb=recur(root.left)
                right,rb=recur(root.right)
                balanced=rb and lb
                if abs(left-right)>1:
                    balanced=False
                return 1+max(left,right),balanced
        return recur(root)[1]
            