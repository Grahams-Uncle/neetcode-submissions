# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None 
        cur = slow.next
        slow.next = None 
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        l2 = prev
        l1 = head

        while l1 and l2:
            nxt1, nxt2 = l1.next, l2.next
            l1.next = l2
            l2.next = nxt1
            l1 = nxt1
            l2 = nxt2




