# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def recur(root,level):
            if root==None:
                return
            if len(result)<level:
                result.insert(0,[root.val])
            else:
                result[-level].append(root.val)
            recur(root.left,level+1)
            recur(root.right,level+1)
        recur(root,1)
        return result
            