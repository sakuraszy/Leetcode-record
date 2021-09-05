# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recur(root,s,target):
            if root==None:
                return False
            if root.left==None and root.right==None:
                return s+root.val ==target
            else:
                return recur(root.left,root.val+s,target) or recur(root.right,root.val+s,target)
        return recur(root,0,targetSum)