# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        l1 = head
        l2 = slow.next
        slow.next = None
        curr = l2
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #prev is now the reversed second part of list
        while l1 and prev:
            temp1 = l1.next
            temp2 = prev.next

            l1.next = prev
            prev.next = temp1

            l1 = temp1
            prev = temp2
        