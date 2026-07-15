# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        start = head
        l = head
        r = head
        while n > 0:
            r = r.next
            n -= 1
        
        if r is None:
            return head.next

        prev = None
        while r:
            prev = l
            l = l.next
            r = r.next
        
        prev.next = l.next
        return start

        
