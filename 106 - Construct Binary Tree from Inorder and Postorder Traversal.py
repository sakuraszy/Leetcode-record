# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        r=None
        def recur(ino):
            if len(ino)<1:
                return None
            root=TreeNode(postorder[-1],None,None)
            postorder.pop(-1)
            if len(ino)==1:
                return root
            i=0
            while(i<len(ino)):
                if ino[i]==root.val:
                    break
                i+=1
            root.right=recur(ino[i+1:])
            root.left=recur(ino[:i])
            return root
        r=recur(inorder)
        return r