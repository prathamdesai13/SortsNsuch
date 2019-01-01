class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, data):

        self.head = Node(data)
        
    def insert(self, data):
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def delete(self, index):

        if index < 0:
            raise IndexError()

        elif index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            while index > 1:
                curr = curr.next
                index -= 1
            if curr:
                curr.next = curr.next.next
            else:
                raise IndexError()

    def search(self, data):
        
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def __str__(self):
        str_rep = ''
        curr = self.head
        while curr:
            str_rep += '[' + str(curr.data) + '] --> '
            curr = curr.next
        str_rep += 'None'
        return str_rep
