# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        ar=[]
        while head:
            ar.append(head)
            head=head.next
        i,j=0,len(ar)-1
        while i<j:
            ar[i].next=ar[j]
            i=i+1
            if i>=j:
                break
            ar[j].next=ar[i]
            j=j-1
        ar[i].next=None