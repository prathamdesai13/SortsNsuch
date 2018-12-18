# min heap in python

class MinHeap:
    # min heap using arrays
    # given the k'th element, its left node is located at
    # index 2k and its right node is located at index 2k + 1
    def __init__(self):
        # element at index zero is ignored
        self.tree = [None]

    def insert(self, val):

        self.tree.append(val)
        val_pos = len(self.tree) - 1
        parent_pos = val_pos // 2
        in_place = False
        while not in_place and val_pos > 1:
            if self.tree[parent_pos] > self.tree[val_pos]:
                self.swap_nodes(parent_pos, val_pos)
                val_pos = parent_pos
                parent_pos = val_pos // 2
            else:
                in_place = True

    def swap_nodes(self, i, j):
        
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]

    def delete_min(self):

        min_val = self.tree[1]
        self.tree[1] = self.tree[-1]
        del self.tree[-1]
        self.heapify(1)
        return min_val
        
    def heapify(self, index):
        
        root = self.tree[index]
        left = self.tree[2 * index]
        right = self.tree[2 * index + 1]

        if left < root:
            self.swap_nodes(index, 2*index)
        
        elif right < root:
            self.swap_nodes(index, 2*index + 1)
        


    