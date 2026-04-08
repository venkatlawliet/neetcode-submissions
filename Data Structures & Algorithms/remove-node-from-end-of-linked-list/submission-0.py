# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        i=0
        while n>0 and right!=None:
            if i==n:
                break
            right=right.next
            i+=1
        while right!=None:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next
        