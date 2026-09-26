class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Maps each original node to its copied node
        old_to_new = {}

        # First pass: create a copy of every node
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Second pass: connect next and random pointers
        current = head
        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)
            current = current.next

        return old_to_new.get(head)