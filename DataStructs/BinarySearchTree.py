
class BST:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __insert__(self, data):

        if data > self.data:
            if not self.right:
                self.right = BST(data)
            else:
                self.right.__insert__(data)
        else:
            if not self.left:
                self.left = BST(data)
            else:
                self.left.__insert__(data)
    