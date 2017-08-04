# K-th to last node in singly linked list

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(k, head):
    total_length = 1
    current = head
    while current.next:
        current = current.next
        total_length += 1

    length = total_length - k
    current = head
    for i in length:
        current = current.next

    return current

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

kth_to_last_node(2, a)
