# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        prev=None
        slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        second=prev
        while second:
            tmp1,tmp2=head.next,second.next
            head.next=second
            second.next=tmp1
            head,second=tmp1,tmp2
        # if not head:
        #     return
        # ar=[]
        # while head:
        #     ar.append(head)
        #     head=head.next
        # i,j=0,len(ar)-1
        # while i<j:
        #     ar[i].next=ar[j]
        #     i=i+1
        #     if i>=j:
        #         break
        #     ar[j].next=ar[i]
        #     j=j-1
        # ar[i].next=None