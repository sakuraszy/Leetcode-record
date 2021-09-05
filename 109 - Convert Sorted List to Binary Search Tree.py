# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def recur(values):
            if values==None:
                return None
            temp=values
            if temp.next==None:
                return TreeNode(values.val)
            temp2=values.next.next
            #print('before',temp)
            while(temp2!=None and temp2.next!=None):
                temp=temp.next
                temp2=temp2.next.next
            root=TreeNode(temp.next.val)
            root.right=recur(temp.next.next)
            temp.next=None
            root.left=recur(values)
            return root
        return recur(head) 