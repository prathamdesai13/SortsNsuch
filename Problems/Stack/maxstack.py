"""
Implement a class for a stack that supports push and pop along
with an additional function that returns the maximum elemtn in the
stack (return None if stack is empty)

All functions should run in constant time
"""

class Stack:

    def __init__(self):
        self.cache = []
        self.max_stack = []
        
    def push(self, val):
        if len(self.max_stack) == 0 or self.max_stack[-1] <= val:
            self.max_stack.append(val)
        self.cache.append(val)
        
    def pop(self):
        val = self.cache[-1]
        max_val = self.max_stack[-1]
        if val == max_val:
            del self.max_stack[-1]
        del self.cache[-1]
        return val
    
    def max(self):
        return self.max_stack[-1]
    
if __name__ == '__main__':

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max())
    s.pop()
    print(s.max())
    s.pop()
    print(s.max())
    s.pop()
    print(s.max())
