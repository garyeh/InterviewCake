# Does this linked list have a cycle?

# class LinkedListNode:
#
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

def contains_cycle(head):
    fast_runner = head
    slow_runner = head

    while fast_runner not None or fast_runner.next not None:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next

        if fast_runner is slow_runner:
            return True

    return False
