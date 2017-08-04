# Queue Two Stacks

# Implement a queue with 2 stacks. Your queue should have an enqueue and
# a dequeue function and it should be "first in first out" (FIFO).
# Optimize for the time cost of m function calls on your queue.
# These can be any mix of enqueue and dequeue calls.

class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        self.out_stack.pop()
