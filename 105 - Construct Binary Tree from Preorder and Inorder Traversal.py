# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        r=None
        def recur(ino):
            if len(ino)<1:
                return None
            root=TreeNode(preorder[0],None,None)
            preorder.pop(0)
            if len(ino)==1:
                return root
            i=0
            while(i<len(ino)):
                if ino[i]==root.val:
                    break
                i+=1
            root.left=recur(ino[:i])
            root.right=recur(ino[i+1:])
            return root
        r=recur(inorder)
        return r