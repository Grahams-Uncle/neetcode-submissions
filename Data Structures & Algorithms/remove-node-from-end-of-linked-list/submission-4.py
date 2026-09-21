# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head 
        while cur:
            N += 1
            cur = cur.next
        
        remove = N - n
        if remove == 0:
            return head.next
        cur = head
        idx = 0
        while idx < remove - 1:
            idx += 1
            cur = cur.next
        cur.next = cur.next.next
        return head