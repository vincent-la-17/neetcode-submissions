# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr != None:
            #
            temp = curr.next
            #curr node's next node is the previous node
            curr.next = prev
            #previous node is now the current node
            prev = curr
            #current node is now it's next node
            curr = temp
        return prev