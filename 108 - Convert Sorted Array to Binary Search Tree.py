# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recur(values):
            if values==[]:
                return None
            midpoint=len(values)//2
            root=TreeNode(values[midpoint])
            root.left=recur(values[:midpoint])
            root.right=recur(values[midpoint+1:])
            return root
        return recur(nums)