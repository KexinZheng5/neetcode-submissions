# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        dummy = ListNode()

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        tail = slow.next = None
        while curr:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp


        c1, c2 = head, tail
        while c2:
            temp1, temp2 = c1.next, c2.next
            c1.next = c2
            c2.next = temp1
            c1, c2 = temp1, temp2
