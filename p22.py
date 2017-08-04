# Delete node

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(node):        
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
print a.next.value
