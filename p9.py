# Binary Search Tree Checker

# Write a function to check that a binary tree is a valid binary search tree.

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

def is_valid_bst(root):
    node_stack = [(root, -float('inf'), float('inf'))]

    while len(node_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            node_stack.append(node.left, lower_bound, node.value))

        if node_right:
            node_stack.append((node.right, node.value, upper_bound))

    return True
