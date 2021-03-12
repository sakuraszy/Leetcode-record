class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        result = ListNode(None)
        count = 1;
        while l1 != None:
            n1 = n1 +l1.val*(10**count)
            n2 = n2 +l2.val*(10**count)
            l1 = l1.next
            l2 = l2.next
            count += 1
        end =list(str(n1+n2));
        end.reverse();
        for i in end:
            result.val = i
            result.next = ListNode(0)
        return result