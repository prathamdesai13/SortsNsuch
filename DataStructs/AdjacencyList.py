
class AdjacencyList:

    def __init__(self, nodes, edges,  weights=None):
        self.nodes = nodes
        self.edges = edges
        self.weights = weights
        self.graph = self.generate_graph()

    def generate_graph(self):
        
        graph = {v : [] for v in self.nodes}
        for e in self.edges:
            u, v = e
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = []
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = []
        return graph

    def add_edge(self, edge):
        
        v, u = edge
        if v in self.graph.keys():
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] =[v]

    def bfs(self, start_vertex):

        visited = { v : False for v in self.graph.keys()}

        queue = [start_vertex]
        visited[start_vertex] = True

        path = []

        while len(queue) > 0:
            v = queue[0]
            del queue[0]   
            path.append(v)
            for u in self.graph[v]:
                if not visited[u]:
                    queue.append(u)
                    visited[u] = True
        return path

    def bfs_path(self, start_vertex, end_vertex):

        visited = { v : False for v in self.graph.keys()}

        queue = [start_vertex]
        visited[start_vertex] = True

        while len(queue) > 0:

            v = queue[0]
            del queue[0]

            for u in self.graph[v]:
                if u != end_vertex:
                    if not visited[u]:
                        queue.append(u)
                        visited[u] = True
                else:
                    return True
        return False
    def dfs(self, start_vertex, visited=None):
        
        if visited is None:
            visited = { v : False for v in self.graph.keys() }

        visited[start_vertex] = True
        print(start_vertex)
        for neighbour in self.graph[start_vertex]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited=visited)

    def generate_spanning_tree(self, root):
        # generates spanning tree of graph using breadth first search

        visited = { v : False for v in self.nodes }
        
        q = [root]
        spanning_tree = []

        while len(q) > 0:
            v = q[0]
            del q[0]

            if not visited[v]:
                spanning_tree.append(v)
                visited[v] = True
                for n in self.graph[v]:
                    if not visited[n]:
                        q.append(n)

        if len(spanning_tree) == len(self.nodes):
            return spanning_tree
        print("This graph is not connected, and so no spanning tree exists!")
        return False

    def shortest_path(self, source, end):
        """
        Dijkstras algorithm to find shortest path between
        source node and end node, given weights. If no weights
        are specified for this graph, then edge weights of 1 are
        assigned to every edge.
        """
        weights_flag = False
        if self.weights:
            weights_flag = True

        distance = {v : float('inf') for v in self.graph}
        distance[source] = 0

        visited = {v : False for v in self.graph}
        q = [v for v in self.graph]

        while q:

            v = q[0]
            del q[0]

            if not visited[v]:
                visited[v] = True
                for u in self.graph[v]:
                    if weights_flag:
                        weight_vu = self.weights[(u, v)]
                    else:
                        weight_vu = 1
                    if distance[v] + weight_vu < distance[u]:
                        distance[u] = distance[v] + weight_vu
        print(distance)
        return distance[end]

    