# 2nd largest item in a BST

# Write a function to find the 2nd largest element in a binary search tree.

# class BinaryTreeNode:
#
#     def __init__(self, value):
#         self.value = value
#         self.left  = None
#         self.right = None
#
#     def insert_left(self, value):
#         self.left = BinaryTreeNode(value)
#         return self.left
#
#     def insert_right(self, value):
#         self.right = BinaryTreeNode(value)
#         return self.right

def find_largest_with_parent(root):
    current = root
    while current.right:
        parent = current
        current = current.right

    return (current, parent)

def find_second_largest(root):
    largest_pair = find_largest_with_parent(root)
    largest = largest_pair[0]
    if largest.left:
        return find_largest_with_parent(largest.left)[0]
    else:
        return largest_pair[1]
