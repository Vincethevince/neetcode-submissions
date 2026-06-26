# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find N from start
        curr = head
        N = 0
        while curr:
            N +=1
            curr = curr.next
        
        remove = N - n + 1

        if remove == 1:
            return head.next
        N = 1
        curr = head
        while True:
            if N +1 == remove:
                curr.next = curr.next.next
                return head
            else:
                N+= 1
                curr = curr.next