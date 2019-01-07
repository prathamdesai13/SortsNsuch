from random import random
from RandyDandyProblems import *
import time
from DataStructs import *


if __name__ == '__main__':
	
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'F'),
             ('B', 'G'), ('C', 'E'), ('D', 'E'), ('E', 'G'),
             ('F', 'G')]

    # generate undirected edge weights
    weights = {
                ('A', 'B') : 1, 
                ('A', 'C') : 2, 
                ('A', 'D') : 3, 
                ('B', 'F') : 3,
                ('B', 'G') : 8, 
                ('C', 'E') : 4, 
                ('D', 'E') : 11, 
                ('E', 'G') : 3,
                ('F', 'G') : 9
                }
    
    for edge in weights:
        flipped_edge  = (edge[1], edge[0])
        if flipped_edge not in weights:
            weights[flipped_edge] = weights[edge]
	
    G = AdjacencyList(nodes, edges, weights=weights)
    print(G.shortest_path('A', 'G'))