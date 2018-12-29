# a hash table implement in python with only arrays
# 

class HashTable:

    def __init__(self):
        
        self.size = 100
        self.num_items = 0
        self.table = [[]] * self.size

    def load_factor(self):

        return self.buckets_filled / self.size

    def hash(self, val):
        
        hash = 0
        for c in val:
            hash += ord(c)
        return hash % self.size

    def retrieve(self, index):
        # doesnt even retive the value at index lol
        if index < self.size:
            return self.table[index]
        print("This does not appear to be an index in this table!")

    def remove(self, index):
        
        # supposed to remove the value at index but idk man its late
        
    def is_empty(self):
        
        return True if self.num_items == 0 else False
    
    def insert(self, val):

        index = self.hash(val)
        self.table[index].append(val)
        self.num_items += 1

    def display(self):

        print("Hash table is empty") if self.is_empty() else print(self.table)

    def clear(self):

        self.table = [[] for _ in range(self.size)]
        return True