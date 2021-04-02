# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        t = ListNode(0,head)
        left = head
        right = t
        while(n>0 and left != None):
            left = left.next
            n-=1
        while(left != None):
            left = left.next
            right = right.next
        right.next = right.next.next
        return t.next
            