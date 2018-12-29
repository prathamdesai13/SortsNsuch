
class BST:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):

        if data > self.data:
            if not self.right:
                self.right = BST(data)
            else:
                self.right.insert(data)
        else:
            if not self.left:
                self.left = BST(data)
            else:
                self.left.insert(data)

    def delete(self, data):
        pass

    def search(self, data):
        pass
    