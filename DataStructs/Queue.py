from .Stack import Stack

class Queue:

    def __init__(self):

        self.enq_stack = Stack()
        self.deq_stack = Stack()

    def enqueue(self, x):

        self.enq_stack.push(x)

    def dequeue(self):
        
        if not self.enq_stack.isEmpty():
            while not self.enq_stack.isEmpty():
                self.deq_stack.push(self.enq_stack.pop())
            x = self.deq_stack.pop()
            while not self.deq_stack.isEmpty():
                self.enq_stack.push(self.deq_stack.pop())
            return x
        else:
            print("Queue is empty, cannot dequeue")

    def __str__(self):
        return self.enq_stack.__str__()