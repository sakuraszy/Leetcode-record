# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tos=None
        y=None
        prev=None
        while(root!=None):
            #print(prev)
            if root.left !=None:
                nextnode=root.left
                while(nextnode.right!=None and nextnode.right !=root):
                    nextnode=nextnode.right
                if nextnode.right==None:
                    #print(prev)
                    nextnode.right =root
                    root=root.left
                else:
                    nextnode.right =None
                    if prev and prev.val>root.val:
                        print(root.val)
                        if tos==None:
                            tos=prev
                            y=root
                        else:
                            y=root
                    prev=root
                    root=root.right
                    
            else:
                #left==None
                
                if prev!= None and prev.val > root.val:
                    #print(prev.val,root.val)
                    if tos==None:
                        tos=prev
                        y=root
                    else:
                        y=root
                prev=root
                root=root.right
        print(y.val,tos.val)
        temp=tos.val
        tos.val=y.val
        y.val=temp
        
                
                
                        
                    
                    
                 