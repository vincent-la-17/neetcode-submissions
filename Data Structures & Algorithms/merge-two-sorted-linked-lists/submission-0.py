# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if (list1 is None):
            return list2
        if (list2 is None):
            return list1
        if (curr1.val <= curr2.val):
            new_head = curr1
            curr1 = curr1.next
        else:
            new_head= curr2
            curr2 = curr2.next
        curr = new_head
        while (curr1 != None) and (curr2 != None):
            
            if (curr1.val <= curr2.val):
                curr.next = curr1
                curr1 = curr1.next
                
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1 is None:
            curr.next = curr2
        elif curr2 is None:
            curr.next = curr1
        return new_head