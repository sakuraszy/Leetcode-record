class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newl = ListNode(0,None)
        head = ListNode(0,newl)
        L1= l1
        L2 =l2
        if(L1 ==None):
            return L2
        elif(L2 == None):
            return L1
        while(L1 != None and L2 != None):
            if L1.val >= L2.val:
                newl.next = ListNode(L2.val,None)
                L2=L2.next
            else:
                newl.next = ListNode(L1.val,None)
                L1=L1.next
            newl = newl.next
        if(L1 !=None):
            newl.next = L1
        elif(L2 != None):
            newl.next=L2
        return head.next.next