# Balanced Binary Tree

# Write a function to see if a binary tree is "superbalanced"
# (the difference between the depths of any two leaf nodes is no greater than one)

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

# A tree is unbalanced if:
# 1. There are more than 2 different leaf depths
# 2. There are exactly 2 leaf depths and they are more than 1 apart

def is_balanced(root):
    if root == None:
        return True

    depths = []
    nodes = [(root, 0)]

    while len(nodes):

        node, depth = nodes.pop()
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

                if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False

        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True
