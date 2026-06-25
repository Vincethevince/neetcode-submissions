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
        
        # slow = last element of left
        last_left = slow
        slow = slow.next
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        last_left.next = None
        right = prev

        left = head
        while left and right:
            tmp1 = left.next
            left.next = right
            tmp2 = right.next
            right.next = tmp1

            left = right.next
            right = tmp2
        
