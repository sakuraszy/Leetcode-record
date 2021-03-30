class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0,head)
        while(head !=None and head.next != None):
            temp = head.val
            head.val =  head.next.val
            head.next.val = temp
            head=head.next.next
        return dummy.next