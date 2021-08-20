# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def recur(level,root):
            if root==None:
                return
            if len(result)< level:
                result.append([root.val])
            else:
                result[level-1].append(root.val)
            recur(level+1,root.left)
            recur(level+1,root.right)
        recur(1,root)
        return result