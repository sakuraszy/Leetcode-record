# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nh=ListNode(0,head)
        r=nh
        count=0
        rl=None
        lh=None
        while(nh):
            print(count)
            if count == left-1:
                lh=nh
                #print(lh)
            if count>=left and count <= right:
                print('yes',count)
                temp=nh
                nh=nh.next
                temp.next=rl
                rl=temp
            else:
                if count==right+1:
                    break
                nh=nh.next
            count +=1
        lh.next=rl
        while(rl.next):
            rl=rl.next
        rl.next=nh
        return r.next
            