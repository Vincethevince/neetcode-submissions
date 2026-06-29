# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                if i+1 < len(lists):
                    mergedLists.append(self.mergetwoLists(lists[i], lists[i+1]))
                
                else:
                    mergedLists.append(lists[i])

            lists = mergedLists

        return lists[0] if lists else None


    
    def mergetwoLists(self,l1,l2):
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1: 
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
