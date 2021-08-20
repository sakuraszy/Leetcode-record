# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def findnext(root):
            #print(root.val)
            if root.left ==None:
                return root.right
            else:
                temp=root.left
                while (temp.right) !=None:
                    temp=temp.right
                temp.right=root
                n=root.left
                root.left=None
                return n
        while(p !=None and q != None):
            if p.val!=q.val:
                return False
            p=findnext(p)
            q=findnext(q)
            #print(p)
            #print(q)
        return p==None and q==None