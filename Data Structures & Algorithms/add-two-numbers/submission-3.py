# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()
        over = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            summ = num1 + num2 + over
            over = summ // 10
            val = summ % 10

            curr.next = ListNode(val)

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            curr = curr.next
        
        if over:
            curr.next = ListNode(over)
        
        return head.next