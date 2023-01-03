class Graph:
    def __init__(self, vertices):
        self.vert = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, start, dest, weight):
        self.graph.append([start, dest, weight])

    def add_node(self, node):
        self.nodes.append(node)

    def print_solution(self, dist: dict):
        print("Vertex Distance from source: ")
        for k, v in dist.items():
            print(" " + k, ": ", v)

    def bellman_ford(self, source):
        # setting all node weights to infinity, nd source to zero
        dist = {i: float("inf") for i in self.nodes}
        dist[source] = 0

        # iterate v-1 times while updating the weights
        for _ in range(self.vert - 1):
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # running one more iteration to check if there is negative cycle
        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("Graph has a negative cycle.")
                return

        self.print_solution(dist)


gr = Graph(5)
gr.add_node("A")
gr.add_node("B")
gr.add_node("C")
gr.add_node("D")
gr.add_node("E")

gr.add_edge("A", "C", 6)
gr.add_edge("A", "D", 6)
gr.add_edge("B", "A", 3)
gr.add_edge("C", "D", 1)
gr.add_edge("D", "C", 2)
gr.add_edge("D", "B", 1)
gr.add_edge("E", "B", 4)
gr.add_edge("E", "D", 2)
gr.bellman_ford("C")
