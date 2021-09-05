# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recur(root):
            if root==None:
                return 0
            else:
                left=recur(root.left)
                right=recur(root.right)
                if left==0 and right==0:
                    return 1
                elif left==0:
                    return 1+right
                elif right==0:
                    return 1+left
                else:
                    return 1+min(left,right)
        return recur(root)