# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = dummy = ListNode()
        cur.next = head
        prevGroupStart = cur
        prev = None
        frontrunner = cur = cur.next
        groupSize = 1

        while frontrunner:
            frontrunner = frontrunner.next
            groupSize += 1
            if frontrunner and groupSize == k:
                for _ in range(k):
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                
                prevGroupStart.next.next = cur
                tmp2 = prevGroupStart.next
                prevGroupStart.next = prev
                prevGroupStart = tmp2
                frontrunner = cur
                groupSize = 1
        
        return dummy.next

        
    