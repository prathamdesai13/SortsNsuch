
class BinaryTree:

    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
    
    def __insert__(self, data):
        # insert elements based on ordering : if x > a => x is to the right of a
        if not self.left:
            self.left = BinaryTree(data)
        elif not self.right:
            self.right = BinaryTree(data)
        else:
            self.left.__insert__(data)
    
    def inorder(self):
        # left branch, root node, right branch
        if self.left:
            self.left.inorder()
        if self.data:
            print(self.data)
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        # root node, left branch, right branch
        if self.data:
            print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        # left branch, right branch, root node
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self.data:
            print(self.data)

    def bfs(self):
        pass

    def find(self, x):
        pass

    def height(self):
        left_height = right_height = 0
        
        if self.left:
            left_height = self.left.height()
        
        if self.right:
            right_height = self.right.height()

        return max(left_height, right_height) + 1

    


                

