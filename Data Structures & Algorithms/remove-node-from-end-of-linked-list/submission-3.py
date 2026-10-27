# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0);
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        #moved fast pointer to nth position
        while (fast.next):
            slow = slow.next
            fast = fast.next
        #moved slow pointer to the nth position FROM THE END
        #remove the nth node by setting next to one after
        slow.next = slow.next.next
        return dummy.next
