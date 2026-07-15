# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findKth(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while head and k > 0:
            head = head.next
            k -= 1
        
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevG = dummy

        while True:
            kth = self.findKth(prevG, k)
            if kth:
                gnext = kth.next

                prev, curr = kth.next, prevG.next
                while curr != gnext:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                temp = prevG.next
                prevG.next = kth
                prevG = temp
            else:
                break
        
        return dummy.next