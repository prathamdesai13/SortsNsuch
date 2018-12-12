

class AdjacencyMatrix:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = generate_graph()

    def generate_graph(self):
        mat = [[0] * len(self.nodes) for _ in self.nodes]
        for v in range(len(mat)):
            for u in range(v):
                if (v + 1, u + 1) in self.edges or (u + 1, v + 1) in self.edges:
                    self.mat[v][u] = 1
                    self.mat[u][v] = 1
        return mat