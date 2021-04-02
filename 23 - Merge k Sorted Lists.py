# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        if (len(lists)==0):
            return None
        if(len(lists)==1):
            return lists[0]
        newl = ListNode(0,None)
        head = newl
        while True:
            index = 0
            min = lists[0]
            for i in range(len(lists)):
                if lists[i]==None:
                    lists.pop(i)
                    min =None
                    break
                elif lists[i].val < min.val:
                    min = lists[i]
                    index =i
            if (min != None):
                newl.next = ListNode(lists[index].val,None)
                lists[index]=lists[index].next
                newl = newl.next
            if len(lists)==0:
                break
        return head.next
                