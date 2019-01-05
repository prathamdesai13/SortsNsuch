# a hash table implement in python with only arrays
# 

class HashTable:

    def __init__(self, size=100):
        
        self.size = size
        self.num_items = 0
        self.table = [[] for _ in range(self.size)]

    def load_factor(self):

        return self.num_items / self.size

    def hash(self, val):
        
        hash_code = 0
        for c in val:
            hash_code += ord(c)
        return hash_code % self.size

    def retrieve(self, key):
        index = self.hash(key)
        collection = self.table[index]
        for kv_pair in collection:
            if kv_pair[0] == key:
                return kv_pair[1]
        print("There is no value associated with the key {}".format(key))

    def remove(self, index):
        
        # supposed to remove the value at index but idk man its late
        pass
        
    def is_empty(self):
        
        return True if self.num_items == 0 else False
    
    def insert(self, key, val):

        index = self.hash(key)
        self.table[index].append((key, val))
        self.num_items += 1

    def display(self):

        if self.is_empty():
            print("Hash table is empty!") 
        else:
            print(self.table)

    def clear(self):

        self.table = [[] for _ in range(self.size)]
        return True