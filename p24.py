# Reverse a Linked list

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head):
    current = head
    previous = None
    next = None

    while current:
        next = current.next
        current.next = previous

        previous = current
        current = next

    return previous
