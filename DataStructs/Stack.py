
class Stack:
    # fixed stack of 10 elements
    def __init__(self):
        self.container = [None] * 10
        self.current_index = 0

    def push(self, x):
        self.container[self.current_index] = x
        self.current_index += 1

    def pop(self):
        if not self.isEmpty():
            self.current_index -= 1
            popped_element = self.container[self.current_index]
            self.container[self.current_index] = None
            return popped_element
        print("Stack is empty")

    def size(self):
        return self.current_index
    
    def isEmpty(self):
        if self.size() > 0:
            return False
        return True

    def display(self):
        print(self.container)