# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        end = head
        currenthead=head
        if head== None or k==0:
            return head
        count = 0
        while (k>-1):
            if end:
                count +=1
                end=end.next
            else:
                k= k%count
                end=head.next
            k-=1
        while(end):
            end=end.next
            currenthead = currenthead.next
        temp = currenthead.next
        currenthead.next = None
        nh=temp
        if temp ==None:
            return head
        while(temp.next):
            temp=temp.next
        temp.next = head
        return nh