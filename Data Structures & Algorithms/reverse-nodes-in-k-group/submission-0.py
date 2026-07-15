# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findKth(self, head: Optional[ListNode], k: int) -> bool:
        counter = 0
        curr = head
        while curr and counter < k:
            curr = curr.next
            counter += 1
        
        return counter == k

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        currNew = dummy
        currOld = head
        while currOld:
            if self.findKth(currOld, k):
                tail = None
                nextDummy = currOld
                counter = 0
                while counter < k:
                    temp = currOld.next
                    currOld.next = tail
                    tail = currOld
                    currOld = temp
                    counter += 1
                currNew.next = tail
                currNew = nextDummy
            else:
                currNew.next = currOld
                break
        
        return dummy.next