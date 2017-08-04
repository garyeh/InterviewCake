# Largest Stack
#
# You want to be able to access the largest element in a stack.
#
# class Stack:
#
#     # initialize an empty list
#     def __init__(self):
#         self.items = []
#
#     # push a new item to the last index
#     def push(self, item):
#         self.items.append(item)
#
#     # remove the last item
#     def pop(self):
#         # if the stack is empty, return None
#         # (it would also be reasonable to throw an exception)
#         if not self.items:
#             return None
#         return self.items.pop()
#
#     # see what the last item is
#     def peek(self):
#         if not self.items:
#             return None
#         return self.items[-1]

class MaxStack:

    def __init__(self):
        self.items = []
        self.maxes = []

    def push(self, item):
        self.items.append(item)
        new_max = max(item, get_max())
        self.maxes.append(new_max)

    def pop(self):
        if not self.items:
            return None
        self.maxes.pop()
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        if not self.maxes:
            return None
        return self.maxes[-1]
