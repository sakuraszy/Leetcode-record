# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        r=[]
        while(root or len(stack)!=0):
            print(root)
            if root==None:
                r.append(stack[-1].val)
                root=stack[-1].right
                stack.pop()
            elif root.left!=None:
                stack.append(root)
                root=root.left
            else:
                r.append(root.val)
                if root.right==None:
                    if len(stack)==0:
                        break
                    root=stack[-1].right
                    r.append(stack[-1].val)
                    stack.pop()
                else:
                    root=root.right
        return r