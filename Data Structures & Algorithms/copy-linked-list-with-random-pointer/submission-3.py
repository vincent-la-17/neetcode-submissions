"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = {}
        curr = head
        while curr:
            #create copy of nodes with their values
            #cannot do all 3 at one because curr.next and curr.random may not have been created yet
            old[curr] = Node(curr.val)
            curr = curr.next
        prev = head
        while prev:
            #connect the copy of nodes now.
            old[prev].next = old.get(prev.next)
            old[prev].random = old.get(prev.random)
            prev = prev.next
        return old.get(head)