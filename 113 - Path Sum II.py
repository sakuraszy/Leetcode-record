# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]
        def recur(path,root):
            if root==None:
                return None
            if root.left==None and root.right==None:
                if sum(path)+root.val==targetSum:
                    result.append(path+[root.val])
            else:
                if root.left !=None:
                    recur(path+[root.val],root.left)
                if root.right !=None:
                    recur(path+[root.val],root.right)
        recur([],root)
        return result