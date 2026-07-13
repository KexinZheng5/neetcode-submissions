# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        while fast != None:
            if count > n:
                slow = slow.next
            fast = fast.next
            count += 1
        
        slow.next = slow.next.next if slow.next else None
        return dummy.next
        