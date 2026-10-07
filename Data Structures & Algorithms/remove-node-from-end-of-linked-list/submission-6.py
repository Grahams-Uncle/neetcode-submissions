# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next
        N = len(node_list)
        if N - n == 0:
            return head.next

        node_list[-n-1].next = node_list[-n-1].next.next
        return head