from Graph import Graph
from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix
from BinaryTree import BinaryTree
from BinarySearchTree import BST
from MinHeap import MinHeap

if __name__ == '__main__':

    heap = MinHeap()
    heap.insert(6)
    heap.insert(7)
    heap.insert(12)
    heap.insert(17)
    heap.insert(5)
    print(heap.tree)
    print(heap.delete_min())
    print(heap.tree)