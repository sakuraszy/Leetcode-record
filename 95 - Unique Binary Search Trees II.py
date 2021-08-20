# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        opt=[i for i in range(1,n+1)]
        def recur(opts):
            #print(opts)
            result=[]
            if len(opts)==0:
                return [None]
            for i in range(len(opts)):
                left=recur(opts[:i])
                right=recur(opts[i+1:])
                for l in left:
                    for r in right:
                        current=TreeNode(opts[i])
                        current.left=l
                        current.right=r
                        result.append(current)
            return result
        return recur(opt)