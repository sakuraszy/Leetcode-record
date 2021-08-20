# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def recur(level,root,direct):
            #direct=True when right
            if root==None:
                return
            if len(result)< level:
                result.append([root.val])
            else:
                if direct:
                    result[level-1].append(root.val)
                else:
                    result[level-1].insert(0,root.val)
            recur(level+1,root.right,not direct) 
            recur(level+1,root.left,not direct)
                               
        recur(1,root,False)
        return result