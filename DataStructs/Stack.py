
class Stack:
    # fixed stack of 10 elements
    def __init__(self):
        self.container = [None] * 10
        self.current_index = 0

    def push(self, x):
        if self.size() < 10:
            self.container[self.current_index] = x
            self.current_index += 1
        else:
            print("Stack is full")
    def pop(self):
        if not self.isEmpty():
            self.current_index -= 1
            popped_element = self.container[self.current_index]
            self.container[self.current_index] = None
            return popped_element
        print("Stack is empty, cannot pop")

    def peek(self):
        if not self.isEmpty():
            return self.container[self.current_index - 1]
        print("Stack is empty, cannot peek")

    def size(self):
        return self.current_index
    
    def isEmpty(self):
        if self.size() > 0:
            return False
        return True

    def __str__(self):
        return self.container.__str__()